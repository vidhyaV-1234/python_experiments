#to check one set is subset of another set
x=set(input().split())
y=set(input().split())
#to check x is a subset of y
if x.issubset(y):
    print("x is a subset of y")
#to check y is a subset of x    
elif y.issubset(x):
    print("y is a subset of x")
else:
    print("different sets")
