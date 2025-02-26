from src.modes import register_mode


@register_mode("text")
def handle_text(client, model):
    """文本批处理模式"""
    print("进入文本处理模式")
    # 实现文本处理逻辑