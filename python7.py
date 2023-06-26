x=set(input().split())
y=set(input().split())
if x.issubset(y):
    print("x is a subset of y")
elif y.issubset(x):
    print("y is a subset of x")
else:
    print("different sets")
