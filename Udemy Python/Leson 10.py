
# for value in range(1500, 2701):
# 	if (value%5) == 0:
# 		print(value, "is devidable by 5")
# 	else:
# 		pass

# 	if (value%7) == 0:
# 		print(value, "is devidable by 7")
# 	else:
# 		continue	


# l = [1, 2, 3, 4, 5, 6, 7, 8, 33, 35, 39]
# even = 0
# odd = 0

# for value in l:
# 	if (value%2) == 0:
# 		even = even + 1
# 	elif (value% 2) == 1:
# 		odd = odd + 1
# 	else:
# 		print("error")

# print("even numers:", even)
# print("odd numers:", odd)

# for value in range(1, 51):
# 	if ((value%3) == 0) & ((value%5) != 0) :
# 		print("Fizz")
# 	elif ((value%5) == 0) & ((value%3) != 0) :
# 		print("Buzz")
# 	elif ((value%5) == 0) & ((value%3) == 0) :
# 		print("FizzBuzz")
# 	else:
# 		print(value)

# n = 120
# sum = 0

# for value in range(1,n):
# 	sum = sum + value

# average = sum / n
# print("Sum = ", sum, ", Average = ", average)


n = 4
product = 1

while n != 0 :
	product = product * n
	n = n - 1

print(product)

