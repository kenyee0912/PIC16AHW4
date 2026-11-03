#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:48:00 2026

@author: Kenneth Yee
"""

#%%
import numpy as np
import matplotlib.image as mpimg


#%% Q1
a = mpimg.imread('a.jpg')
b = mpimg.imread('b.jpg')


#PART A
#Index of where to insert is at index (137, 130)
#Get the slice

# a_slice = a[137:457,130:370]
# c = a.copy()
# c[137:457,130:370] = b


#PART B and C
# a = np.concatenate((a, a[-1:]))         #Adds the array a with last row of a at end
# b = np.concatenate((b[: 1], b))         #Adds first row of b (index 0 to 1 excluding 1) with b

# print("Shape of a: ", a.shape)
# print("Shape of b: ", b.shape)


a_num_row, a_num_col, a_rgb = a.shape
b_num_row, b_num_col, b_rgb = b.shape           #Assuming a is large and b is small

#Let b_num_col dictate the size of the slice of a


row_diff_div2 = (a_num_row - b_num_row) // 2   #integer division so it'll always be the smaller even integer
col_diff_div2 = (a_num_col - b_num_col) // 2    #same with column


row_end = row_diff_div2 + b_num_row
col_end = col_diff_div2 + b_num_col

c = a.copy()
c[row_diff_div2 : row_end, col_diff_div2 : col_end] = b




mpimg.imsave('c.jpg', c)


#%% Q2
d = mpimg.imread('d.jpg')
e = mpimg.imread('e.jpg')

d = d.astype(np.int16)
e = e.astype(np.int16)

# bool_mask = ((abs(d[...,0] - e[...,0]) > 60)  | 
#              (abs(d[...,1] - e[...,1]) > 60) | 
#              (abs(d[...,2] - e[...,2]) > 60))

bool_mask = (abs(d[...,0] - e[...,0]) +
             abs(d[...,1] - e[...,1]) + 
             abs(d[...,2] - e[...,2]) > 111)

f = d.copy()
f[~bool_mask] = [0,0,0]
f = f.astype(np.uint8)

mpimg.imsave('f.jpg', f)


#%% Q3
minion = mpimg.imread('g.jpg')
shugga = mpimg.imread('h.jpg')


bool_mask = ((minion[...,1] > 160) & (minion[...,0] < 120))
minion_pink_bg = minion.copy()
minion_pink_bg[bool_mask] = [255,100,255]


i = shugga.copy()

minion_num_row, minion_num_col, minion_rgb = minion.shape
shugga_num_row, shugga_num_col, shugga_rgb = shugga.shape

minion_row_idx = shugga_num_row - minion_num_row    #At bottom of shugga image
minion_col_idx = (shugga_num_col - minion_num_col) // 2

i[minion_row_idx: minion_row_idx + minion_num_row, minion_col_idx: minion_col_idx + minion_num_col] = minion_pink_bg


new_mask = (((i[:,:]) == [255,100,255]).all(axis=-1))


i[new_mask] = shugga[new_mask]


# mpimg.imsave('i.jpg', i)
