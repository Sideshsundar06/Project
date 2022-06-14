#11
def unique(list1):
  unique_list = []
  for x in list1:
    if x not in unique_list:
      unique_list.append(x)
  for x in unique_list:
    print(x),
list1 = [1,6,9,4,2,0,2,6,6,7,9]
print("the unique values from first list are: ")
unique(list1)

s1=[1,6,9,4,2,0,2,6,6,7,9]
print(set(s1))
s2=set()
s2.add(11)
print(s2)
s2.update(s1)
print(s2)
