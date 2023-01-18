import os

for folderName, subfolders, filenames in os.walk("C:\\Users\\Kuya\\Desktop\\example"):
    print(folderName)
    print(subfolders)
    print(filenames)
