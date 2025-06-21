import datetime
from .notifier import message_failed

def parse_schedule(schedule):
    """
    解析计划字符串。
    :param schedule: str，计划字符串（如 "0,6,12,18"）
    :return: list，包含有效小时数的列表
    """
    try:
        return [int(hour.strip()) for hour in schedule.split(",")]
    except ValueError:
        raise ValueError("计划格式错误，必须为逗号分隔的整数列表")

def match_schedule(hours, current_time):
    """
    检查当前小时是否匹配计划。
    :param hours: list，有效小时数列表
    :param current_time: datetime.datetime，当前时间
    :return: bool，是否匹配
    """
    return current_time.hour in hours

def is_time_to_run(schedule):
    """
    检查当前时间是否符合计划。
    :param schedule: str，计划字符串（如 "0,6,12,18"）
    :return: bool，若到达计划时间返回True，否则返回False
    """
    try:
        hours = parse_schedule(schedule)
        current_time = datetime.datetime.now()
        return match_schedule(hours, current_time)
    except Exception as e:
        message_failed(f"解析或匹配计划时出错: {e}")
        return False
