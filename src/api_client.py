import os
from openai import OpenAI
from dotenv import load_dotenv


def get_client():
    """创建并返回OpenAI客户端"""
    dotenv_path = '.env'
    load_dotenv(dotenv_path)
    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("未找到OPENAI_API_KEY环境变量")
    else:
        LLM_API_KEY=os.environ["OPENAI_API_KEY"]
    if "OPENAI_API_BASE" not in os.environ:
        LLM_URL = "https://api.openai.com"
    else:
        LLM_URL=os.environ["OPENAI_API_BASE"]
        
    return OpenAI(
        api_key=LLM_API_KEY,
        base_url=LLM_URL
        )

def basic_chat(client, prompt, model="gpt-3.5-turbo", temperature=0.7, stream=False):
    """基础对话功能，支持流式输出
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        stream=stream  # 是否启用流式输出
    )
    if not stream:
        # 非流式模式，直接返回完整结果
        yield response.choices[0].message.content
    else:
        # 流式模式，返回一个生成器
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content