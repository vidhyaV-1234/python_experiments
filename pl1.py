#list-index (positive and negative)
a=list(map(int,input().split()))
n=int(input("enter the element wants to be searched"))
d=a.index(n)
print(d)
print((d)-len(a))


