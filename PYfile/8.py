#8
l = []
l.append("24")
l.append("41")
l.append("49")
l.append("50")
l.append("54")
l.append("Sai teja")
l.append("Sabarinath")
l.append("Shyam")
l.append("Sidesh")
l.append("Jayakrishna")
l.append("2")
print("List: ",l)
print("\nPoping element at index 0:\n",l)
l.pop(0)
print("\nAgain poping element at index 0:\n",l)
l.pop(0)
print("\nAgain poping element at index 0:\n",l)
l.pop(0)
print("\nThe list after removing elements is:\n ")
print(l)
print("\nReverse of the string is:\n",l[::-1])
l1 = [24,41,49,50,54]
l2 = ["SAI","SABARI","SHYAM","SIDESH","JAYAKRISHNA"]
l3 = l1+l2
l4 = zip(l1,l2)
zipped_list = list(l4) 
print("\nThe final appended list\n",l3)
print("\nConcating using zip() function\n",zipped_list)
print("\nPrinting the first 6 elements from the final list:\n",l3[0:6])