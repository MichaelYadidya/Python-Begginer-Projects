from threading import *
from ipwhois import IPWhois 
from pprint import pprint
import socket

class ip_lookup():
    def __init__(self):

        print('Welcome to IP Scanner: ')
        target = input('Enter the IP which you want to scan: ')
        ip = IPWhois(target)
        resolve = IPWhois.lookup_whois(ip)
        pprint(resolve)

def ip_port():
    

    print('Welcome to IP port Scanner: ')
    target = input('Enter the IP which you want to scan: ')
    from_port = (input('Enter the port from which you want to start the scan: '))
    end_port = (input('Enter the port at which you want to stop the scan at: '))
    open_port = []
    closed_port = []
    threads = []

    def scan(port):

        s = socket.socket()
        result = s.connect_ex((target,port))
        print('Working on Port: '+ (port))

        if result ==0:
            open_port.append(port)
            s.close()
        else:
            closed_port.append(port)
            s.close()
    for i in (open_port,closed_port.append(1)):

        t = Thread(target = scan , args = (i,))
        threads.append(t)
        t.start()

        [x.join() for x in threads]

        print(open_port)


def main():
    print('Welcome to All-in-One Ip tool')
    user_input = (input('Enter the Desired Option: '))

    if user_input == '1':
        return ip_lookup()
    elif user_input == '2':
        return ip_port()

    return;

main()
