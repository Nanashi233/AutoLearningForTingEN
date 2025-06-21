import os
from .notifier import log_info

def run_app(app_path):
    """
    启动指定路径的应用程序。

    :param app_path: str，应用程序的完整路径
    """
    os.startfile(app_path)

def kill_app(app_image_name):
    """
    通过进程名强制关闭应用程序。

    :param app_image_name: str，应用程序进程名（如 ting_en.exe）
    """
    os.system(f"taskkill /f /t /im {app_image_name}")
