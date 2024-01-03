from datetime import date
from langchain.chat_models import ChatOpenAI
from langchain.agents import tools, initialize_agent, tool, load_tools
from langchain.agents import AgentType
import langchain

llm = ChatOpenAI(
    openai_api_key="TU_API_KEY", 
    model="gpt-3.5-turbo"
    )

@tool
def get_date(dummy: str) -> str:
    """
    Returns the current date. The dummy argument is ignored.
    """
    return str(date.today())

tools = load_tools(["wikipedia"])


langchain.debug = True
agent = initialize_agent(
    tools=tools + [get_date],
    llm=llm,
    agent= AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True,
    handle_parsing_errors=True
)

agent("Cuál fue el primer presidente de Colombia?")
langchain.debug = False
