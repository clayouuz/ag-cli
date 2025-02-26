from src.modes import register_mode
from src.api_client import basic_chat
from src.utils.typewriter import typewriter_print
from src.utils import history, logger

@register_mode("chat")
def handle_chat(client,args):
    """交互式聊天处理，支持流式和非流式输出
    
    Args:
        model(str): 使用的模型名称，默认为 "gpt-3.5-turbo"
        temperature(float): 生成文本的随机性，默认为 0.7
        stream(bool): 是否启用流式输出，默认为 False
    """
    model=args.model
    temperature=args.temperature
    stream=args.stream
    log = logger.get_logger("chat_mode")
    
    typewriter_print("Establishing agent control, standby ", delay=0.01, end='')
    typewriter_print("... ", delay=0.3, end='\n')
    #wait for openAI client to be ready
    
    while True:
        try:
            user_input = input("\n🤓👆: ")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            print(f"\n🤖({model}): ", end="", flush=True)  # 不换行并立即刷新缓冲区
            response = ""
            for chunk in basic_chat(client, user_input, model=model, temperature=temperature, stream=stream):
                response += chunk
                print(chunk, end="", flush=True)  # 逐块输出
            print()  # 最后换行
            
            history.save_history(user_input, response, model)
            log.debug(f"用户输入: {user_input[:50]}... | AI响应: {response[:50]}...")
            
        except KeyboardInterrupt:
            print("\n对话已终止")
            log.warning("用户手动终止对话")
            return
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return
