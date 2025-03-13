import argparse
from src.utils.config import Config
def parse_args():
    config = Config()
    parser = argparse.ArgumentParser(
        description="AI对话命令行工具",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        default="chat",
        choices=["chat", "doc"],
        help="选择运行模式"
    )
    parser.add_argument(
        "--api",
        default=config.get("api", default="openai"), 
        help="指定使用的api服务"
    )
    
    parser.add_argument(
        "--model",
        default=config.get("default_model"), 
        help="指定使用的AI模型"
    )
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=config.get("temperature"),
        help="控制生成随机性 (0-2)"
    )
    
    parser.add_argument(
        "--stream",
        type=str,  # 先解析为字符串
        default=config.get("stream"),
        help="是否启用流式输出（True/False）",
    )
    parser.add_argument(
        "--use_proxy",
        type=str,
        default=config.get("use_proxy"),
        help="是否使用代理服务器（True/False）"
    )
    
    args=parser.parse_args()
    from src.utils.logger import get_logger
    logger = get_logger("cli.parse_args")
    logger.debug(f"解析命令行参数：{args}")
    args.stream = args.stream.lower() == "true"
    args.use_proxy = args.use_proxy.lower() == "true"
    
    return args