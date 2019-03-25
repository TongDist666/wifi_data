# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:54:49 2019

@author: TongDist
"""
def get_csi_xwfz(datastr):
    result=[]
    temp1=datastr.split('$')
    temp2=temp1[1].split('_')
    for t in temp2:
        temp_t=t.split('+')
        result.append([float(temp_t[1]),#相位
                       float(temp_t[2])])#幅值
    return result
def reshape(list_in,size=1):
    if len(list_in)%size!=0:
        print('input size is wrong!!')
        return False
    else:
        final_result,temp=[],[]
        for i in range(len(list_in)):
            if (i+1)%size!=0:
                temp.append(list_in[i])
            else:
                temp.append(list_in[i])
                final_result.append(temp)
                temp=[]
        return final_result
def reshape513(data513):
    data_temp=reshape(data513,57)
   
    final_result=[]
    for c in range(57):
        temp9=[[data_temp[0][c],data_temp[1][c],data_temp[2][c]],
               [data_temp[3][c],data_temp[4][c],data_temp[5][c]],
               [data_temp[6][c],data_temp[7][c],data_temp[8][c]]]
        final_result.append(temp9)
    return final_result
with open('1.txt','r') as data_read:

    dat=data_read.readline()
    #print(dat)
    dat1=get_csi_xwfz(dat)
#    print(dat1)
#    dat2=reshape(dat1,57)
#    print(dat2)
#    final=[]
#    for c in range(57):
#        temp9=[[dat2[0][c],dat2[1][c],dat2[2][c]],
#               [dat2[3][c],dat2[4][c],dat2[5][c]],
#               [dat2[6][c],dat2[7][c],dat2[8][c]]]
#        final.append(temp9)
#    print(final)
    re=reshape513(dat1)
    print(re)
