#Import libraries

from inspect import stack
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load dataset

breastcancer = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")
print(breastcancer.columns)

#Correlation heatmap for seleted features

#Subset columns of interest

selected_cols = ["radius_mean", "texture_mean", "perimeter_mean", "area_mean", "smoothness_mean", "compactness_mean"]
subset = breastcancer[selected_cols]

sns.heatmap(data = subset.corr(),
            annot = True,
            cmap = "Blues"
             )
plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)
plt.tight_layout()
plt.title("Correlation Heatmap of Selected Features")

# Save to a folder (e.g., "plots")
plt.savefig("plots/corr_hm_sc.png", dpi=300, bbox_inches='tight')
plt.close()


