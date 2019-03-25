# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:31:54 2019

@author: TongDist
"""
import scipy.io


inp=1
mat_name='./mat/'+str(inp)+'.mat'
data=scipy.io.loadmat(mat_name)
#scipy.io.savemat(mat_name,{'csi':csi,'heatmaps':data['heatmaps']})
csi_mat=data['csi']
print(csi_mat)
print(csi_mat.shape)
