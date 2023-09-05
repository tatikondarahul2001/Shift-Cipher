ip_str = str(input("Enter the Cipher text that you want to decrypt: "))
op_str1 = []
op_str2 = []
for i in ip_str:
	#print(i)
	asccode = ord(i)
	#print(asccode)
	#print(chr(asccode+3))
	sam1 = chr(asccode+3)
	sam2 = chr(asccode-3)
	op_str1.append(sam1)
	op_str2.append(sam2)

op1 = ''.join(map(str,op_str1))
op2 = ''.join(map(str,op_str2))

print("If left shift operation is performed the output is:",op1)
print("If Right shift operation is performed the output is:",op2)
