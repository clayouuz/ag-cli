from .base import BaseAPIClient
from .openai import OpenAIClient
from .gemini import GeminiClient

def get_client(name: str = "openai") -> BaseAPIClient:
    """获取API客户端实例
    
    Args:
        name: API提供商名称，支持"openai"和"gemini"
        
    Returns:
        BaseAPIClient: API客户端实例
        
    Raises:
        ValueError: 如果提供的名称不受支持
    """
    if name.lower() == "openai":
        return OpenAIClient()
    elif name.lower() == "gemini":
        return GeminiClient()
    else:
        raise ValueError(f"不支持的API提供商: {name}")