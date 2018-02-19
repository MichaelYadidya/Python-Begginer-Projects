from ipwhois import *
from pprint import pprint

target = input('Enter the IP you wish to scan: ')
ip = IPWhois(target)
resolve = ip.lookup_whois(ip)
resolved = resolve
print('The Ip is from ',resolved['asn_country_code'])
print('Fetching details of the IP: \n')
print(resolved['nets'][0]['address'])

