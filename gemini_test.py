from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)

response = llm.invoke(
    "Explain DB_CONNECTION_TIMEOUT in one simple sentence."
)

print(response.content)