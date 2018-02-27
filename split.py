import os

def main():
    origen = readFile('load.txt')
    print('Origen_length:%d'%len(origen))
    newlist = ''
    left=''
    for i in range(len(origen)):
        string = origen[i]
        new1 = get_H(string)
        new2 = get_Z(string)
        new3 = get_G(string)
        new4 = get_B(string)
        new5 = get_K(string)
        new6 = get_XZSH(string)
        new7 = get_YW(string)
       
        rlist = [new7, new6, new5, new4, new3, new2, new1,  '。']
        left += remove(string,rlist)
        newlist += new2+'\n'
    writeFile(newlist,"anew1.txt")
    writeFile(left, "left.txt")

# ==============================================================#
def remove(s,lis):
    for i in range(len(lis)):
        s=s.replace(lis[i],'')
    s = s.replace('；', '，')
    s = s.replace('，，', '，')
    s = s.replace('，，', '，')
    s = s.replace('，\n', '\n')
    if len(s)>0 and s[0] == '，':
        s = s.replace('，', '',1)
    return s
    

def get_H(string):    
    s=''    
    if len(string) > 3 :
        if string[1] == '行' and string[0]<'\x3a':
            s = string[0:string.find('行') + 1]
        elif string[2] == '行' and string[0]<'\x3a':
            s = string[0:string.find('行') + 1]                
    return s

def get_Z(string):
    s = ''
    if string.find('字或') != -1:
        pass
    elif  string.find('行') != -1 and string.find('字') != -1:
        s = string[string.find('行')+1:string.find('字') + 1]
        if len(s) <2 or len(s) > 3 :
            s=''
        elif s[0]>'\x39' or s[0]<'\x30':
            s=''

    return s

def get_YW(string):
    s = ''
    if string.find('單魚尾') != -1:
        s = '單魚尾'
    elif string.find('雙魚尾') != -1:
        s = '雙魚尾'

    return s



def get_XZSH(string):
    s = ''
    if string.find('小字雙行同') != -1:
        s = '小字雙行同'
    # elif string.find('小字雙行') != -1:
    #     s = '小字雙行'
    else:
        s = get(string, '小字雙行', '，')    
    return s


# def get_E(string):
#     if string.find('有耳') != -1:
#         string = '有耳'
#     # elif string.find('無格') != -1:
#     #     string = '無格'
#     # elif string.find('綠格') != -1:
#     #     string = '綠格'
#     else:
#         string = ''
#     return string

def get_G(string):
    s = ''
    if string.find('無直格') != -1:
        s= '無直格'
    elif string.find('無格') != -1:
        s= '無格'
    elif string.find('小藍格') != -1:
        s= '小藍格'
    elif string.find('黑格') != -1:
        s= '黑格'
    elif string.find('小紅格') != -1:
        s= '小紅格'
    elif string.find('紅格') != -1:
        s= '紅格'
    elif string.find('綠格') != -1:
        s= '綠格'
    elif string.find('藍格') != -1:
        s= '藍格'
    elif string.find('綠格') != -1:
        s= '綠格'
    elif string.find('綠格') != -1:
        s= '綠格'

    return s

def get_K(string):
    s = ''
    if string.find('白口') != -1:
        s= '白口'
    elif string.find('細藍口') != -1:
        s= '細藍口'
    elif string.find('藍口') != -1:
        s= '藍口'
    elif string.find('綠口') != -1:
        s= '綠口'
    elif string.find('線黑口') != -1:
        s= '線黑口'
    elif string.find('細黑口') != -1:
        s= '細黑口'
    elif string.find('紅黑口') != -1:
        s= '紅黑口'
    elif string.find('大黑口') != -1:
        s= '大黑口'
    elif string.find('粗黑口') != -1:
        s= '粗黑口'
    elif string.find('上下黑口') != -1:
        s= '上下黑口'
    elif string.find('下黑口') != -1:
        s= '下黑口'
    elif string.find('黑口') != -1:
        s= '黑口'
    # elif string.find('白口') != -1:
    #     s= '白口'

    return s

def get_B(string):
    s = ''
    z = '邊或'
    a = '四周單邊'
    b = '四周雙邊'
    c = '左右單邊'
    d = '左右雙邊'
    e = '上下雙邊'
    f = '上下單邊'
    if  string.find(z) != -1:
        s= ''
    elif string.find(a) != -1:
        s= a
    elif string.find(b) != -1:
        s= b
    elif string.find(c) != -1:
        s= c
    elif string.find(d) != -1:
        s= d
    elif string.find(e) != -1:
        s= e
    elif string.find(f) != -1:
        s= f
    

    return s

# ==============================================================#

def removeBetween(string, head, tail):
    while string.find(head) != -1:
        left = string[0:string.find(head)]
        revleft = string[string.find(head) + len(head):]
        right = revleft[revleft.find(tail) + len(tail):]
        string = right
    return string


def get(string, head, tail):
    if string.find(head)!=-1 and string.find(tail)!=-1:
        s = string[string.find(head):]
        s = s[:s.find(tail) ]
    else:
        s=''
    return s

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
