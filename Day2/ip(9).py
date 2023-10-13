import re

def check_ip_address(ip):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$'
    
    if re.match(pattern, ip):
        return True
    else:
        return False
    
ip_address = input("Enter an IP address: ")

if check_ip_address(ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"{ip_address} is not a valid IP address.")

#Output
'''
Enter an IP address: 192.168.123.132
192.168.123.132 is a valid IPv4 address.
'''