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
        default="gemini-1.5-flash",
        help="指定使用的AI模型"
    )
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="控制生成随机性 (0-2)"
    )
    
    parser.add_argument(
        "--stream",
        type=str,  # 先解析为字符串
        default="False",  # 默认值为字符串 "False"
        help="是否启用流式输出（True/False）",
    )
    args=parser.parse_args()
    args.stream = args.stream.lower() == "true"
    
    return args