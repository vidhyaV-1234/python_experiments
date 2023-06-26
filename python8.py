x={}
y=int(input("no.of values to be entered"))
for i in range(y):
    k=input("enter the key")
    v=input("enter the value")
    x[k]=v
print("dictionary elements are :")
for k,v in x.items():
    print(k,v)
    
