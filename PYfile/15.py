#15
import random
l = 10*[""]
print("Generating 10 random numbers between 1 and 1000")
for i in range(0,10):
    val = random.randrange(1,1000)
    l[i] = val
print("Random list generated: ",l)
print("Minimum value in the list generated is ",min(l))
print("Maximum value in the list generated is ",max(l))
