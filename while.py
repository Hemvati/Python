age=int(input("Enter your age:"))
n=age
fact=1

while (age>1):
	fact*=age
	age-=1
else:
	print("Python while loops have redundant else")
print("Factorial of your age is",fact)
