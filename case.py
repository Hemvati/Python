instr=str(input("Enter a string:"))
res=""
for i in range(len(instr)):
	if instr[i].isupper():	
		res+=instr[i]
print(res)
ab=""
for i in range(0,len(instr),2):
	#if instr[i].isupper():
	ab+=instr[i]
print(ab)
