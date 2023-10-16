# .envの読込み
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# langchain の読込み
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# 環境変数用に os を読込み
import os


API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_RESOURCE_ENDPOINT")
API_TYPE = os.getenv("OPENAI_API_TYPE")
API_VERSION = os.getenv("OPENAI_API_VERSION")
DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")

# 入力をgptに投げて、そのまま答えを返す
def make_res(prompt: str):
    model = AzureChatOpenAI(
        openai_api_base=BASE_URL,
        openai_api_version=API_VERSION,
        deployment_name=DEPLOYMENT_NAME,
        openai_api_key=API_KEY,
        openai_api_type=API_TYPE,
    )
    res = model(
        [
            HumanMessage(content=prompt)
        ]
    )

    return res

# 入力の要約 -> Markdown形式
def create_summarize(query: str):
    res = make_res(
        f"""以下の文を要約して、Markdown形式で出力してください。
        ```
        {query}
        ```
        """
    )

    print(res)
    print(res.content)
    return res

# 入力からのコンテンツ生成 -> Markdown形式に゙出力
def create_summarize_md(query: str):
    res = make_res(
        f"""以下の文章から営業に役に立つコンテンツをmarkdown形式で生成してください.
        フォーマットに従って下さい.

        フォーマット
        //////
        # コンテンツタイトル
        ## 1. タイトル
        　内容
        ## 2.  タイトル
        　内容
        ## 3. タイトル
        　内容
        ## 4. タイトル
        　内容
        ## 5.タイトル


        　内容
        ////////

        ////////

        元の文章は以下の通りです。
        ```
        {query}
        ```
        """
    )

    print(res)
    print(res.content)
    return res



# Markdownでの出力を OutputParser を用いて変換を試みる
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
def create_summarize_md_using_OutputParser(query: str):
    # OutputParserの準備
    response_schemas = [
        ResponseSchema(name="answer", description="ユーザーの質問に対する回答"),
        ResponseSchema(name="source", description="ユーザーの質問への回答に使用されるソース。Webサイトである必要がある。")
    ]

    # フォーマット命令の準備
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()


    # PromptTemplateの準備
    prompt = PromptTemplate(
        template="ユーザーの質問にできる限り答えてください。\n{format_instructions}\n{question}",
        input_variables=["question"],
        partial_variables={"format_instructions": format_instructions}
    )

    _input = prompt.format_prompt(question=query)


    res = make_res(_input.to_string())
    print(res)
    print(res.content)

    # 辞書型にパース
    response = output_parser.parse(res.content)
    print("type:", type(response))
    print("response:", response)

    return response

def create_section_title(query: str, num:int = 5):
    res = make_res(
        f"""以下の文からを要約して、セクションタイトルを{num}個出力してください。
        ```
        {query}
        ```
        """
    )
    return res
