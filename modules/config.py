import os
import yaml
from modules.notifier import log_info

# 路径常量
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.yaml")
EXAMPLE_PATH = os.path.join(CONFIG_DIR, "config.example.yaml")

def create_default_config():
    """
    如果 config.yaml 不存在，则根据 config.example.yaml 创建默认配置文件。
    """
    if not os.path.exists(EXAMPLE_PATH):
        log_info(f"未找到示例配置文件：{EXAMPLE_PATH}")
        exit(1)
    with open(EXAMPLE_PATH, "r", encoding="utf-8") as f:
        default_config = yaml.safe_load(f)
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        yaml.dump(default_config, file, default_flow_style=False, allow_unicode=True)
    log_info(f"已创建默认配置文件：{CONFIG_PATH}")
    input("请修改配置文件，然后按回车键继续...")
    # 不再退出程序，直接返回
    return

def load_config():
    """
    加载配置文件，并确保其键与示例配置一致（缺失则补充，多余则删除）。
    :return: dict，最终的配置字典
    """
    if not os.path.exists(CONFIG_PATH):
        log_info(f"未找到配置文件：{CONFIG_PATH}，正在创建默认配置...")
        create_default_config()
        return load_config()  # 递归调用以加载新创建的配置
    with open(EXAMPLE_PATH, "r", encoding="utf-8") as f:
        example_config = yaml.safe_load(f)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        user_config = yaml.safe_load(f)
    # 只保留示例中的键，缺失则补充，多余则删除
    new_config = {}
    updated = False
    for key in example_config:
        if key in user_config:
            new_config[key] = user_config[key]
        else:
            new_config[key] = example_config[key]
            updated = True
    if set(user_config.keys()) != set(example_config.keys()):
        updated = True
    # 如有变更则写回
    if updated:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            yaml.dump(new_config, f, default_flow_style=False, allow_unicode=True)
    return new_config

_config_cache = None

def get_config(key=None):
    """
    获取配置项，支持按需获取单个键或全部配置。
    :param key: str，可选，配置项名称
    :return: 对应配置项的值或整个配置字典
    """
    global _config_cache
    if _config_cache is None:
        _config_cache = load_config()
    if key:
        return _config_cache.get(key)
    return _config_cache