import sys
from settings import(
    LINUX_OS, WINDOWS_OS, MAC_OS
)

from services import(
    windows_shutdown
)

def shutdown_pc(hour: int, minute: int, seconds: int) -> None:
    """
    Shuts down the computer

    Args:
        hour (int): UTC Hour in the day for the system to shutdown
        minute (int): UTC minute of the timestamp for the system to shutdown
        seconds (int): UTC seconds of the timestamp for the system to shutdown

    Returns:
        None

    Raises:
        None
    """

    if sys.platform.startswith(WINDOWS_OS):
        windows_shutdown(hour, minute, seconds)


if __name__ == "__main__":
    hour = 0
    minute = 9
    seconds = 0 
    shutdown_pc(hour, minute, seconds)