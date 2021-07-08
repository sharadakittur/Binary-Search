lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def binary(lst, itm):
	nlst = []
	for x in range(0, len(lst) - 1, -1):
		nlst.append(x)
	exp = 1
	half = len(lst)/(2**exp)
	for y in range(half):
		if lst[y] == itm:
			return y
	del lst[0:round(len(lst)/2)]
	for z in range(half):
		print(z)
		if nlst[z] == itm:
			return z
	del nlst[0:round(len(lst)/2)]
	exp += 1
	
print(binary(lst, 3))
