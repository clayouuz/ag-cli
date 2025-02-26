# 在src/modes/__init__.py中添加路由逻辑
import importlib
import pkgutil

_mode_handlers = {}

def register_mode(mode_name):
    """模式注册装饰器"""
    def decorator(func):
        _mode_handlers[mode_name] = func
        return func
    return decorator

def get_mode_handler(mode_name):
    """获取模式处理器"""
    handler = _mode_handlers.get(mode_name)
    if not handler:
        raise NotImplementedError(f"未注册的模式: {mode_name}")
    return handler

# 自动导入所有子模块 -------------------------------------------------
__all__ = []
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name != "__init__":
        importlib.import_module(f".{module_name}", __name__)
        __all__.append(module_name)