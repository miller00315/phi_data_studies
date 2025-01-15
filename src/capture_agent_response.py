from typing import Iterator
from dotenv import load_dotenv
from phi.agent import Agent, RunResponse
from phi.utils.pprint import pprint_run_response

load_dotenv()

agent = Agent(
    system_prompt='You are a helpful assistant',  
)

response_stream: Iterator[RunResponse] = agent.run("Hi, how are you?", stream=True)

pprint_run_response(response_stream, markdown=True, show_time=True)

