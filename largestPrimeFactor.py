# this has very high time complexity.
# need to think of some better solution

def is_prime(input):
	is_prime = True
	for i in range(2,input):
		if input % i == 0:
			is_prime=False
			break
	return is_prime


user_input = 600851475143

largest_prime = 1

for i in reversed(range(1,int(user_input/2))):
	print("iter>>{}".format(i))
	if user_input%i==0:
		print("div>>{}".format(i))
		if is_prime(i):
			print("prime>>".format(i))
			largest_prime=i
			break

print(largest_prime)