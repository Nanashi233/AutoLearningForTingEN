import pyautogui as pg
import time
import os
from .notifier import log_info, log_error, message_success, message_failed
from .app_manager import run_app, kill_app

def learn_english(app_image_name,app_path,image_dir,debug_mode):

    # 启动应用
    kill_app(app_image_name)
    time.sleep(20)
    run_app(app_path)
    time.sleep(20)

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
    if debug_mode:
        log_info("Debug mode is on, short sleep for 10 second.")
        time.sleep(10)
    else:
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

    # 关闭应用
    time.sleep(20)
    kill_app(app_image_name)