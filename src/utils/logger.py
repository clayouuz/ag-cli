import logging
from logging.handlers import TimedRotatingFileHandler
from .cache import cache_dir
from .config import get_config

def get_logger(name=__name__):
    """获取带有文件轮转功能的日志记录器"""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    
    config_data = get_config()
    logger.setLevel(config_data["log_level"])
    
    log_dir = cache_dir / ".ag_logs"
    log_dir.mkdir(exist_ok=True)
    
    # 文件处理器（按天轮转，保留7天）
    file_handler = TimedRotatingFileHandler(
        log_dir / "ag.log",
        when="midnight",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# 使用示例
if __name__ == "__main__":
    logger = get_logger('example')
    logger.info("日志模块示例输出")