import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="AI对话命令行工具",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        "--mode",
        type=str,
        default="chat",
        choices=["chat", "text"],
        help="选择运行模式"
    )
    
    parser.add_argument(
        "--model",
        default="gpt-3.5-turbo",
        help="指定使用的AI模型"
    )
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="控制生成随机性 (0-2)"
    )
    
    return parser.parse_args()