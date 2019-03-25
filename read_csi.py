# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:04:04 2019

@author: TongDist
"""

import pickle
#import scipy.io
f=1

with open('./csi_frame/'+str(f)+'.pkl','rb') as rf:
    csi = pickle.load(rf)
    #mat_name='./mat/'+str(f)+'.mat'
    #data=scipy.io.loadmat(mat_name)
   # csi_data=data['csi']
    print(csi)
    print(len(csi[0]))
    print(len(csi[0][0]))
