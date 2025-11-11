#Import libraries
from inspect import stack
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load dataset

breastcancer = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")
print(breastcancer.columns)

#Scatter plot for smoothness_mean vas compactness_mean
sns.scatterplot(data = breastcancer, 
               x = "smoothness_mean", 
               y = "compactness_mean", 
               hue = "diagnosis")

# Save to a folder (e.g., "plots")
plt.savefig("plots/scatter_bc_sc.png", dpi=300, bbox_inches='tight')
plt.close()

