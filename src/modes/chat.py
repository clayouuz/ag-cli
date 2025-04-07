from src.modes import register_mode

from src.utils.typewriter import typewriter_print
from src.utils import history
from src.utils.logger import get_logger

@register_mode("chat")
def handle_chat(client,args):
    """交互式聊天处理，支持流式和非流式输出
    
    Args:
        model(str): 使用的模型名称
        temperature(float): 生成文本的随机性，默认为 0.7
        stream(bool): 是否启用流式输出，默认为 False
    """
    model=args.model
    temperature=args.temperature
    stream=args.stream
    logger = get_logger()
    
    while True:
        try:
            user_input = input("\n🤓👆: ")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            print(f"\n🤖({model}): ", end="", flush=True)  # 不换行并立即刷新缓冲区
            response = ""
            # for chunk in client.chat(client, user_input, model=model, temperature=temperature, stream=stream):
            for chunk in client.chat(user_input, model=model, temperature=temperature, stream=stream):
   
                response += chunk
                # print(chunk, end="", flush=True)  # 逐块输出
                typewriter_print(chunk, delay=0.002, end="")  # 逐块输出
            print()  # 最后换行
            
            history.save_history(user_input, response, model)
            logger.debug(f"用户输入: {user_input[:50]}... | AI响应: {response[:50]}...")
        except Exception as e:
            logger.error(f"发生错误: {str(e)}")
