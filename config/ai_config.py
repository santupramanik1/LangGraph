# from langchain_openai import ChatOpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI(
#     model="openai/gpt-4o-mini",
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
# )

# prompt="how are you"

#     # ask the question to llm
# answer=model.invoke(prompt).content

# print (answer)


from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=1000
)

