#17
import random  
import string  
def specific_string(length):  
    sample_string = 'ABCDE' # define the specific string  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    print(" Randomly generated string is: ", result)  
    
    str = result
  
    # declaring an empty string variable for storing modified string
    modified_str = ''
  
    for char in range(0, len(str)):
        if(str[char] == 'B'):
            modified_str += 'Z'
        else:
            modified_str += str[char]
            
    print("Modified string : ",modified_str)

specific_string(8) 
specific_string(10)
specific_string(4)
