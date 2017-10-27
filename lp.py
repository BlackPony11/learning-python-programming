arr = []
size = 10
s=[]
def buble(bad_list):
	length = len(bad_list)-1
	sorteda = False
	while not sorteda:
		sorteda = True
		for i in range(length):
			if bad_list[i]>bad_list[i+1]:
				sorteda = False
				bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
def median(array):
	half = len(array)//2
	if not len(arr)%2:
		print ((arr[half-1]+arr[half])/2)
	else:
		print (arr[half])
while True:
	print("What do you want, input values from keybord or from file?(1/2): ")
	inp = input()
	if inp == 1:
		 for i in range(size):
			  arr.append(int(input("Pleas input values")))
	elif inp == 2:
		ifile=input("Please, input the file name(with extention and ''): ")
		with open(ifile) as f:
			arr = f.read().splitlines()
			arr = (list(map(int,arr)))
	else:
		pass
	print (arr)
	sort=input("Do you want to sort u array?(1/2): ")
	if sort == 1:
		for i in arr:
			if  i not in s:
				s.append(i)
		buble(s)
		print (s)
	elif sort == 2:
		pass
	else:
		print("What is this?")
		pass
	buble(arr)
	cont = input("Do u wanna find average?(1/2): ")
	if cont == 1:
		print (sum(arr)/float(len(arr)))
	else:
		pass
	nextstep = input("Do u wanna find median number?(1/2): ")
	if nextstep == 1:
		median(arr)
		choice = (input('Do u want to repeat this programm? 1/2\n'))
	else:
		choice = (input('Do u want to repeat this programm? 1/2\n'))
	if choice == 1:
		arr[:] = []
		s[:] = []
		continue
	elif choice == 2:
		break
	else:
		exit

