# help(str)
# print(dir(str))

# format
# num1 = 100
# num2 = 200

# print("num1 is", num1, "num2 is", num2)
# print("Value of num1 is {1}, value of num2 ist {0}".format(num1, num2)) #values in format are saved by index 0, 1, 2,..

# print("Value of num1 is {val2}, value of num2 ist {val1}".format(val1=num1, val2=num2))

# s = "python sample string"
# s1 = s.capitalize()
# print(s1)

# upper
# lower
# title

# print(s.upper())
# print(s.lower())
# print(s.title())

# print(s.isupper())
# print(s.islower())
# print(s.istitle())



# split
# join

# s = "html, css, java, delphi, python"
# l = s.split(",")
# print(l)

# s1 = (" ").join(l)

# print(s1)


# maketrans
# translate

# s1 = "abcd"
# s2 = "1234"

# s3 = "python sample string abcd"

# table = str.maketrans(s1, s2)
# result = s3.translate(table)
# print(result)


# index
# find
# rfind funktion

# s = "html, css, java, delphi, python"

# print("python" in s)
# print(s.index("python"))

# print(s.find("Python"))
# print(s.rfind("python"))


# s = "       this is a sample string    "
# s1 = s.strip(" ")
# s2 = s.lstrip(" ")
# s3 = s.rstrip(" ")
# print(s1)


# s = "python"
# s1 = s.center(20, "*")
# s2 = s.ljust(20, "*")
# s3 = s.rjust(20, "*")
# print(s3)




s = "html, css, java, delphi, python"
s1 = s.replace("html", "html5")
print(s1)





