#creating a function to check whether a number is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
a=int(input("enter the value"))
evenOdd(a)
