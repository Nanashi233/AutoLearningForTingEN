import datetime
from .notifier import message_failed

def parse_schedule(schedule):
    """
    Parse a schedule string.
    :param schedule: str, schedule string (e.g., "0,6,12,18")
    :return: list, containing valid hour values
    """
    try:
        return [int(hour.strip()) for hour in schedule.split(",")]
    except ValueError:
        raise ValueError("Invalid schedule format, must be a comma-separated list of integers")

def match_schedule(hours, current_time):
    """
    Check if the current hour matches the schedule.
    :param hours: list, valid hour values
    :param current_time: datetime.datetime, current time
    :return: bool, whether it matches
    """
    return current_time.hour in hours

def is_time_to_run(schedule):
    """
    Check if the current time matches the schedule.
    :param schedule: str, schedule string (e.g., "0,6,12,18")
    :return: bool, True if it's time to run, False otherwise
    """
    try:
        hours = parse_schedule(schedule)
        current_time = datetime.datetime.now()
        return match_schedule(hours, current_time)
    except Exception as e:
        message_failed(f"Error parsing or matching schedule: {e}")
        return False

# Example usage
if __name__ == "__main__":
    schedule = "0,6,12,18"  # Trigger at 0:00, 6:00, 12:00, and 18:00
    if is_time_to_run(schedule):
        print("It's time!")
    else:
        print("Not yet time.")