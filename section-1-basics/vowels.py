while True: 
    user = input('Enter your senteces: ')
    vowels = "A,I,U,O,E,i,a,e,u,o"
    total = 0
    for i in user:
        if i in vowels:
            total+=1
    print(total)