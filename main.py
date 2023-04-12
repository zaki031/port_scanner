import socket

type = input("type 1 if you want to check a single port, type 2 if you want to check a range of ports : ")

if type =="1":
    target_ip = input("enter the IP you want to check : ")
    port = int(input("enter the port your want to check : "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    result = s.connect_ex((target_ip, port))
    if result == 0: print(port, "is open !")
    else: print(port, "is closed !")


if type == "2":
    target_ip = input("enter the IP you want to check : ")
    port = input("enter the ports range you want to check (exemple :  0-500): ").split("-")
    for i in range(int(port[0]),int(port[1])+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, i))
        if result == 0: print(i, "is open !")
        else: print(i, "is closed !")
        




    
