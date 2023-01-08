'''
def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print('you tried to divide by 0')

print(div42by(2))
print(div42by(0))
print(div42by(1))
'''

number = input()

try:
    if int(number) > 4:
        print("that's is a lot")
    elif int(number) < 0:
        print("that is impossible")
    else:
        print("meh")
except:
    print("put a number")
