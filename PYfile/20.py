from turtle import clear


#20
def prod(n1,n2,n3):
    a = n1
    b = n2
    c = n3
    res = a*b*c
    print("The product is: ",res)

print("Enter three numbers to find its product")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
prod(n1,n2,n3)