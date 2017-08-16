import math
import helperfunctions

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer

DATA_DIRECTORY = 'C:\\Users\\Andrew\\repos\\RDCKaggle\\Data\\'

def main():
    train_variants_df = pd.read_csv(DATA_DIRECTORY + "training_variants")
    test_variants_df = pd.read_csv(DATA_DIRECTORY + "test_variants")
    train_text_df = pd.read_csv(DATA_DIRECTORY + "training_text", sep="\|\|", engine="python", skiprows=1, names=["ID", "Text"])
    test_text_df = pd.read_csv(DATA_DIRECTORY + "test_text", sep="\|\|", engine="python", skiprows=1, names=["ID", "Text"])
    
    print("Train Variant".ljust(15), train_variants_df.shape)
    print("Train Text".ljust(15), train_text_df.shape)
    print("Test Variant".ljust(15), test_variants_df.shape)
    print("Test Text".ljust(15), test_text_df.shape)

    print(train_variants_df.head())

if __name__ == "__main__":
    main()