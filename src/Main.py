# %%
import MyConvexHull as mch
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# contoh 1
# Data frame awal
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

# tes visualisasi
plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g']
plt.title('Sepal Width vs Sepal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [0, 1]].values
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])

    for j in range(len(data.target_names)):
        coord = mch.Finishing(df, j, "sepal length (cm)",
                              "sepal width (cm)", "Target")
        coord.append(coord[0])
        xs, ys = zip(*coord)
        plt.plot(xs, ys, c=colors[j])

plt.legend()

# %%
# contoh 2
# Data frame awal
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

# Data frame awal
plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[3])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [2, 3]].values
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for j in range(len(data.target_names)):
        coord = mch.Finishing(df, j, "petal length (cm)",
                              "petal width (cm)", "Target")
        coord.append(coord[0])
        xs, ys = zip(*coord)
        plt.plot(xs, ys, c=colors[j])

plt.legend()

# %%
# contoh 3
# Data frame awal
data = datasets.load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)

# Data frame awal
plt.figure(figsize=(10, 6))
colors = ['b', 'r', 'g']
plt.title('mean radius vs mean texture')
plt.xlabel(data.feature_names[2])
plt.ylabel(data.feature_names[3])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:, [0, 1]].values
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for j in range(len(data.target_names)):
        coord = mch.Finishing(df, j, "mean radius",
                              "mean texture", "Target")
        coord.append(coord[0])
        xs, ys = zip(*coord)
        plt.plot(xs, ys, c=colors[j])
