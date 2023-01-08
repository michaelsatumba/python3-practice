def hello(name):
    print("hello " + str(name))

hello("mj")


def plusOne(number):
    return number + 1
    

    

n = plusOne(5)
print(n)


def spam():
    global bacon
    print(bacon)
    bacon = 'yumdvv'
    

bacon = 'yuk'
spam()
print(bacon)

