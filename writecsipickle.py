# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:26:12 2019

@author: TongDist
"""

data_read=open('data.txt','r')
video_time_read=open('VideoTimestamp','r')

#data_test=data_read.readline()
#video_time_test=video_time_read.readline()

#print(data_test)
#print(video_time_test)

#获取 video时间戳的 [小时，分，秒，'毫秒']
def get_video_hmsus(timestr):
    #输入形式：'2019-03-14 14:55:54.033745'
    result=[]
    temp1=timestr.split()[1]
    temp2=temp1.split(':')
    result.append(int(temp2[0]))
    result.append(int(temp2[1]))
    temp_s=temp2[2].split('.')
    result.append(int(temp_s[0]))
    result.append(temp_s[1])
    return result

#获取 csi 时间戳的 [小时，分，秒，'毫秒']
def get_csi_hmsus(datastr):
    result=[]
    temp1=datastr.split('$')
    temp2=temp1[0].split()
    result.append(int(temp2[3]))
    result.append(int(temp2[4]))
    result.append(int(temp2[5]))
    result.append(temp2[6])
    return result

#获取csi的相位和幅值
def get_csi_xwfz(datastr):
    result=[]
    temp1=datastr.split('$')
    temp2=temp1[1].split('_')
    for t in temp2:
        temp_t=t.split('+')
        result.append([complex(float(temp_t[1]),float(temp_t[2]))])
#        result.append([int(temp_t[0]),#count
#                       float(temp_t[1]),#相位
#                       float(temp_t[2])])#幅值
    return result
#print(get_video_hmsus(video_time_test))
#print(get_csi_hmsus(data_test))
#print(get_csi_xwfz(data_test))
    
#从刚读完的video时间戳list
#获取 video时间戳的 [小时，分，秒，'毫秒']
def get_format_hmsus_fromvideo(videoTimeList):
    result=[]
    for vtl in videoTimeList:
        result.append(get_video_hmsus(vtl))
    return result

#从csi读data的 list中获取规格化的数据
#[[小时，分，秒，'毫秒'],[[count，相位，幅值]，...]     ]
def get_format_data_csi(csiDataList):
    result=[]
    for gfdc in csiDataList:
        #获取 csi 时间戳的 [小时，分，秒，'毫秒']
        time_temp=get_csi_hmsus(gfdc)
        time_temp[3]=time_temp[3].zfill(6)
        #获取csi的相位和幅值
        data_temp=get_csi_xwfz(gfdc)
        result.append([time_temp,data_temp])
    return result

#csi的us 规格化为六位字符串 少的左边补0
def format_csi_us(usStr):
    if len(usStr)==6:
        return usStr
    else:
        while len(usStr)<6:
            usStr='0'+usStr
        return usStr
#video的s 规格化为2位字符串 少的左边补0
def format_video_s(sStr):
    if len(sStr)==2:
        return sStr
    else:
        while len(sStr)<2:
            sStr='0'+sStr
        return sStr

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

data_read_list=[]
video_time_read_list=[]
try:
    data_read_list=data_read.readlines()
    print(len(data_read_list))
except:
    print('something wrong!\ndata read!!!')
    

try:
    video_time_read_list=video_time_read.readlines()
    print(len(video_time_read_list))
except:
    print('something wrong!\nvideo read!!!')
    
video_format_time=get_format_hmsus_fromvideo(video_time_read_list)
csi_format_data=get_format_data_csi(data_read_list)
#print(csi_format_data[0][1][:4])
count=0
final_result=[]

frame_count=10

for i in range(len(video_format_time)):
    for j in range(len(csi_format_data)-1):
        if video_format_time[i][0]==csi_format_data[j][0][0] and video_format_time[i][1]==csi_format_data[j][0][1]:
            #小时 分一样，比较秒和毫秒
            temp_v=str(video_format_time[i][2]).zfill(2)+video_format_time[i][3]
            temp_s=str(csi_format_data[j][0][2]).zfill(2)+csi_format_data[j][0][3]
            temp_s2=str(csi_format_data[j+1][0][2]).zfill(2)+csi_format_data[j+1][0][3]
            if temp_v>=temp_s and temp_v<=temp_s2:
                count+=1
                print(count)
                print(video_format_time[i])
                print(csi_format_data[j][0])
                print(csi_format_data[j+1][0])
                temp_re=[]
                for r_i in range(frame_count):
                    print(j+r_i-frame_count//2)
                    temp_re.append(reshape513(csi_format_data[j+r_i-frame_count//2][1]))
                final_result.append(temp_re)

import pickle
f=1
for d in final_result:
    with open('./csi_frame/'+str(f)+'.pkl','wb') as pic:
        pickle.dump(d,pic)
        f+=1
        print('writing'+str(f))

data_read.close()
video_time_read.close()