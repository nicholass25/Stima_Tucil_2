# %%
import MyConvexHull as mch
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# input yang bisa digunakan sebagai contoh

# 0
# sepal length (cm)
# sepal width (cm)

# 0
# petal length (cm)
# petal width (cm)

# 1
# mean radius
# mean texture

# 1
# mean perimeter
# mean area

# minta input untuk menampilkan dari beberapa dataframe
dataset = int(input("0. Dataset iris 1. Dataset breast_cancer"))
x_col = input("Nama kolom untuk x")
y_col = input("Nama kolom untuk y")
title = x_col + " vs " + y_col


if(dataset == 0):
    data = datasets.load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
else:
    data = datasets.load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

index_0 = df.columns.get_loc(x_col)
index_1 = df.columns.get_loc(y_col)

# tes visualisasi
plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g']
plt.title(title)
plt.xlabel(data.feature_names[index_0])
plt.ylabel(data.feature_names[index_1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [index_0, index_1]].values
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for j in range(len(data.target_names)):
        coord = mch.Finishing(df, j, x_col, y_col, "Target")
        coord.append(coord[0])
        xs, ys = zip(*coord)
        plt.plot(xs, ys, c=colors[j])
plt.legend()

# %%
