import os

filename = "task_6.txt"

if os.path.exists(filename):
    file = open(filename,'r')
    print(file.read())

    file.close()
else:
    print("file not found. please check the filename.")