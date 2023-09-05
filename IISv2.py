ip_str = str(input("EnTeR ThE CiPhEr TeXt: "))
n = 0

while(n!=27):
	op_str1 = []
	op_str2 = []
	for i in ip_str:
		ascode = ord(i)
		sam1 = chr(ascode+n)
		sam2 = chr(ascode-n)
		op_str1.append(sam1)
		op_str2.append(sam2)

	op1 = ''.join(map(str,op_str1))
	op2 = ''.join(map(str,op_str2))
	print("Position: "+str(n)+", Left Shift: "+op2+", Right Shift: "+op1)
	n = n+1
