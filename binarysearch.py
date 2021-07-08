nov = input("How many items in the list?") #stands for number of values
lst = []
for x in r:
	val = input("What is a value?")
	lst.append(val)
item = input("What item are you looking for?")

def binary(lst, itm):
  nlst = []
  for x in lst:
    nlst.insert(0,x)
  exp = 1
  half = round(len(lst)/(2**exp))
  for y in range(0, half):
    if lst[y] == itm:
      print(y + 1)
  for z in range(0, half):
    if nlst[z] == itm:
      print(len(lst) - (z)) 
  del lst[0:round(len(lst)/2)]
  exp += 1

binary(lst,item)
