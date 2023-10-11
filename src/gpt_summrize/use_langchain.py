# .envの読込み
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# langchain の読込み
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# 環境変数用に os を読込み
import os


BASE_URL = os.getenv("RESOURCE_ENDPOINT")
API_KEY = os.getenv("OPENAI_API_KEY")
DEPLOYMENT_NAME = "gpt-35-turbo-test"

def create_summarize(query: str):
    model = AzureChatOpenAI(
        openai_api_base=BASE_URL,
        openai_api_version="2023-07-01-preview",
        deployment_name=DEPLOYMENT_NAME,
        openai_api_key=API_KEY,
        openai_api_type="azure",
    )
    res = model(
        [
            HumanMessage(
                content=f"""以下の文を要約して、Markdown形式で出力してください。
                ```
                {query}
                ```
                """
            )
        ]
    )

    print(res)
    print(res.content)
    return res
