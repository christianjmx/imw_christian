import sys

n=int(sys.argv[1])

if n <= 0:
	print("Error")
	exit()
elif n==1:
	print(n, "por convenio no es ni primo ni compuesto")
else:
	for i in range(2, n):
		p=n%i
		if p==0:
			print(n, "no es primo.")
			exit()
	print(n, "es primo.")