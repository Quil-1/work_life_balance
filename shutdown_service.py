import win32serviceutil
import win32service
import win32event
import os
import time
import socket
from datetime import datetime

WINDOWS_OS_LOGOUT_COMMAND = "shutdown -l"
CLOSING_HOUR = 17
CLOSING_MINUTE = 0

class FileCreationService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'auto_closing_time'
    _svc_display_name_ = 'Auto Closing Time'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_running = True
        self.shutdown_signal = b'SHUTDOWN_NOW'
        self.logoff_signal = b'LOGOFF_NOW'
        self.set_closing_time_signal = b'SET_CLOSING_TIME'
        self.helper_address = ('127.0.0.1', 5555)  # Helper application address

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def send_shutdown_request(self):
        # Send shutdown request to helper application via socket
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect(self.helper_address)
                client_socket.send(self.shutdown_signal)
                client_socket.close()
        except Exception as e:
            with open("error_log.txt", "a") as error_file:
                error_file.write(f"Error occurred: {e}\n")

    def SvcDoRun(self):  
        while self.is_running:
            current_time = datetime.now().time()
            date_time = datetime.now().isoformat()

            # Check if it is office closing time 
            if current_time.hour == CLOSING_HOUR and current_time.minute == CLOSING_MINUTE:
                with open("time.txt", "a") as file:
                    file.write(f"Closing Dates and Closing Time : {date_time} \n")
                    self.send_shutdown_request()  # Send request to initiate shutdown

            time.sleep(10)  # Sleep for 10 seconds before checking again


if __name__ == '__main__':
    # Install the service
    win32serviceutil.HandleCommandLine(FileCreationService)
