from src.modes import register_mode
from src.utils.logger import get_logger
import sys
import io
import os
import msvcrt

@register_mode("stdin")
def handle_stdin(client, args):
    """
    处理来自stdin的输入，支持管道输入和文件输入
    """
    model = args.model
    temperature = args.temperature
    stream = args.stream
    logger = get_logger()
    
    # 读取输入内容
    try:
        user_input = ""
        is_pipe = False
        try:
            # 检查是否存在管道输入
            is_pipe = not sys.stdin.isatty()
            logger.debug(f"检测到管道输入: {is_pipe}")
        except Exception as e:
            logger.debug(f"检查管道状态时出错: {str(e)}")
            is_pipe = True
        
        if is_pipe:
            # Windows系统
            if os.name == 'nt':
                logger.debug("Windows系统，尝试读取管道输入")
                
                try:
                    # 读取原始数据
                    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
                    raw_data = sys.stdin.buffer.read()
                    
                    # 尝试不同的编码
                    encodings = ['utf-8', 'gbk', 'cp936', sys.getdefaultencoding()]
                    
                    for encoding in encodings:
                        try:
                            user_input = raw_data.decode(encoding)
                            logger.debug(f"成功使用 {encoding} 解码输入")
                            break
                        except UnicodeDecodeError:
                            continue
                    
                    # 如果所有编码都失败，使用替换错误处理
                    if not user_input:
                        user_input = raw_data.decode('utf-8', errors='replace')
                        logger.debug("使用替换错误处理解码输入")
                    
                    logger.debug(f"Windows读取完成，长度: {len(user_input)}")
                    
                except Exception as e:
                    logger.debug(f"Windows读取失败: {str(e)}")
            else:
                # Unix系统直接读取
                logger.debug("Unix系统，读取管道输入")
                user_input = sys.stdin.read()
        
        if user_input:
            logger.debug(f"读取内容前20个字符: {repr(user_input[:20])}")
        
        # 如果管道输入为空，尝试命令行参数
        if not user_input or not user_input.strip():
            if hasattr(args, 'input') and args.input:
                user_input = args.input
                logger.debug(f"使用命令行参数作为输入: {args.input[:20]}...")
        
        # 最终检查输入是否为空
        if not user_input or not user_input.strip():
            logger.error("错误: 输入内容为空")
            print("错误: 输入内容为空，请提供有效的输入")
            print("用法: 使用管道输入 (例如: echo 'input' | ag)")
            print("      或提供参数 (例如: ag -m stdin -i 'input')")
            return
        
        # 发送到AI
        logger.debug(args.prompt)
        response = ""
        user_input=args.prompt+'\n'+user_input
        for chunk in client.chat(user_input, model=model, temperature=temperature, stream=stream):
            response += chunk
            print(chunk, end="", flush=True)  # 逐块输出
        print()  # 最后换行
        
        # 记录响应
        logger.debug(f"AI响应完成，响应长度: {len(response)} 字符")
        
    except Exception as e:
        logger.error(f"处理输入或生成响应时出错: {str(e)}")
        import traceback
        logger.debug(f"详细错误信息: {traceback.format_exc()}")
        print(f"错误: {str(e)}")