
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from agent_tools import all_tools

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

agent = create_react_agent(
    model=llm,
    tools=all_tools,
    prompt=(
        "You are an IT production support assistant. "
        "Investigate incidents using application status, logs, "
        "and knowledge base tools. "
        "Do not invent errors or resolutions. "
        "Create an incident only when no reliable resolution is found. "
        "Never claim a fix was applied unless a tool confirms it."
    )
)

if __name__ == "__main__":
    response = agent.invoke({
        "messages": [
            ("user", "Investigate Payment API errors and suggest a resolution.")
        ]
    })

    for message in response["messages"]:
        print(message.type, ":", message.content)
