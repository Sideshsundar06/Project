def check(S1,S2):
    count = 0
    A = len(S1)
    B = len(S2)
    if (A==B):
        print("The length of S1 and S2 are equal.")
    else:
        print("The length of S1 and S2 are not equal.")
    for i in range(A):
        if (S1[i]==S2[i]):
               count = count + 1
        if (A>B):
            C = count / A
        else:
            C = count / B   
    if(C*100>=90):
        print("S1 is " , S1)
        print("S2 is " , S2)
        print("S1 and S2 are identical.")
    elif(89>=C*100>=60):
        print("S1 is " , S1)
        print("S2 is " , S2)
        print("S1 and S2 are similar.")
    else:
        print("S1 is " , S1)
        print("S2 is " , S2)
        print("S1 and S2 are not identical.")

#1     
S1 = "ATTCGG"
S2 = "ATTCGG"
check(S1,S2)
#2
S1 = "ATTCGC"
S2 = "ATTCGG"
check(S1,S2) 
#3
S1 ="ATGC"
S2 ="ATGCC"
check(S1,S2) 
