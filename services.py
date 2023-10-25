import os
from settings import(
    WINDOWS_OS_SHUTDOWN_COMMAND,
    WINDOWS_OS_LOGOUT_COMMAND
)
from datetime import(
    datetime, timezone
)

now = datetime.now(timezone.utc)

current_hour, current_minute, current_seconds = now.hour, now.minute, now.second

def windows_shutdown(hour: int, minute: int, seconds: int):
    """
    Shuts down a Windows computer at the specified time.

    Args:
        hour (int): UTC Hour in the day for the system to shutdown
        minute (int): UTC minute of the timestamp for the system to shutdown
        seconds (int): UTC seconds of the timestamp for the system to shutdown

    Returns:
        None

    Raises:
        None

    Examples:
        >>> windows_shutdown(12, 30, 0)
    """

    if (current_hour == hour) and (current_minute == minute):
        print("Time to shutdown")
    else:
        print("Keep working workaholic")

    # complete_shutdown_command = f" {WINDOWS_OS_SHUTDOWN_COMMAND} {time}"

    # # os.system(complete_shutdown_command)
    # os.system(WINDOWS_OS_LOGOUT_COMMAND)