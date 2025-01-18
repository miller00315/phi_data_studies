from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()


web_agent = Agent(
    name= 'Web agent',
    model=OpenAIChat(id='gpt-4o-mini'),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)

web_agent.print_response("Whats happening in USA elections", stream=True)
