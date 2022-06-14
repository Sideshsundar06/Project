import random
a="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pas = int(input("enter a value for password to create:"))
p=" ".join(random.sample(a,pas))
print(p)

