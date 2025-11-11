#Differential expression results for chromosome 22. Plot log2FoldChange vs log10(Padj) from the DEG results.

import pandas as pd
import matplotlib.pyplot as plt

chr22 = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/main/Python/Dataset/hbr_uhr_deg_chr22_with_significance.csv")

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

# Save to a folder (e.g., "plots")
plt.savefig("plots/scatter_sc_deg.png", dpi=300, bbox_inches='tight')
plt.close()
