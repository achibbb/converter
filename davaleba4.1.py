num = int(str(input("N: ")))
if num < 10:
	print("Error!")
num = str(num)
for i in reversed(num):
	print(i, end="")