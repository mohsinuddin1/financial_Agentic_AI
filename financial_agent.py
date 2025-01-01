from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 
import openai


import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

websearch_agent=Agent(
    name="Web Search Agent",
    role="search the web for the information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,
)

financial_agent=Agent(
    name="Finance AI Agent",
    role="search the web for the information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YFinanceTools(stock_price=True , analyst_recommendations=True , 
                         stock_fundamentals=True ,  company_news=True),
                         ],
    instructions=["use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[websearch_agent,financial_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("comapare tesla and nvidea which one should one buy",stream=True)