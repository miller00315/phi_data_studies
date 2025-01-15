
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.deepseek import DeepSeekChat

load_dotenv()

agent = Agent(
    system_prompt='You are a helpful SwiftUI soding assistant', 
   
)

agent.print_response('Create a SwiftUI spring animation', stream=True)


