#!/usr/bin/python3
import os,sys

#Testing out command
#os.system("echo Hello world brought to you by command line.")

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])



print(

"""


=================================================================

 ===========
|           |
|           |                            
|===========                            
|\         ---    ----   ----    ---    
| \       |   |  |      |       |   |   
|  \      ----   |      |       ----    
|   \     |      |      |       |       
|    \     ----   ----   ----    ----    

"""

)
print("Because no-one ever spells reconesance properly" )
print(strike("test"))
print("=================================================================")

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <IP> ")
    sys.exit()

ip=sys.argv[1]

start = True 

#NMAP scan

def nmap(ip):
    global start
    os.system("mkdir scans")
    os.system("mkdir scans/nmap")
    os.system(f"mkdir scans/nmap/{ip}")
    print(f"Running NMAP stealth scan on {ip} ")
    os.system(f"sudo nmap -sS -p- -Pn -vvv --script default,vuln -sV -oA scans/nmap/{ip}/tcp {ip}")
    print(f"Creating a textfile with a list of open TCP Ports")
    os.system(f"cat scans/nmap/{ip}/tcp.nmap | grep tcp | grep open | cut -f 1 -d '/' >> scans/opentcpports.txt ")
    while start == True:
        response = input("Do you also want to do UDP scanning (top 1024)? Y/N  ").lower()
        if response == "y":
            print(f"Running UDP scan on {ip} ")
            os.system(f"sudo nmap -sU -vvv --top-ports=1024 -oA scans/nmap/{ip}/udp --script default,vuln -Pn {ip}"  )
            sys.exit()
        elif response == "n":
            start = False
            sys.exit()
        else:
            print("Please enter a valid input Y or N")

#Nikto scan
def nikto(ip):
    os.system("mkdir scans/nikto")

nmap(ip)
