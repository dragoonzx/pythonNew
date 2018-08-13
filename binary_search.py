def binary_search():
	listOf = list(map(int, input().split()))
	n = int(input())
	listOf.sort()
	first = 0
	last = len(listOf)-1
	found = False

	while first <= last and not found:
		midpoint = (first + last)//2
		if listOf[midpoint] == n:
			found = True
		else:
			if n < listOf[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1

	print(found)





binary_search()
