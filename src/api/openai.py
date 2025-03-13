from typing import Dict, Any, Generator, Optional
from openai import OpenAI
from .base import BaseAPIClient
from ..utils.config import Config

class OpenAIClient(BaseAPIClient):
    """OpenAI API客户端实现"""
    
    def __init__(self):
        """初始化OpenAI客户端"""
        config = Config()
        self.api_key = config.get("OPENAI_API_KEY")
        self.base_url = config.get("OPENAI_API_BASE")
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def chat(self, 
             prompt: str, 
             model: str = None, 
             temperature: float = 0.7, 
             stream: bool = False) -> Generator[str, None, None]:
        """发送聊天请求到OpenAI API
        
        Args:
            prompt: 用户输入的提示
            model: 使用的模型名称，默认使用配置中的默认模型
            temperature: 温度参数
            stream: 是否使用流式输出
            
        Returns:
            Generator: 生成器，产生响应文本
        """
        config = Config()
        if model is None:
            model = config.get("default_model")
            
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            stream=stream
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
    