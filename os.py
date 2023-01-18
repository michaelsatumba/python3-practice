helloFile = open("C:\\Users\\Kuya\\Desktop\\hello.txt", "w")

content = helloFile.write("hola mundo")

print(content)

helloFile.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['dogs'] = ['armando', 'rob', 'david']
shelfFile.close()

