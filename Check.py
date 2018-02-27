#======================================================#
import os
#======================================================#
imageFolderPath = "./PDF"
filePath = "list.txt"
#======================================================#
eName = 0
ePicture = 0
imgsum = 0
Low=0
High =32
scale =100

def main():
    name_list = loadNameList(filePath)
    folder_list = listDir(imageFolderPath)
    for i in range(len(folder_list)):
    # for i in range(Low,High):
        path = imageFolderPath+'/'+'P'+adjust(i,2)+'01-P'+adjust(i+1,2)+'00'
        image_list = listDir(path)
        check(image_list,name_list,i)        
    print("Count of eName:",eName)
    print("Count of ePDF:",ePicture)
    print("Count of PDF:", imgsum)

def check(img, name,index):
    relname = name[index*scale:min((index+1)*scale,len(name))]
    img_len = len(img)
    for i in range(len(relname)):
        if relname[i] in img:
            img.remove(relname[i])
            relname[i]= None        
        elif relname[i] ==".pdf":
            relname[i] = None
    
    relname = remNone(relname)
    # nimg = rem(img)


    print("-" * 80,'Start-with-',index*scale)
    print(">>>Name(%d): "%len(relname))
    for i in range(len(relname)):                
        print(relname[i])

    print("-" * 50, 'PDF Count=', img_len)

    print(">>>PDF(%d):"%len(img))
    for i in range(len(img)):        
        print(img[i])
        # print(nimg[i])
    print("-" * 80,'End-with-',(index+1)*scale)
    print()

    global eName ,ePicture,imgsum
    eName += len(relname)
    ePicture += len(img)
    imgsum += img_len

def remNone(lis):
    while lis.count(None) != 0:
        lis.remove(None)
    return lis
# ====================================================
def loadNameList(path):
    with open(path, "r") as fopen:
        lines = fopen.readlines()

    if(lines[0] == 'PDF文件名\n'):
        lines.remove('PDF文件名\n')    
    while(lines[len(lines)-1] == '\n'):
        lines.pop()
        
    length = len(lines)
    for i in range(length):
        lines[i] = lines[i].replace("\n", ".pdf")
    return lines

def listDir(path):
    return os.listdir(path)


def adjust(num, length):
    num = '0' * length + str(num)
    num = num[len(num) - length:]
    return num
#======================================================#
if __name__ == '__main__':
    main()
#======================================================#
