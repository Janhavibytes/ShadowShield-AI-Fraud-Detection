import pandas as pd

df = pd.read_csv("../data/fraud.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nHead:\n", df.head())
print("\nClass distribution:\n", df["Class"].value_counts())