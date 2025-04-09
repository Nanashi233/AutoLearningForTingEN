import time
import os
import yaml
from modules import learn_english, log_info, initialize_notifier, is_time_to_run, message_success

def create_default_config(config_path):
    """
    Create a default config.yaml file if it doesn't exist.
    """
    default_config = {
        "LOG_LEVEL": "INFO",
        "RUN_TIME": "9,14",
        "WAIT_TIME": 20,
        "TING_EN_APP_PATH": "C:\\Program Files (x86)\\ting_en\\ting_en.exe",
        "TING_EN_IMAGE_NAME": "ting_en.exe",
        "DING_TALK_BOT_WEBHOOK": "https://your.dingtalk.webhook.url",
        "DING_TALK_BOT_SECRET": "your_secret_key",
        "IMAGE_DIR": "src"
    }
    with open(config_path, "w", encoding="utf-8") as file:
        yaml.dump(default_config, file, default_flow_style=False, allow_unicode=True)
    print(f"Default config.yaml created at {config_path}")
    print("Please edit the config.yaml file with your settings and rerun the program.")
    os.system("pause")
    exit(0)  # Exit the program after creating the default config

def load_config():
    """
    Load the configuration from config.yaml.
    If the file doesn't exist, create a default one.
    """
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")
    if not os.path.exists(CONFIG_PATH):
        create_default_config(CONFIG_PATH)
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# Load configuration
config = load_config()
LOG_LEVEL = config["LOG_LEVEL"]
RUN_TIME = config["RUN_TIME"]
WAIT_TIME = config["WAIT_TIME"]
TING_EN_APP_PATH = config["TING_EN_APP_PATH"]
TING_EN_IMAGE_NAME = config["TING_EN_IMAGE_NAME"]
DING_TALK_BOT_WEBHOOK = config["DING_TALK_BOT_WEBHOOK"]
DING_TALK_BOT_SECRET = config["DING_TALK_BOT_SECRET"]
IMAGE_DIR = os.path.join(os.path.dirname(__file__), config["IMAGE_DIR"])

# Initialize notifier
initialize_notifier(DING_TALK_BOT_WEBHOOK, DING_TALK_BOT_SECRET, log_level=LOG_LEVEL)

if __name__ == "__main__":
    while True:

        if is_time_to_run(RUN_TIME) != True:
            log_info("Not time yet. Waiting 45 minutes to ensure once an hour")
            time.sleep(60 * 45)
            continue
        
        log_info("Time to run the task. Starting new round...")
        if learn_english(TING_EN_IMAGE_NAME, TING_EN_APP_PATH, IMAGE_DIR, wait_time = 60 * WAIT_TIME):
            message_success("Learning Task completed successfully! Date:%s"%time.strftime("%Y-%m-%d", time.localtime()))
            log_info("Round completed. Waiting 45 minutes to ensure once an hour")
            time.sleep(60 * 45)
            continue
        else:
            log_info("Learning Task failed. Waiting 45 minutes to ensure once an hour")
            time.sleep(60 * 45)
            continue