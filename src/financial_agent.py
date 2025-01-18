import openai
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

financial_agent = Agent(
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

financial_agent.print_response('Summarize analyst recommendations for Apple', stream=True)