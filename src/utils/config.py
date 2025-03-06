import json
from typing import Dict, Any
from .cache import cache_dir
class Config():
    '''
    配置类  
    find(key) 查找单个配置项  
    update(key, value) 更新单个配置项
    '''
    def __init__(self) -> None:
        self._CONFIG_PATH = cache_dir / ".ag_config.json"
        self._DEFAULT_CONFIG = {
            "default_model": "gpt-3.5-turbo",
            "temperature": 0.7,
            "max_history": 50,
            "log_level": "WARNING",
            "OPENAI_API_KEY": "改为你的API_KEY",
            "OPENAI_API_BASE":"https://api.openai.com",
            "use_proxy": False,
        }
        self.details = self._DEFAULT_CONFIG
        
        if not self._CONFIG_PATH.exists():
            print("未找到配置文件，使用默认配置")
            self._save(self._DEFAULT_CONFIG)
            get_logger('config').warning("未找到配置文件，使用默认配置")
        try:
            with open(self._CONFIG_PATH, "r", encoding="utf-8") as f:
                self.details = json.load(f)
        except Exception as e:
            print(f"读取配置失败，使用默认配置: {str(e)}")

    def _save(self,config: Dict[str, Any]) -> None:
        """保存配置信息"""
        try:
            with open(self._CONFIG_PATH, "w", encoding="utf-8") as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存配置失败: {str(e)}")

    def update(self,key: str, value: Any) -> None:
        """更新单个配置项"""
        config = self.get_config()
        config[key] = value
        self._save(config)
        
    def get(self,key: str , create=True) -> Any:
        """查找单个配置项"""
        if create and key not in self.details:
            self.details[key] = key + ' not fond'
            self._save(self.details)
            from .logger import get_logger
            get_logger('config').warning(f"未找到配置项：{key}")
        return self.details[key]