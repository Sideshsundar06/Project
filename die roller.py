import random
import time

def castdie():


    print('rolling.....')
    time.sleep(1)
    print('rolling.....')
    time.sleep(1)
    print('rolling.....')
    time.sleep(1)
    print('rolling.....')
    time.sleep(1)
    r=list(range(1,7))
    print("result" + str(random.choice(r))) 

while True:
    time.sleep(2)
    x=input("Press enter to roll the die")
    if x=="exit":
        break
    else:
        castdie()
        
