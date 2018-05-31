m1=int(input("Enter the marks:"))
m2=int(input("Enter the marks:"))
m3=int(input("Enter the marks:"))
m4=int(input("Enter the marks:"))
m5=int(input("Enter the marks:"))
avg=((m1+m2+m3+m4+m5)/5)
print(avg)
if avg>=75:
	print("A")
elif avg>=60 and avg<75:
	print("B")
elif avg>=50 and avg<60:
	print("C")
elif avg>35 and avg<50:
	print("D")
else:
	print("Fail")
	
