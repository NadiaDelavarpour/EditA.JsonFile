#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[4]:


json_file_path = "H:/Ortho_Data/Annotation_Images/Image_All/labels_my-project-name_2023-04-12-06-04-27.json"


# In[5]:


with open(json_file_path, 'r') as f:
    data = json.load(f)


# In[6]:


# Define a function to recursively remove all occurrences of a particular key-value pair
def remove_key_value_pair(obj, key, value):
    if isinstance(obj, dict):
        return {k: remove_key_value_pair(v, key, value) for k, v in obj.items() if v != value or k != key}
    elif isinstance(obj, list):
        return [remove_key_value_pair(elem, key, value) for elem in obj if elem != value]
    else:
        return obj


# In[ ]:


# Remove all occurrences of "label":"HPU" from the Python object
data = remove_key_value_pair(data, "label:"HPU"")

