'''
spam = 0
while spam < 5:
    print('hi')
    spam = spam + 1
    print(spam)
'''

'''
name = ''
while name != 'ur name': #does not equal 'ur name' it will keep looping
    print('type ur name')
    name = input()
print('thanks')
'''

'''
name = ''
while True: 
    print('type ur name')
    name = input()
    if name == 'ur name':
        break #takes you out of loop
print('thanks')
'''

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # jumps back to condition of while loop
    print(str(spam))
