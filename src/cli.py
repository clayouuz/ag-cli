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
        # choices=["chat", "doc"],
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
        default=config.get("temperature",default=0.7),
        help="控制生成随机性 (0-2)"
    )
    
    parser.add_argument(
        "--stream",
        type=lambda x: (str(x).lower() == 'true'),
        default=config.get("stream"),
        help="是否启用流式输出(True/False)",
    )
    parser.add_argument(
        "--use_proxy",
        type=lambda x: (str(x).lower() == 'true'), 
        default=config.get("use_proxy"),
        help='是否使用代理 (true 或 false)'
    )
    
    args=parser.parse_args()
    from src.utils.logger import get_logger
    logger = get_logger()
    logger.debug(f"解析命令行参数：{args}")
    
    return args