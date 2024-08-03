import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataframe = pd.read_csv("population_by_age_group.csv")
ages = [22, 25, 29, 34, 45, 50, 55, 60, 65, 70, 75, 80, 85]
plt.hist(ages, bins=10, edgecolor='black')
plt.xlabel('Count')
plt.ylabel('Age')
plt.title('Distribution of ages by population')
plt.show()
