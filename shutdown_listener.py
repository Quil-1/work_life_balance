import socket
import os
import subprocess

WINDOWS_OS_SHUTDOWN_COMMAND = "shutdown /s /t 1"
WINDOWS_OS_LOGOUT_COMMAND = "shutdown -l"

def shutdown_listener():
    server_address = ('127.0.0.1', 5555)  # Socket server address (loopback IP and port)
    shutdown_signal = b'SHUTDOWN_NOW'  # Signal to initiate shutdown
    logoff_signal = b'LOGOFF_NOW'

    # Create a socket and bind it to the server address
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen(1)  # Listen for incoming connections

        print("Shutdown listener started...")
        while True:
            connection, client_address = server_socket.accept()

            try:
                print(f"Connection from {client_address}")
                data = connection.recv(1024)
                if data == logoff_signal:
                    print("Logoff signal received")
                    os.system(WINDOWS_OS_LOGOUT_COMMAND)
                elif data == shutdown_signal:
                    print("Shutdown signal received")
                    os.system(WINDOWS_OS_SHUTDOWN_COMMAND)
                else:
                    print("Invalid command received")
            except Exception as e:
                print(f"Error occurred: {e}")
            finally:
                connection.close()

if __name__ == "__main__":
    shutdown_listener()
