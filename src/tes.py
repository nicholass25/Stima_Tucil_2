# %%
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data,
                  columns=data.feature_names)

# Convert the whole dataframe as a string and display
display(df.to_string())

# %%
