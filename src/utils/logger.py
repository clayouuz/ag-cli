import logging
import atexit
import signal
import sys
import os
from logging.handlers import TimedRotatingFileHandler
from .cache import cache_dir
from .config import Config

class GlobalLogger:
    """全局单例日志类"""
    _instance = None
    _initialized = False
    
    @classmethod
    def get_logger(cls):
        """获取全局唯一的日志记录器实例"""
        if cls._instance is None:
            logger = logging.getLogger("ag_global")
            
            if not cls._initialized:
                cls._setup_logger(logger)
                cls._initialized = True
                
            cls._instance = logger
        
        return cls._instance
    
    @classmethod
    def _setup_logger(cls, logger):
        """设置日志处理器"""
        config=Config()
        log_level=config.get(key='log_level',default='DEBUG')
        numeric_level = getattr(logging, log_level.upper(), None)
        logger.setLevel(numeric_level)
        
        # 创建日志目录
        log_dir = cache_dir / ".ag_logs"
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / "ag.log"
        
        # 文件处理器（按天轮转，保留7天）
        file_handler = TimedRotatingFileHandler(
            log_file,
            when="midnight",
            interval=1,
            backupCount=7,
            encoding="utf-8"
        )
        # 包含文件位置的格式化
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(pathname)s:%(lineno)d \n\t %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        
        # 控制台处理器
        console_handler = logging.StreamHandler()
        # 控制台也包含文件位置
        console_formatter = logging.Formatter(
            "%(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(logging.INFO)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # 注册退出时关闭handlers
        cls._register_shutdown_handlers(logger)
    
    @staticmethod
    def _register_shutdown_handlers(logger):
        """注册退出处理函数，确保日志文件正确关闭"""
        # 标准Python退出
        def cleanup_handlers():
            for handler in logger.handlers[:]:
                handler.flush()  # 先刷新缓冲区
                handler.close()
                logger.removeHandler(handler)
        
        atexit.register(cleanup_handlers)
        
        # 捕获CTRL+C信号
        original_sigint = signal.getsignal(signal.SIGINT)
        
        def sigint_handler(sig, frame):
            logger.warning("接收到中断信号，正在关闭日志...")
            # 确保先刷新所有日志
            for handler in logger.handlers:
                handler.flush()
            
            cleanup_handlers()
            
            if callable(original_sigint):
                original_sigint(sig, frame)
            else:
                # 如果没有原始处理器，则使用默认行为
                sys.exit(1)
        
        signal.signal(signal.SIGINT, sigint_handler)


# 获取全局唯一的logger的函数
def get_logger(name=None):
    """获取全局唯一的logger实例"""
    return GlobalLogger.get_logger()


# 使用示例
if __name__ == "__main__":
    logger = get_logger()
    logger.info("日志模块示例输出")