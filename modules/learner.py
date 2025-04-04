import pyautogui as pg
import time
import os
from .notifier import log_info, log_error, message_success, message_failed

def learn_english(image_dir):
    # 开始学习
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "stopped.png"), confidence=0.75)
        log_info(f"Clicked [PLAY] at {site}")
        pg.click(site)
    except Exception as e:
        log_error(f"Unable to click [PLAY]: {e}")
        message_failed("Unable to click [PLAY]")
        return

    # 学习过程
    log_info("Learning in progress for 20 minutes...")
    time.sleep(60 * 20)

    # 结束学习
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "played.png"), confidence=0.75)
        log_info(f"Clicked [STOP] at {site}")
        pg.click(site)
    except Exception as e:
        log_error(f"Unable to click [STOP]: {e}")
        message_failed("Unable to click [STOP]")
        return

    # 检查完成情况
    log_info("Checking completion status...")
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "vip.png"), confidence=0.75)
        log_info(f"Clicked [VIP] at {site}")
        pg.click(site)
        time.sleep(5)
        try:
            site = pg.locateCenterOnScreen(os.path.join(image_dir, "daka.png"), confidence=0.75)
            log_info(f"Clicked [打卡] at {site}")
            pg.click(site)
            time.sleep(1)
            try:
                site = pg.locateCenterOnScreen(os.path.join(image_dir, "pass.png"), confidence=0.75)
                log_info(f"Success detected at {site}")
                message_success(f"打卡成功！Date: {time.strftime('%Y-%m-%d', time.localtime())}")
            except Exception as e:
                log_error(f"Success not detected: {e}")
                message_failed("Success not detected")
        except Exception as e:
            log_error(f"Unable to click [打卡]: {e}")
            message_failed("Unable to click [打卡]")
    except Exception as e:
        log_error(f"Unable to click [VIP]: {e}")
        message_failed("Unable to click [VIP]")