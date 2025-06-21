import pyautogui as pg
import time
import os
from .notifier import log_info, message_failed
from .app_manager import run_app, kill_app

def before_learning(app_image_name, app_path):
    """
    启动应用程序。

    :param app_image_name: str，应用程序进程名
    :param app_path: str，应用程序路径
    :return: (bool, str)，是否成功及日志信息
    """
    try:
        kill_app(app_image_name)
    except Exception as e:
        log = (f"无法关闭应用 @ 步骤1: {e}")
        return False, log
    time.sleep(5)

    try:
        run_app(app_path)
    except Exception as e:
        log = (f"无法启动应用 @ 步骤1: {e}")
        return False, log
    time.sleep(20)

    log = (f"应用启动成功 @ 步骤1")
    return True, log

def learning(image_dir, wait_time):
    """
    模拟学习过程。

    :param image_dir: str，图片目录
    :param wait_time: int，学习等待时间（秒）
    :return: (bool, str)，是否成功及日志信息
    """
    # 开始学习
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "stopped.png"), confidence=0.75)
        pg.click(site)
    except Exception as e:
        log = (f"无法点击【播放】 @ 步骤2: {e}")
        return False, log

    # 学习过程
    time.sleep(wait_time)

    # 结束学习
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "played.png"), confidence=0.75)
        pg.click(site)
    except Exception as e:
        log = (f"无法点击【停止】 @ 步骤2: {e}")
        return False, log

    log = (f"学习过程顺利完成 @ 步骤2")
    return True, log

def check_completion(image_dir):
    """
    检查学习是否完成。

    :param image_dir: str，图片目录
    :return: (bool, str)，是否成功及日志信息
    """
    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "vip.png"), confidence=0.75)
        pg.click(site)
        time.sleep(5)
    except Exception as e:
        log = (f"无法点击【VIP】 @ 步骤3: {e}")
        return False, log

    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "daka.png"), confidence=0.75)
        pg.click(site)
        time.sleep(1)
    except Exception as e:
        log = (f"无法点击【打卡】 @ 步骤3: {e}")
        return False, log

    try:
        site = pg.locateCenterOnScreen(os.path.join(image_dir, "pass.png"), confidence=0.75)
        log = (f"学习成功！日期：{time.strftime('%Y-%m-%d', time.localtime())}")
        return True, log
    except Exception as e:
        log = (f"未检测到成功标志 @ 步骤3: {e}")
        return False, log

def after_learning(app_image_name):
    """
    关闭应用程序。

    :param app_image_name: str，应用程序进程名
    :return: (bool, str)，是否成功及日志信息
    """
    time.sleep(5)
    try:
        kill_app(app_image_name)
    except Exception as e:
        log = (f"无法关闭应用 @ 步骤4: {e}")
        return False, log
    
    log = (f"应用已成功关闭 @ 步骤4")
    return True, log

def learn_english(app_image_name, app_path, image_dir, wait_time = 60 * 20):
    """
    自动化完整英语学习流程。

    :param app_image_name: str，应用程序进程名
    :param app_path: str，应用程序路径
    :param image_dir: str，图片目录
    :param wait_time: int，学习等待时间（秒），默认20分钟
    :return: bool，是否全部流程成功
    """
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

    if total_success:
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

    return total_success