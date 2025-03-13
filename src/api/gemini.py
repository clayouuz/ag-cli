from typing import Dict, Any, Generator, Optional
from google import genai
from google.genai import types
from .base import BaseAPIClient
from ..utils.config import Config
from ..utils.logger import get_logger

class GeminiClient(BaseAPIClient):
    """Gemini API客户端实现
    
    使用OpenAI兼容接口访问Gemini API
    """
    
    def __init__(self):
        """初始化Gemini客户端"""
        config = Config()
        self.api_key = config.get("GEMINI_API_KEY")
        self.base_url = config.get("GEMINI_API_BASE")
        self.client = genai.Client(
            api_key=self.api_key,
            http_options={'base_url': self.base_url}
        )
    
    def chat(self, 
             prompt: str, 
             model: str = "gemini-2.0-flash", 
             temperature: float = 0.7, 
             stream: bool = False) -> Generator[str, None, None]:
        """发送聊天请求到Gemini API
        
        Args:
            prompt: 用户输入的提示
            model: 使用的模型名称
            temperature: 温度参数
            stream: 是否使用流式输出
            
        Returns:
            Generator: 生成器，产生响应文本
        """
        if not stream:
            # 非流式模式，直接返回完整结果
            response = self.client.models.generate_content(
                model=model,
                contents=[prompt],
                config=types.GenerateContentConfig(
                    temperature=temperature
                )
            )
            yield response.text
        else:
            # 流式模式，返回一个生成器
            response = self.client.models.generate_content(
                model=model,
                contents=[prompt],
                config=types.GenerateContentConfig(
                    # system_instruction="chat",
                    temperature=temperature
                )
            )
            for chunk in response:
                content = chunk.text
                if content is not None:
                    yield content
