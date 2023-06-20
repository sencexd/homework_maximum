def checker(x):
    func = False
    spisok = list(x)
    konec = len(x) - 1
    counter = 0
    for i in range(len(x)//2):
        if spisok[i] == spisok[konec]:
            counter += 1
            konec -= 1
    if counter == len(x)//2:
        func = True
    print(func)

        
