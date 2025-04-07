#modify config
from src.modes import register_mode



@register_mode("setting")
def handle_setting(client,args):
    """设置模式
    """
    from src.utils.config import Config
    config = Config()
    def _print_config():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print("当前配置:")
        for k, v in config.get_all().items():
            print(f"{k}: {v}")
    
    # 修改配置
    while True:
        _print_config()
        key=input("请输入要修改的配置项,输入为空则退出: ")
        if key is None or key == "":
            print("退出设置模式")
            break
        value = input(f"请输入新的值（当前值: {config.get(key)}）: ")
        config.set(key,value)
        print(f"已将 {key} 修改为 {value}")
