import logging
from dingtalkchatbot.chatbot import DingtalkChatbot

bot = None

def initialize_notifier(webhook, secret, log_level="INFO"):
    """
    初始化钉钉通知机器人，并设置日志级别。

    :param webhook: str，钉钉机器人Webhook地址
    :param secret: str，钉钉机器人安全密钥
    :param log_level: str，日志级别（如"INFO"、"DEBUG"等）
    """
    global bot
    bot = DingtalkChatbot(webhook, secret=secret)

    # 将日志级别字符串转换为 logging 模块的日志级别
    numeric_log_level = getattr(logging, log_level.upper(), logging.INFO)
    logging.getLogger().setLevel(numeric_log_level)

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 默认日志级别为 INFO
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("TingEN.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# def log_debug(message):
#     """记录 DEBUG 级别日志"""
#     logging.debug(message)

def log_info(message):
    """
    记录 INFO 级别日志。

    :param message: str，日志内容
    """
    logging.info(message)

# def log_warning(message):
#     """记录 WARNING 级别日志"""
#     logging.warning(message)

def log_error(message):
    """
    记录 ERROR 级别日志。

    :param message: str，日志内容
    """
    logging.error(message)

# def log_critical(message):
#     """记录 CRITICAL 级别日志"""
#     logging.critical(message)

def message_success(message):
    """
    发送成功消息到钉钉，并记录日志。

    :param message: str，发送的消息内容
    """
    logging.info(f"{message}, sending message")
    bot.send_text(msg=message, is_at_all=False)

def message_failed(message):
    """
    发送失败消息到钉钉，并记录日志。

    :param message: str，发送的消息内容
    """
    logging.error(f"{message}, sending message")
    bot.send_text(msg=message, is_at_all=True)