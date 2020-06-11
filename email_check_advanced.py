
#check conditions if entered email is a string if yes print the same using regex
import re
email=input()
list=re.findall('^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$',email) 
if(len(list)==1):
    print(list[0].lower())        #brings evrything to lowerCASE
else:
    print("Invalid email Id")      #error_message