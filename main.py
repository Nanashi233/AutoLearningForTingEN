import time
import os
import yaml
from modules import learn_english, log_info, initialize_notifier, is_time_to_run

def load_config():
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# 加载配置
config = load_config()
DEBUG_MODE = config["DEBUG_MODE"]
RUN_TIME = config["RUN_TIME"]
TING_EN_APP_PATH = config["TING_EN_APP_PATH"]
TING_EN_IMAGE_NAME = config["TING_EN_IMAGE_NAME"]
WEBHOOK = config["WEBHOOK"]
SECRET = config["SECRET"]
IMAGE_DIR = os.path.join(os.path.dirname(__file__), config["IMAGE_DIR"])

# 初始化通知器
initialize_notifier(WEBHOOK, SECRET)

if __name__ == "__main__":
    while True:
        if is_time_to_run(RUN_TIME):
            log_info("Time to run the task. Starting new round...")
            learn_english(TING_EN_IMAGE_NAME, TING_EN_APP_PATH, IMAGE_DIR, DEBUG_MODE)
            log_info("Round completed.Waiting 45 minutes to ensure once an hour")
            time.sleep(60 * 45)  # 每 45 分钟检查一次,保证一小时内只运行一次
        else:
            log_info("Not time yet, waiting...")
            