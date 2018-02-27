import os
import re


def main():
    path = 'D:/OneDrive - Lqs/牛三库/700-800/fsh'
    path=input("input path:")
    origen = os.listdir(path)
    a = ''
 
    for i in range(len(origen)):
        string = origen[i]
        string = string[string.find('-A')+2:]
        string = string[0:string.find('-')]
        a+=string+'\n'
    # print(a)
    writeFile(a, "001.txt")
# ==============================================================#


def readFile(path):
    with open(path, "r", encoding='utf-8') as fopen:
        content = fopen.readlines()
    return content


def writeFile(string, name):
    with open(name, "w+", encoding='utf-8') as fwrite:
        fwrite.write(string)


# ==============================================================#
if __name__ == '__main__':
    main()
