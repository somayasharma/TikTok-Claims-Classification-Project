#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
data = pd.read_csv("cleaned_tiktok_dataset.csv")

# Visualize engagement trends
plt.figure(figsize=(8,5))
sns.boxplot(x="claim_status", y="video_view_count", data=data, palette="coolwarm")
plt.title("View Count Distribution by Claim Status")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt='.2f')
plt.title("Feature Correlation Heatmap")
plt.show()


# In[ ]:




