test = True

for i in range(12):
    for j in range(11):
        if test:
            print("*", end=" ")
            test = False
        else:
            print("+", end=" ")
            test = True

    print()