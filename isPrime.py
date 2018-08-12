def get_number():
	return int(input('Give me a number: '))

def isPrime():
	num = get_number()
	listRange = list(range(1,num+1))

	divisorList = []

	for number in listRange:
		if num%number == 0:
			divisorList.append(number)
	
	if len(divisorList)==1 or len(divisorList)==2: 
		print('It is a prime number!')
	else:
		print('It is not a prime number!')

isPrime()
