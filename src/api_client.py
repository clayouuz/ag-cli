import os
from openai import OpenAI
from .utils.config import Config
from .utils.logger import get_logger

def get_client(name="openai"):
    """创建并返回OpenAI客户端或Gemini客户端"""
    config = Config()
    logger=get_logger("api_client.get_client")
    LLM_API_KEY=config.get("OPENAI_API_KEY",create=True)
    if name=="gemini":
        LLM_URL=config.get("GEMINI_API_BASE",create=True)
    else:
        LLM_URL=config.get("OPENAI_API_BASE",create=True)
        
    return OpenAI(
        api_key=LLM_API_KEY,
        base_url=LLM_URL
    )

def basic_chat(client, prompt, model="gemini-2.0-flash", temperature=0.7, stream=False):
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
                
def get_models(client):
    models = client.models.list().to_dict()
    for model in models['data']:
        print(model['id'])