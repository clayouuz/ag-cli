from src.modes import register_mode
from src.api_client import basic_chat

@register_mode("chat")
def handle_chat(client, model, temperature=0.7):
    """交互式聊天处理"""
    print("进入AI对话模式（输入'exit'退出）")
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            response = basic_chat(
                client, 
                user_input,
                model=model,
                temperature=temperature
            )
            print(f"\nAI: {response}")
            
        except KeyboardInterrupt:
            print("\n对话已终止")
            return
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return