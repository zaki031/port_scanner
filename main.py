import socket


target_ip = 'python.org'
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)  # set a timeout for the connection attempt

    # Attempt to connect to the target IP address and port
result = s.connect_ex((target_ip, port))
if result == 0: print(port, "is open !")
else: print(port, "is closed !")