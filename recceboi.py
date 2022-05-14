#!/usr/bin/python3
import os,sys

#Testing out command
#os.system("echo Hello world brought to you by command line.")

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <IP> ")
    sys.exit()

ip=sys.argv[1]

#NMAP scan

def nmap(ip):
    os.system("mkdir nmap")
    os.system(f"nmap -p- -Pn -vvv --script default,vuln -sV -oA nmap/tcp {ip}")
print(f"Running scripted nmap on {ip}")

print(str(len(sys.argv)))

nmap(ip)
