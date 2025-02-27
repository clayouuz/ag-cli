from src.modes import register_mode
from src.api_client import basic_chat
from src.utils.typewriter import typewriter_print

@register_mode("chat")
def handle_chat(client, model, temperature=0.7):
    """交互式聊天处理"""
    typewriter_print("Establishing agent control, standby ", delay=0.01, end='')
    typewriter_print("... ", delay=0.3, end='\n')
    while True:
        try:
            user_input = input("\n🤓👆: ")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            response = basic_chat(
                client, 
                user_input,
                model=model,
                temperature=temperature
            )
            print(f"\n🤖({model}): {response}")
            
        except KeyboardInterrupt:
            print("\n对话已终止")
            return
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return