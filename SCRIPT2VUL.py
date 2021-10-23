#!/bin/python3
#make install pip install python
import nmap
import os
import sys
from termcolor import colored, cprint
sc = nmap.PortScanner()



print(r"""______   __  _____ _   _ _____ _____ _______   __
| ___ \ \ / / |  __ \ | | |  _  /  ___|_   _\ \ / /
| |_/ /\ V /  | |  \/ |_| | | | \ `--.  | |  \ V / 
| ___ \ \ /   | | __|  _  | | | |`--. \ | |  /   \ 
| |_/ / | |   | |_\ \ | | \ \_/ /\__/ / | | / /^\ \
\____/  \_/    \____|_| |_/\___/\____/  \_/ \/   \/
                                                   
                                                     """)


response = input("""\nEnter type of scan
            1)SYN ACK
            2)OS DETECTION\n""")

print("You have selected options :", response)

def main():
    n = input("1- Network scanner\n2- Vulnerabilities Detection \nPlease enter a number : ")
    
    if n == '1':
       nmap()
    if n == '2':
       vuln()
    else :
       print("Choose enter number 1 or 2")
    

def nmap():
    text = colored('###############SCAN VULN###################', 'red', attrs=['reverse', 'blink'])
    print(text) 
    ip = input("\nEnter IP : ")
    sc = nmap.PortScanner()
    scan_range = sc.scan(hosts="localhost/24") #insert your range
    print(scan_range['scan'])

def vuln():
    text = colored('*********Vulnerability Scanner*************', 'red', attrs=['reverse', 'blink'])
    print(text)
    ip = input("*\nEnter adress: ") 
    print(os.system('nmap -sV --script=vulners.nse ' +ip))


if __name__ == "__main__":
    main()









