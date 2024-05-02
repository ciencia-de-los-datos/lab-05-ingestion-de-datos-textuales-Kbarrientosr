"""GitHub Classroom autograding script."""

import os.path

import pandas as pd

if not os.path.exists("train_dataset.csv"):
    raise FileNotFoundError("File 'train_dataset.csv' not found")

train_dataset = pd.read_csv("train_dataset.csv")

assert train_dataset.columns[0] == "phrase"
assert train_dataset.columns[1] == "sentiment"

counts = train_dataset["sentiment"].value_counts()

assert counts["neutral"] == 1117
assert counts["positive"] == 458
assert counts["negative"] == 236


if not os.path.exists("test_dataset.csv"):
    raise FileNotFoundError("File 'test_dataset.csv' not found")

test_dataset = pd.read_csv("test_dataset.csv")

counts = test_dataset["sentiment"].value_counts()

assert counts["neutral"] == 274
assert counts["positive"] == 112
assert counts["negative"] == 67
