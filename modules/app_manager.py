import os
from .notifier import log_info

def run_app(app_path):
    log_info("Starting APP...")
    os.startfile(app_path)

def kill_app(app_image_name):
    log_info("Killing APP...")
    os.system(f"taskkill /f /t /im {app_image_name}")