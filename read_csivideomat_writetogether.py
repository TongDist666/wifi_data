# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:10:22 2019

@author: TongDist
"""

import pickle
import scipy.io
#import _thread

def task(inp):
    with open('./csi_frame/'+str(inp)+'.pkl','rb') as rf:
            csi = pickle.load(rf)
            mat_name='./mat/'+str(inp)+'.mat'
            data=scipy.io.loadmat(mat_name)
            scipy.io.savemat(mat_name,{'csi':csi,'heatmaps':data['heatmaps']})
            print('writing'+str(inp))

f=1

try:
    while True:
        task(f)
        f+=1
        print(f)
except:
    print('something wrong!!')
