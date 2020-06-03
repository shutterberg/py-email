#check conditions if entered email is a string if yes print the same using regex
import re
email=input()
list=re.findall('(?i)\S+@\S+.\S+',email) #\S+ --non space charcters #(?i) case sensitive removed
if(len(list)==1):
    print(list[0].lower())        #brings evrything to lowerCASE
else:
    print("Invalid email Id")
