#19
def grtst(n1,n2,n3,n4):
    a = n1
    b = n2
    c = n3
    d = n4
    max1 = max(a,b)
    max2 = max(c,d)
    maxf = max(max1,max2)
    print("\nThe greatest of the four numbers is ",maxf)

print("Enter four numbers which are to be compared")
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))
n4 = int(input("Enter a number: "))
grtst(n1,n2,n3,n4)
