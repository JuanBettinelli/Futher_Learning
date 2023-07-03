# break
# continue
# enumerate

# l = [10, 20, 30, 40, 50, 60]
# key = 400

# for value in l:
# 	if value == key:
# 		print("Element found")
# 		break
# 	else:
# 		continue
# else:
# 	print("element not found")

# print("statment after the for loop")


l = [10, 20, 30, 40, 50, 60]
key = 40

for index, value in enumerate(l):
	# print(index, value)
	if value == key:
		print("Element found at index:", index)
		break
	else:
		pass
		print("element not found yet")
else:
	print("element not found")

print("statment after the for loop")


# else:
# break
# continue
# pass
# enumerate


