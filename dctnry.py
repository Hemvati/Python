dctnry={'a':1,'b':2,'c':3,'d':4}
print("Initial dictionary\n",dctnry)
a=input("Enter a key to delete(a-d):")
if a in dctnry:
	del dctnry[a]
	print("Updated dictionary\n",dctnry)
