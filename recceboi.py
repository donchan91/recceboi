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
    print("Running NMAP stealth scan")
    os.system(f"sudo nmap -sS -p- -Pn -vvv --script default,vuln -sV -oA nmap/tcp {ip}")
    print("Do you also want to do UDP scanning? Y/N")
    response = input("Do you also want to do UDP scanning (top 1024)? Y/N  ").lower()
    if response == "y":
        os.system(f"sudo nmap -sU -vvv --top-ports=1024 -oA nmap/udp --script default,vuln -Pn {ip}"  )
print(f"Running scripted nmap on {ip}")

print(str(len(sys.argv)))

nmap(ip)
