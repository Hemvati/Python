d1 = {1:"Abc",2:"Xyz"}
d4=input("Enter a key:")
print(d4)
if d1[d4]:
	print("Entered key is present")
	del d1[d4]
else:
	print("Entered key isn't found")
	
	
