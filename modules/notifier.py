import logging
from dingtalkchatbot.chatbot import DingtalkChatbot

bot = None

def initialize_notifier(webhook, secret):
    """初始化通知器"""
    global bot
    bot = DingtalkChatbot(webhook, secret=secret)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("TingEN.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def log_info(message):
    """记录 INFO 级别日志"""
    logging.info(message)

def log_error(message):
    """记录 ERROR 级别日志"""
    logging.error(message)

def message_success(message):
    """发送成功消息"""
    log_info(f"Sending success message: {message}")
    bot.send_text(msg=message, is_at_all=False)

def message_failed(message):
    """发送失败消息"""
    log_error(f"Sending failure message: {message}")
    bot.send_text(msg=message, is_at_all=True)