a=list(map(int,input("enter the value for list").split()))
#checking if it is in descending order
count=1
count2=1
for i in range(len(a)):
    if (i+1)!=len(a):
        if a[i]>a[i+1]:
            count+=1
        if a[i]<a[i+1]: 
            count2+=1
if len(a)==count:
    print("it is in descending order")
elif len(a)==count2:
    print("it is in ascending order")
else:
    print("it is mixed list")
    
