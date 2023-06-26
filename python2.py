def print_string(str1,str2):
    i=len(str1)
    j=len(str2)
    c=[]
 #checking whether the second string can be obtained from the first    
    while i>0 and j>0:
        if i==j:
            c.append(i) 
            j-=1
        i-=1
    if len(str2)==len(c):
         return 1
    else:
         return 0
str1=input("enter the string")
str2=input("enter the string2")
if(print_string(str1,str2)):
    print("yes")
else:
    print("no")
        
