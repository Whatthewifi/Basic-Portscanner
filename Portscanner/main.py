#imports

import socket


#scanning function

def scan(target, ports):
    print('\n' + 'starting scan for ' + str(target))
    for port in range (1,ports):
        scan_port(target,port)


#main function

def scan_port(ipaddress, port):
    # socket object
    # socket is an end point of communication between two devices
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] port open - " + str(port))
        sock.close()
    except:
        pass

        #edit: output looks sloppy and closed ports are of no interest
        #print("[-] port closed - " + str(port))

targets = input("[*] enter targets to scan (split by comma) ")
ports = int(input("[*] enter how many ports you want to scan: "))
if ',' in targets:
    print("[*] scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets,ports)