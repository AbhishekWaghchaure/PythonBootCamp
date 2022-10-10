import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# pd.set_option('display.max_columns', None)

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
data = load_breast_cancer()
print(data.keys())
print(data['feature_names'])
df = pd.DataFrame(data['data'], columns=data['feature_names'])
print(df.head().to_string())

scalar = StandardScaler()
scalar.fit(df)
scaled_data = scalar.transform(df)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)
print(scaled_data.shape)
x_pca = pca.transform(scaled_data)
print(x_pca.shape)
print(x_pca)


plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c = data['target'], cmap='plasma')
plt.xlabel('First principle component')
plt.ylabel('Second principle component')


