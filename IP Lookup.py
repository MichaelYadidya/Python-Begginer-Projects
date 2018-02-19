from ipwhois import IPWhois
from pprint import pprint

target = input('Enter the Ip to start the search: ')

ip = IPWhois(target)
resolve = ip.lookup_whois(ip)

pprint(resolve)
