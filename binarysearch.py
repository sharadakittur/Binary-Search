nov = input("How many items in the list?") #stands for number of values
lst = []
for x in range(int(nov)):
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
      return y
  for z in range(0, half):
    if nlst[z] == itm:
      return len(lst) - (z + 1) 
  del lst[0:round(len(lst)/2)]
  exp += 1

answer = binary(lst,item)
if answer == None:
  print("The item is not there in the list.")
else:
  print(answer)
