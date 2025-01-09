# from phi.agent import Agent
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# from phi.model.groq import Groq 

# from dotenv import load_dotenv
# import os

# load_dotenv()

# phi_api_key = os.getenv("PHI_API_KEY")
# groq_api_key = os.getenv("GROQ_API_KEY")


# groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview")

# web_search_agent= Agent(
#   name="web_search",
#   role="a web search agent",
#   tools=[DuckDuckGo()],
#   model=groq_model,
#   instructions=["Always include sources"],
#   show_tools_calls = True,
#   markdown = True,
# )

# financial_agent = Agent(
#   name="Finance Agent",
#   role="a financial agent",
#   tools=[YFinanceTools(stock_price=True,stock_fundamentals=True, analyst_recommendations=True,company_info=True, company_news=True)],
#   model=groq_model,
#   instructions=["Use Tables to display the data."],
#   show_tools_calls = True,
#   markdown = True,
# )

# multimodal_ai_agent = Agent(
#   team=[web_search_agent, financial_agent],
#   instructions=["Use Tables to display the data.","Always include sources"],
#   model=groq_model,
#   show_tool_calls=True,
#   markdown=True,
# )

# multimodal_ai_agent.print_response("Summarize analyst recommendations and share the latest news for Tesla", stream=True)

from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

phi_api_key = os.getenv("PHI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview")

# Define Web Search Agent
web_search_agent = Agent(
    name="web_search",
    role="a web search agent",
    tools=[DuckDuckGo()],
    model=groq_model,
    instructions=["Search the web for a given query and return results."],
    show_tools_calls=True,
    markdown=True,
)

# Define Financial Agent
financial_agent = Agent(
    name="Finance Agent",
    role="a financial agent",
    tools=[
        YFinanceTools(
            stock_price=True,
            stock_fundamentals=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    model=groq_model,
    instructions=[
        "Analyze stock data, fundamentals, and news for a given stock symbol.",
        "Use Tables to display the data.",
    ],
    show_tools_calls=True,
    markdown=True,
)

# Define Multimodal AI Agent
multimodal_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    instructions=[
        "Use Tables to display the data.",
        "Always include sources.",
        "Summarize analyst recommendations and provide the latest news.",
    ],
    model=groq_model,
    show_tool_calls=True,
    markdown=True,
)

agents = [web_search_agent,financial_agent,multimodal_ai_agent]  # Export multimodal_ai_agent for the Playground


