
# coding: utf-8

# In[4]:


import os,time,platform,winsound


def sound():
    
    for i in range (2):   # No. of Replays
        
        for j in range (5):  # No.of times to play
            
            winsound.MessageBeep(-1)  # Sound Plays
            
            time.sleep(2)   # Interval between Sound
            
            
def alarm(n):
    
    print()
    
    print('wait_time:',n,'seconds')
    
    time.sleep(n)
    
    sound()
    
    
def input_destinations(user_input):
    
    if user_input == '1':
        
        user_input = int(input('Enter the time:'))
        
        wait_time = (user_input*60)*60
        
        alarm(wait_time)
        
    elif user_input == '2':
        
        user_input = int(input('Enter the time:'))
        
        wait_time = (user_input)*60
        
        alarm(wait_time)
        
    elif user_input == '3':
        
        user_input = int(input('Enter the time:'))
        
        wait_time = (user_input)
        
        alarm(wait_time)
        
    elif user_input == '4':
        
        hours = int(input('hours:'))
        
        minutes = int(input('minutes:'))
        
        seconds = int(input('seconds:'))
        
        wait_time = (hours*60)*60 + minutes * 60 + seconds
        
        alarm(wait_time)
        
    else:
        
        try:
            
            os.system('cls')
            main()
        
        except:
            
            os.system('clear')
            main()
            
def main():
    
    print('Choose the preferred option \n 1) Hours \n 2) Minutes \n 3) Seconds \n 4) Mixed ')
    
    main_input = input(' : ')
    
    input_destinations(main_input)
    
    return;


main()
        
        

            
            
            
            
         
            
            


# In[2]:


import os,time,platform,winsound

