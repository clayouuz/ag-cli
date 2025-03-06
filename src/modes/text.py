from src.modes import register_mode
from src.utils.logger import get_logger

@register_mode("doc")
def handle_text(client, args):
    """文档对话
    
    Args:
        model(str)
        
    
    """
    print("进入文本处理模式")
    # 实现文本处理逻辑