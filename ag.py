#!/usr/bin/env python3
from src.cli import parse_args
from src.api_client import get_client
from src.modes import get_mode_handler

def main():
    args = parse_args()
    client = get_client()
    
    try:
        handler = get_mode_handler(args.mode)
        handler(client, args.model)
    except Exception as e:
        print(f"运行错误: {str(e)}")

if __name__ == "__main__":
    main()