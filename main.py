import time
import os
import yaml
from modules import run_app, kill_app, learn_english, log_info, initialize_notifier

def load_config():
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# 加载配置
config = load_config()
DEBUG_MODE = config["DEBUG_MODE"]
TING_EN_APP_PATH = config["TING_EN_APP_PATH"]
TING_EN_IMAGE_NAME = config["TING_EN_IMAGE_NAME"]
WEBHOOK = config["WEBHOOK"]
SECRET = config["SECRET"]
IMAGE_DIR = os.path.join(os.path.dirname(__file__), config["IMAGE_DIR"])

# 初始化通知器
initialize_notifier(WEBHOOK, SECRET)

if __name__ == "__main__":
    while True:

        log_info("Starting new round...")
        learn_english(TING_EN_IMAGE_NAME, TING_EN_APP_PATH, IMAGE_DIR, DEBUG_MODE)
        log_info("Round completed.")

        log_info("Next round will start in 12 hours.")
        time.sleep(60 * 60 * 12 - 60 * 20 - 66)