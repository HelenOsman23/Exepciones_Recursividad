def countdown(num):
    if num == 0:
        print("Blastoff!")
    else:
        print(num)
        countdown(num -1)
countdown(5)

print("--------------------")

def countdown2(num):
    for number in range(-num, 1):
        if number == 0:
            print("Blastoff")
        else:
            print(-number) 
countdown2(5)

print("--------------------")

def countdown3(num):
    for number in range(-num, 0):
        print(-number)
    print("Blastoff!")

countdown3(5)

print("--------------------")

def infinite_recursion(word):
    print(word)
    infinite_recursion(word)

infinite_recursion("palabra")    