#16
import random  
import string  
def specific_string(length):  
    sample_string = 'ABCDE' # define the specific string  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  


specific_string(8) # define the length  
specific_string(10)
specific_string(4)