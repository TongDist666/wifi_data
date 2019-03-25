# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:46:14 2019

@author: TongDist
"""

import cv2
#摄像头编号:0  多摄像头的话记得查看各自的编号
cap = cv2.VideoCapture('video.avi')
#有的书上说X64的电脑上，这个地方要加：#0xFF != 27
#但是可以不加
count=1
try:
    while cv2.waitKey(1) & 0xFF != 27:
    
    	#frame是一帧的图像
        ret, frame = cap.read()
        dst=cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        cv2.imwrite('./frame_img/'+str(count)+'.jpg',dst)
        print('writing '+str(count))
        count+=1
except:
    print('something wrong!!')
#结束记得释放
cap.release()
print('Done')