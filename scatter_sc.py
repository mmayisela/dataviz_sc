#Import libraries
from inspect import stack
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load dataset

breastcancer = pd.read_csv("https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")
print(breastcancer.columns)

#Create scatterplot for texture_mean vs radius_mean showing malignant and benign

sns.scatterplot(data = breastcancer, 
               x = "texture_mean", 
                y = "radius_mean", 
                hue = "diagnosis")
plt.show()