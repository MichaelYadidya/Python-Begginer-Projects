
# coding: utf-8

# In[ ]:


from threading import *
import socket

host = input('Host :')
from_port = int(input('Start Port Scan From :'))
to_port = int(input('End Port Scan At : '))
counting_open = []
counting_close = []
threads = []

def scan(port):
    
    s = socket.socket()
    result = s.connect_ex((host,port))
    print('Working on Port:' + (str(port)))
    
    if result == 0:
        counting_open.append(port)
        
        s.close()
    else:
        counting_close.append(port)
        
        s.close()
        
for i in range (from_port,to_port+1):
    t= Thread(target=scan ,args=(i,))
    threads.append(t)
    t.start()
    
[x.join() for x in threads]

print(counting_open)

