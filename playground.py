# from phi.agent import Agent
# import phi.api
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
# from phi.model.groq import Groq 
# from phi.playground import Playground,serve_playground_app
# from dotenv import load_dotenv
# import os
# import phi

# load_dotenv()

# phi_api_key = os.getenv("PHI_API_KEY")
# groq_api_key = os.getenv("GROQ_API_KEY")


# groq_model = Groq(id="llama3-groq-70b-8192-tool-use-preview")

# web_search_agent= Agent(
#   name="web_search",
#   role="a web search agent",
#   tools=[DuckDuckGo()],
#   model=groq_model,
#   instructions="Always include sources",
#   show_tools_calls = True,
#   markdown = True,
# )

# financial_agent = Agent(
#   name="Finance Agent",
#   role="a financial agent",
#   tools=[YFinanceTools(stock_price=True,stock_fundamentals=True, analyst_recommendations=True,company_info=True, company_news=True)],
#   model=groq_model,
#   instructions="Use Tables to display the data.",
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

# app= Playground(agents=[financial_agent,web_search_agent]).get_app()

# if __name__=="__main__":
#   serve_playground_app("playground:app",reload=True)


from financialagent import agents  # Import agents from financialagent.py
from phi.playground import Playground, serve_playground_app

# Create the Playground application
app = Playground(agents=agents).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
