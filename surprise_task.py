#Visualising single cell sequencing data

###Gene expression analysis###

#Using the python3 environment
# python3 -m venv venv
#source venv/bin/activate

#Import libraries
from inspect import stack
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# A. Create clustered heatmap of the top differentially expressed genes between HBR and UHR samples

# Load datasets using pandas
gene_counts = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/main/Python/Dataset/hbr_uhr_top_deg_normalized_counts.csv")
chr22 = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/main/Python/Dataset/hbr_uhr_deg_chr22_with_significance.csv")

print(gene_counts.columns)

#Set gene names as index if needed
gene_counts.set_index('Unnamed: 0', inplace=True)

# Plot heatmap
sns.clustermap(gene_counts, cmap='Blues', xticklabels=True, yticklabels=True)
plt.title("Heatmap of Normalized Gene Counts")
plt.show()


# B. Differential expression results for chromosome 22. Plot log2FoldChange vs log10(Padj) from the DEG results.

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
#url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/main/Python/Dataset/hbr_uhr_deg_chr22_with_significance.csv"
#chr22 = pd.read_csv(url)

#Define color mapping
color_map = {
  'up': 'green',
  'down': 'blue',
  'ns': 'orange'
}

chr22['color'] = chr22['significance'].map(color_map)

#Plot
plt.figure(figsize=(10, 6))
plt.scatter(chr22['log2FoldChange'], chr22['-log10PAdj'], c=chr22['color'], alpha=0.7, edgecolor='black', linewidth=0.5)
plt.axvline(x=1, color='black', linestyle='--')
plt.axvline(x=-1, color='black', linestyle='--')
plt.xlabel('log₂ Fold Change')
plt.ylabel('–log₁₀ Adjusted P-value')
plt.tight_layout()
plt.show()



#Breast cancer data eploration

#Load dataset

breastcancer = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")
print(breastcancer.columns)

#C Create scatterplot for texture_mean vs radius_mean showing malignant and benign

sns.scatterplot(data = breastcancer, 
               x = "texture_mean", 
                y = "radius_mean", 
                hue = "diagnosis")
plt.show()


#D Correlation heatmap for seleted features

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
plt.show()



#E Scatter plot for smoothness_mean vas compactness_mean
sns.scatterplot(data = breastcancer, 
               x = "smoothness_mean", 
               y = "compactness_mean", 
               hue = "diagnosis")
plt.show()

#F Density plot for area_mean

sns.kdeplot(data = breastcancer,
            x = "area_mean",
            hue = "diagnosis",
            multiple = "stack",
            common_norm=False, 
            alpha=.5, linewidth=0)
plt.show()