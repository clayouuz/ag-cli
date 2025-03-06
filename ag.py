#!/usr/bin/env python3
from src.cli import parse_args
from src.api_client import get_client
from src.modes import get_mode_handler
from src.utils.logger import get_logger
from src.utils.proxy import activate_proxy

def main():
    args = parse_args()
    client = get_client()
    logger = get_logger("main")
    if args.use_proxy:
        activate_proxy()
    
    try:
        handler = get_mode_handler(args.mode)
        handler(client, args)
    except Exception as e:
        logger.error(f"运行错误: {str(e)}")
        print(f"运行错误: {str(e)}")

if __name__ == "__main__":
    main()