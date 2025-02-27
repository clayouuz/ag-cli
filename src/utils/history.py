import json
from datetime import datetime
from typing import List, Dict
from cache import cache_dir

_HISTORY_PATH = cache_dir / ".ag_history.json"
_MAX_HISTORY = 100  # 最大保存记录数

def save_history(user_input: str, ai_response: str, model: str) -> None:
    """保存对话记录"""
    history = load_history()
    
    record = {
        "timestamp": datetime.now().isoformat(),
        "user": user_input,
        "ai": ai_response,
        "model": model
    }
    
    history.append(record)
    
    # 保持最多_MAX_HISTORY条记录
    if len(history) > _MAX_HISTORY:
        history = history[-_MAX_HISTORY:]
    
    with open(_HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def load_history(count: int = 10) -> List[Dict]:
    """加载最近的对话记录"""
    try:
        if not _HISTORY_PATH.exists():
            return []
            
        with open(_HISTORY_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
            return history[-count:]
    except Exception as e:
        print(f"加载历史记录失败: {str(e)}")
        return []

def clear_history() -> None:
    """清空历史记录"""
    if _HISTORY_PATH.exists():
        _HISTORY_PATH.unlink()