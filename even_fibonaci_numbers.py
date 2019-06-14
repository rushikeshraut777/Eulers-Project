limit=4000000

list=[1,2,3]

# since we have kept 2 in the initial list
sum=2

while(True):
	next_elem=list[-1]+list[-2]
	list.append(next_elem)

	if next_elem < limit:
		if next_elem %2==0:
			sum+=next_elem
	else:
		break


print(sum)
