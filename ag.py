#!/usr/bin/env python3
from src.cli import parse_args
from src.modes import get_mode_handler
from src.utils.logger import get_logger
from src.utils.proxy import activate_proxy
from src.api import get_client


def main():
    args = parse_args()
    logger = get_logger()
    if args.use_proxy:
        activate_proxy()
        logger.info("已启用代理服务器")
        
    client = get_client(args.api)
    logger.debug("client connected")
    try:
        handler = get_mode_handler(args.mode)
        handler(client,args)
    except Exception as e:
        logger.error(f"运行错误: {str(e)}")

if __name__ == "__main__":
    main()