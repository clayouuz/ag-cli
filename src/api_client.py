import os
from openai import OpenAI
from .utils.config import get_config, update_config
from .utils.logger import get_logger

def get_client():
    """创建并返回OpenAI客户端"""
    config_data = get_config()
    logger=get_logger("api_client.get_client")
    if "OPENAI_API_KEY" not in config_data:
        raise ValueError("未找到OPENAI_API_KEY，前往.cache/ag_config.json配置文件中设置")
    else:
        LLM_API_KEY=config_data["OPENAI_API_KEY"]
    if "OPENAI_API_BASE" not in config_data:
        LLM_URL = "https://api.openai.com"
        logger.warning("未找到OPENAI_API_BASE，使用默认值")
        update_config("OPENAI_API_BASE",LLM_URL)
    else:
        LLM_URL=config_data["OPENAI_API_BASE"]
        
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
                
def get_models(client):
    models = client.models.list().to_dict()
    for model in models['data']:
        print(model['id'])