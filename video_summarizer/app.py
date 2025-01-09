import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import mimetypes

import time
import tempfile
import os
from pathlib import Path

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY is not None:
    genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Multimodal AI Agent - Video Summarizer",
    page_icon=":robot_face:",
    layout="wide",
)

st.title("Phidata Video Summarizer AI Agent")
st.header("Powered by Gemini 2.0 Flash exp")

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video Summarizer Agent",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )
try:
    multimodal_agent = initialize_agent()
except Exception as e:
    st.error(f"Failed to initialize the agent: {e}")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a video file",
    type=["mp4", "mov", "avi", "mkv"],
    help="Upload a video for AI analysis. Supported video formats: mp4, mov, avi, mkv"
)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        video_path = temp_file.name

    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "What insights are you seeking from this video summarizer?",
        placeholder="Ask anything about the video content. The AI agent will analyze and gather additional insights about the video.",
        help="Provide specific questions or insights you want from the video."
    )

    if st.button("Analyze video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please provide a question or insights to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Detect MIME type
                    mime_type, _ = mimetypes.guess_type(video_path)
                    if not mime_type:
                        mime_type = "video/mp4"  # Fallback to a default MIME type

                    # Upload file with MIME type
                    processed_video = upload_file(video_path, mime_type=mime_type)

                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

                    analysis_prompt = (
                        f"Analyze the uploaded video content and summarize for content and context.\n"
                        f"Respond to the following query using video insights and supplementary web research results: {user_query}\n\n"
                        f"Provide a detailed, user-friendly, and actionable response."
                    )
                    response = multimodal_agent.run(analysis_prompt, videos=[processed_video])

                    st.subheader("Video Summarizer AI Agent Response")
                    st.markdown(response.content)

            except Exception as e:
                st.error(f"Error processing video: {e}")
            finally:
                Path(video_path).unlink(missing_ok=True)

# Customize text area height
st.markdown(
    """
    <style>
    .stTextArea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

