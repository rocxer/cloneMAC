# -*- coding: utf-8 -*-
'''
本文件配合CLONEIP读取文件中ip,mac对应关系。
作者：rocxer
日期：2013.10.12
Ver:beta
=======
文件格式：按照ip顺序排序
ip mac
'''
import os
#os.system('cls')
#读取文件，插入例子。
#'''
#====from http://bbs.csdn.net/topics/390109364
def eachlineof(handle):#filename):
    #逐行读取给定的文本文件，返回行号、剔除末尾空字符的行内容 
    #with open(filename) as handle:
        for lno, line in enumerate(handle):
            yield lno+1, line.strip()#http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
#'''
#'''
#===========
def getline(handle, desired_line_number):
    if desired_line_number < 1:
        return ''
    for current_line_number,line in enumerate(handle):
        if current_line_number == desired_line_number - 1 :
            return line 
    return ''#都不符合的时候

#'''
'''
#不再使用
def showTen(handle):
    i=10
    for num,line in enumerate(handle):
        if i > 0:
            print(num+1,line.strip())#指针始终在文件尾.
            i-=1
        else:
            break
'''        
def seleMac(filename):
    f=open(filename)
    #f.seek(0,2)
    #endoffile=f.tell() #获取文件尾
    #print(endoffile)
    #f.seek(0)
    #print(endoffile)
    #print f.tell()
    #print getline(filename,12)
    #showTen(f)
    for n,ls in eachlineof(f):
        print n,ls
    #print eachlineof(f)
    sl=raw_input(u'line num')
    '''
    j=0
    while(sl == ''):
        showTen(f)
        f.tell()
        sl=raw_input(u'line num Or ENTER for go on')
        j+=1 
    #'''
    f.seek(0)
    line=getline(f,int(sl))
    ip=line[:-14]
    mac=line[-13:]#总是记不住的字符串子串方式
    #print('select %s%s'%(j,sl))
    f.close()
    return [ip],mac


#测试
#seleMac(r".\SCmac.txt")
