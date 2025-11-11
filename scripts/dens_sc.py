#Import libraries
from inspect import stack
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


#Load dataset

breastcancer = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")
print(breastcancer.columns)

#Density plot for area_mean
sns.kdeplot(data = breastcancer,
            x = "area_mean",
            hue = "diagnosis",
            multiple = "stack",
            common_norm=False, 
            alpha=.5, linewidth=0)

# Save to a folder (e.g., "plots")
plt.savefig("plots/dens_sc.png", dpi=300, bbox_inches='tight')
plt.close()