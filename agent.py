
from llm import gemini
from tools import live_cricket_score


from langchain.agents import create_agent

agent = create_agent(
    model=gemini,
    system_prompt = "You are a helpful assistant",
    # tools = [live_cricket_score]
)
