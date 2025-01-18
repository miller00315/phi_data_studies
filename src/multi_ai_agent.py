import openai
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

web_search_agent = Agent(
    name= 'Web search agent',
    model=OpenAIChat(id='gpt-4o-mini'),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name='Finacial AI Agent',
    model=OpenAIChat(id='gpt-4o'),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True
        )
    ],
    instructions=['Use tables to display data'],
    show_tool_calls=True,
    markdown=True    
)

multi_ai_Agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=['Always include sources', 'Use tables to display data'],
    show_tool_calls=True,
    markdown=True
)

multi_ai_Agent.print_response('Summarize analyst recommendations and share the latest news for NVDA', stream=True)