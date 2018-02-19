
# coding: utf-8

# In[15]:


def calculator(a,b,op):
    
    
    if op not in  '+/*-':
        
        print ("Please select a valid operand")
    
    if op == '+':
        
        return ('a' + '' + op +'' + 'b' +'' + '=' + str(a+b))
    
    if op == '-':
        
        return ('a' + '' + op + '' + 'b' + '' + '=' + str(a-b))
    
    if op == '/':
        
        return ('a' + '' + op + '' + b + '' + '=' + str(a/b))
    
    if op == '*':
        
        return ('a' + '' + op + '' + 'b' + '' + '=' + str(a*b))
    
    
    
def main():
    
    a = int(input('First Number: '))
    
    b = int(input('Second Number: '))
    
    op = input('Choose the operand : + - / * ')
    
    print(calculator(a,b,op))
    
    return;

main()
    
    

