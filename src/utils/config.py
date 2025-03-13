import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

class Config:
    """配置管理类
    
    负责读取、保存和更新配置信息
    """
    _instance = None  # 单例模式
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        from .cache import cache_dir
        self._config_path = cache_dir / ".ag_config.json"
        self._default_config = {
            "default_model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_history": 50,
            "OPENAI_API_KEY": "",
            "OPENAI_API_BASE": "https://api.openai.com/v1",
            "GEMINI_API_KEY": "",
            "GEMINI_API_BASE": "https://generativelanguage.googleapis.com",
            "stream": "True",
            "use_proxy": "False",
            "proxy_url": "",
        }
        
        self._config = self._load_config()
        self._initialized = True
    
    def _load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        if not self._config_path.exists():
            print("未找到配置文件，创建默认配置")
            self._save_config(self._default_config)
            return self._default_config.copy()
        try:
            with open(self._config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"读取配置失败，使用默认配置: {str(e)}")
            return self._default_config.copy()
    
    def _save_config(self, config: Dict[str, Any]) -> bool:
        """保存配置到文件
        
        Args:
            config: 要保存的配置字典
            
        Returns:
            bool: 保存是否成功
        """
        try:
            self._config_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存配置失败: {str(e)}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项
        
        Args:
            key: 配置项键名
            default: 默认值，如果未找到配置项则返回此值
            
        Returns:
            配置项的值
        """
        # 先检查环境变量
        env_value = os.environ.get(key)
        if env_value is not None:
            return env_value
            
        # 再检查配置文件
        if key not in self._config:
            self.set(key, default)
        return self._config.get(key, default or self._default_config.get(key))
    
    def set(self, key: str, value: Any) -> bool:
        """设置配置项
        
        Args:
            key: 配置项键名
            value: 配置项值
            
        Returns:
            bool: 设置是否成功
        """
        self._config[key] = value
        return self._save_config(self._config)
    
    def get_all(self) -> Dict[str, Any]:
        """获取所有配置
        
        Returns:
            Dict[str, Any]: 所有配置的副本
        """
        return self._config.copy()
