# My script for the lab 
from netmiko import ConnectHandler
from getpass import getpass
import datetime

IP = input("Please enter the IP address: ")
USERNAME = input("Please enter your username: ")
PASSWORD = getpass("Please enter your password: ")

Device = {
    #'ip': "192.168.182.130",
    'ip': IP,
    'username': USERNAME,
    'password': PASSWORD,
    'device_type': 'cisco_ios'
   
}

Connect = ConnectHandler(**Device)
output = Connect.send_command('show run')
File = open('Output.conf', 'x')
File.write(output)

Date = datetime.date.today()
File = open('Output.conf', 'a')
File.write(str(Date))

File = open('Output.conf', 'a')
File.write("\n")

