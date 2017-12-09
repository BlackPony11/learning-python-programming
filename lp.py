#!usr/bin/python3
arr = []
size = 10
s = []

def buble(listForSort):
    length = len(listForSort) - 1
    sorteda = False
    while not sorteda:
        sorteda = True
        for i in range(length):
            if listForSort[i] > listForSort[i + 1]:
                sorteda = False
                listForSort[i], listForSort[i + 1] = listForSort[i + 1], \
                                                     listForSort[i]


def median(array):
    half = len(array) // 2
    if not len(arr) % 2:
        print((arr[half - 1] + arr[half]) / 2)
    else:
        print(arr[half])

continueLoop = True
while continueLoop:
    print("What do you want, input values from keybord or from file?(1/2): \n")
    inp = int(input())
    if inp == 1:
        for i in range(size):
            arr.append(int(input("Pleas input values")))
    elif inp == 2:
        ifile = str(
            input("Please, input the file name(without extention and ''): \n"))
        with open(ifile) as f:
            arr = f.read().splitlines()
            arr = (list(map(int, arr)))
    else:
        continueLoop = \
            True if \
                input("Choose eather 1 or 2. Do you want to repeat? (y\\n)\n") == 'y' \
            else False
        continue
    print(arr)
    sort = int(input("Do you want to sort u array?(1/2): "))
    if sort == 1:
        for i in arr:
            if i not in s:
                s.append(i)
        buble(s)
        print(s)
    elif sort == 2:
        pass
    else:
        print("What is this?")
        pass
    buble(arr)
    cont = int(input("Do u wanna find average?(1/2): "))
    if cont == 1:
        print(sum(arr) / float(len(arr)))
    else:
        pass
    nextstep = int(input("Do u wanna find median number?(1/2): "))
    if nextstep == 1:
        median(arr)
        choice = int((input('Do u want to repeat this programm? 1/2\n')))
    else:
        choice = int((input('Do u want to repeat this programm? 1/2\n')))
    if choice == 1:
        arr[:] = []
        s[:] = []
        continue
    elif choice == 2:
        break
    else:
        exit
