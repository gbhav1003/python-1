#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# # Task 1: Create an Array and Basic Math

# In[2]:


import numpy as np
import time

temps_celsius = np.array([22, 25, 28, 24, 26])
print(f"Celsius: {temps_celsius}")

temps_fahrenheit = temps_celsius * 1.8 + 32
print(f"Fahrenheit: {temps_fahrenheit}")

avg_fahrenheit = np.mean(temps_fahrenheit)
print(f"Average Fahrenheit: {avg_fahrenheit:.1f}")


# # Task 2: Array Shape and Statistics

# In[3]:


scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print(f"Shape: {scores.shape}")
print(f"Total Elements: {scores.size}")

highest = np.max(scores)
print(f"Highest Score: {highest}")

lowest = np.min(scores)
print(f"Lowest score: {lowest}")

score_range = highest - lowest
print(f"Range: {score_range}")


# # Task 3: Performance Comparison

# In[8]:


n_elements = 50000
np_arr = np.arange(1, n_elements + 1)
py_list = list(range(1, n_elements + 1))

start_np = time.time()
np_sum = np.sum(np_arr)
end_np = time.time()
time_np = end_np - start_np

start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()
time_py = end_py - start_py

speedup = time_py / time_np

print(f"NumPy sum: {np_sum}")
print(f"Python sum: {py_sum}")
print(f"NumPy time: {time_np:.4f} seconds")
print(f"Python time: {time_py:.4f} seconds")
print(f"NumPy is {speedup:.1f}x faster")


# In[ ]:





# In[ ]:





# In[ ]:




