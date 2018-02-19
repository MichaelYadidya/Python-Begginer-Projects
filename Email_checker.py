#!/usr/bin/env/python

def email_checker(username,password):
    import imaplib,re
    i = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        i.login(username,password)

        x,y = i.status('INBOX','(MESSAGES UNSEEN)')

        messages = int(re.search('MESSAGES\s+(\d)' , y[0]).group(1))
        unseen = int(re.search('UNSEEN\s+(\d)' ,y[0]).group(1))
        return(messages,unseen)
    except:
        return False,0
messages,unseen = email_checker('michaelyadidya@gmail.com' , 'jesusmicheal21')
print ('%i messages, %i unseen' % (messages,unseen))
