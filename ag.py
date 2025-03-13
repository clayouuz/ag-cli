#!/usr/bin/env python3
from src.cli import parse_args
from src.modes import get_mode_handler
from src.utils.logger import get_logger
from src.utils.proxy import activate_proxy
from src.api.gemini import GeminiClient
from src.api.openai import OpenAIClient

def main():
    args = parse_args()
    logger = get_logger("main")
    if args.use_proxy:
        activate_proxy()
        logger.info("已启用代理服务器")
    client = OpenAIClient() if args.api == "openai" else GeminiClient()
        
    try:
        handler = get_mode_handler(args.mode)
        handler(client,args)
    except Exception as e:
        logger.error(f"运行错误: {str(e)}")
        print(f"运行错误: {str(e)}")

if __name__ == "__main__":
    main()