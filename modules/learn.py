import pyautogui as pg
import time
import os
from .notifier import log_info, message_failed
from .app_manager import run_app, kill_app

def before_learning(app_image_name, app_path):
    '''
    启动应用
    '''
    try:
        kill_app(app_image_name)
    except Exception as e:
        log = (f"Unable to kill app @ STEP1: {e}")
        return False, log
    time.sleep(5)

    try:
        run_app(app_path)
    except Exception as e:
        log = (f"Unable to run app @ STEP1: {e}")
        return False, log
    time.sleep(20)

    log = (f"App started successfully @ STEP1")
    return True, log

def learning(image_dir, wait_time):
    '''
    模拟学习
    '''
    # 开始学习
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "stopped.png"), confidence=0.75)
        pg.click(site)
    except Exception as e:
        log = (f"Unable to click [PLAY] @ STEP2: {e}")
        return False, log

    # 学习过程
    time.sleep(wait_time)

    # 结束学习
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "played.png"), confidence=0.75)
        pg.click(site)
    except Exception as e:
        log = (f"Unable to click [STOP] @ STEP2: {e}")
        return False, log

    log = (f"Learning completed successfully @ STEP2")
    return True, log

def check_completion(image_dir):
    '''
    检查完成情况
    '''
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "vip.png"), confidence=0.75)
        pg.click(site)
        time.sleep(5)
    except Exception as e:
        log = (f"Unable to click [VIP] @ STEP3: {e}")
        return False, log

    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "daka.png"), confidence=0.75)
        pg.click(site)
        time.sleep(1)
    except Exception as e:
        log = (f"Unable to click [打卡] @ STEP3: {e}")
        return False, log

    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "pass.png"), confidence=0.75)
        log = (f"Learn English Success! Date: {time.strftime('%Y-%m-%d', time.localtime())}")
        return True, log
    except Exception as e:
        log = (f"Success not detected @ STEP3: {e}")
        return False, log

def after_learning(app_image_name):
    '''
    关闭应用
    '''
    time.sleep(5)
    try:
        kill_app(app_image_name)
    except Exception as e:
        log = (f"Unable to kill app @ STEP4: {e}")
        return False, log
    
    log = (f"App closed successfully @ STEP4")
    return True, log

def learn_english(app_image_name, app_path, image_dir, wait_time = 60 * 20):

    total_success = True

    success, log = before_learning(app_image_name, app_path)
    total_success = total_success and success
    if not success:
        message_failed(f"{log}")
    else:
        log_info(f"{log}")

    if total_success:
        success, log = learning(image_dir, wait_time)
        total_success = total_success and success
        if not success:
            message_failed(f"{log}")
        else:
            log_info(f"{log}")

    if  total_success:
        success, log = check_completion(image_dir)
        total_success = total_success and success
        if not success:
            message_failed(f"{log}")
        else:
            log_info(f"{log}")
    
    success, log = after_learning(app_image_name)
    total_success = total_success and success
    if not success:
        message_failed(f"{log}")
    else:
        log_info(f"{log}")

    if total_success:
        return True
    else:
        return False