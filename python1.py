x=int(input("enter the integer" ))
fact=1
#checking it is odd or even
if x%2==1:
    #if it is odd doing factorial
    for i in range(1,x+1):
        fact=fact*i
    print(fact)
else:
    #else checking it is palindrom or not
    c=str(x)
    if c[::-1]== str(x):
        print("it is palindrom")
    else:
        print("it is not palindrom")
