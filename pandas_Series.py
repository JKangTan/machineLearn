
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# Seris
my_int_list = [1, 2, 3]
my_str_list = ['a', 'b', 'c']
my_np_list = np.array(my_int_list)
print(pd.Series(my_int_list))  # value
print(pd.Series(my_np_list, my_str_list))  # value index\
print(pd.Series({'a':1, 'b':2, 'c':3}))
pt1 =  pd.Series([min, max, abs], my_str_list)
print(pt1)  # pt1['a'] 指向min方法
print("pt1['a'] -> min: %d" % pt1['a']([1,3,5,2,0]))

