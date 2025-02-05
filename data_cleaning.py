#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load dataset
data = pd.read_csv("tiktok_dataset.csv")

# Drop missing values
data_cleaned = data.dropna()

# Convert data types if necessary
data_cleaned['video_id'] = data_cleaned['video_id'].astype(str)

# Save cleaned dataset
data_cleaned.to_csv("cleaned_tiktok_dataset.csv", index=False)

print("Data cleaning complete. Saved cleaned dataset.")


# In[ ]:




