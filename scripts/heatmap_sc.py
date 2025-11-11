#Import libraries
from inspect import stack
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Create clustered heatmap of the top differentially expressed genes between HBR and UHR samples

# Load datasets using pandas
gene_counts = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/main/Python/Dataset/hbr_uhr_top_deg_normalized_counts.csv")

print(gene_counts.columns)

#Set gene names as index if needed
gene_counts.set_index('Unnamed: 0', inplace=True)

# Plot heatmap
sns.clustermap(gene_counts, cmap='Blues', xticklabels=True, yticklabels=True)
plt.title("Heatmap of Normalized Gene Counts")

# Save to a folder (e.g., "plots")
plt.savefig("plots/heatmap_sc.png", dpi=300, bbox_inches='tight')
plt.close()