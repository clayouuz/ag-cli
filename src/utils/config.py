import json
from typing import Dict, Any
from .cache import cache_dir


_CONFIG_PATH = cache_dir / ".ag_config.json"
_DEFAULT_CONFIG = {
    "default_model": "gpt-3.5-turbo",
    "temperature": 0.7,
    "max_history": 50,
    "log_level": "INFO",
    "OPENAI_API_KEY": "改为你的API_KEY",
    "OPENAI_API_BASE":"https://api.openai.com"
}

def get_config() -> Dict[str, Any]:
    """获取配置信息"""
    if not _CONFIG_PATH.exists():
        save_config(_DEFAULT_CONFIG)
        return _DEFAULT_CONFIG
    
    try:
        with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"读取配置失败，使用默认配置: {str(e)}")
        return _DEFAULT_CONFIG

def save_config(config: Dict[str, Any]) -> None:
    """保存配置信息"""
    try:
        with open(_CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存配置失败: {str(e)}")

def update_config(key: str, value: Any) -> None:
    """更新单个配置项"""
    config = get_config()
    config[key] = value
    save_config(config)
