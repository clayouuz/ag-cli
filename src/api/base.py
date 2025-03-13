from abc import ABC, abstractmethod
from typing import Dict, Any, Generator, Optional, Union

class BaseAPIClient(ABC):
    """API客户端基类
    
    所有特定API客户端都应继承此类并实现其方法
    """
    
    @abstractmethod
    def chat(self, 
             prompt: str, 
             model: str = None, 
             temperature: float = 0.7, 
             stream: bool = False) -> Generator[str, None, None]:
        """发送聊天请求
        
        Args:
            prompt: 用户输入的提示
            model: 使用的模型名称
            temperature: 温度参数
            stream: 是否使用流式输出
            
        Returns:
            Generator: 生成器，产生响应文本
        """
        pass
    
