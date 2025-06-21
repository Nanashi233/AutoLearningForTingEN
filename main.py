import time
import os
from modules.learn import learn_english
from modules.notifier import initialize_notifier, log_info, message_success
from modules.timed_task import is_time_to_run
from modules.config import get_config

# 获取配置
LOG_LEVEL = get_config("LOG_LEVEL")
RUN_TIME = get_config("RUN_TIME")
WAIT_TIME = get_config("WAIT_TIME")
TING_EN_APP_PATH = get_config("TING_EN_APP_PATH")
TING_EN_IMAGE_NAME = get_config("TING_EN_IMAGE_NAME")
DING_TALK_BOT_WEBHOOK = get_config("DING_TALK_BOT_WEBHOOK")
DING_TALK_BOT_SECRET = get_config("DING_TALK_BOT_SECRET")
IMAGE_DIR = os.path.join(os.path.dirname(__file__), get_config("IMAGE_DIR"))

# 初始化通知器
initialize_notifier(DING_TALK_BOT_WEBHOOK, DING_TALK_BOT_SECRET, log_level=LOG_LEVEL)

# 主程序
if __name__ == "__main__":
    while True:
        if not is_time_to_run(RUN_TIME):
            log_info("未到设定时间，等待45分钟后再次检查。")
            time.sleep(60 * 45)
            continue
        
        log_info("到达设定时间，开始新一轮任务...")
        if learn_english(TING_EN_IMAGE_NAME, TING_EN_APP_PATH, IMAGE_DIR, wait_time=60 * WAIT_TIME):
            message_success("学习任务已成功完成！日期：%s" % time.strftime("%Y-%m-%d", time.localtime()))
            log_info("本轮任务完成，等待45分钟后再次执行。")
            time.sleep(60 * 45)
            continue
        else:
            log_info("学习任务失败，等待45分钟后重试。")
            time.sleep(60 * 45)
            continue