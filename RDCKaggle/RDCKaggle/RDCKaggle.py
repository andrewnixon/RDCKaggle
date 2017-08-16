import math
import helperfunctions

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer

DATA_DIRECTORY = 'C:\\Users\\Andrew\\repos\\RDCKaggle\\Data\\'
train_variants_df = pd.read_csv(DATA_DIRECTORY + "training_variants")
test_variants_df = pd.read_csv(DATA_DIRECTORY + "test_variants")
train_text_df = pd.read_csv(DATA_DIRECTORY + "training_text", sep="\|\|", engine="python", skiprows=1, names=["ID", "Text"])
test_text_df = pd.read_csv(DATA_DIRECTORY + "test_text", sep="\|\|", engine="python", skiprows=1, names=["ID", "Text"])

def plot_classes():
    plt.figure(figsize=(12,8))
    sns.countplot(x="Class", data=train_variants_df, palette="Blues_d")
    plt.ylabel('Frequency', fontsize=14)
    plt.xlabel('Class', fontsize=14)
    plt.title("Distribution of genetic mutation classes", fontsize=18)
    plt.show()

def plot_gene_by_class():
    fig, axs = plt.subplots(ncols=3, nrows=3, figsize=(12,12))

    for i in range(3):
        for j in range(3):
            gene_count_grp = train_variants_df[train_variants_df["Class"]==((i*3+j)+1)].groupby('Gene')["ID"].count().reset_index()
            sorted_gene_group = gene_count_grp.sort_values('ID', ascending=False)
            sorted_gene_group_top_7 = sorted_gene_group[:7]
            sns.barplot(x="Gene", y="ID", data=sorted_gene_group_top_7, ax=axs[i][j])

    plt.show()

def print_varient_data():
    print("Train Variant".ljust(15), train_variants_df.shape)
    print("Train Text".ljust(15), train_text_df.shape)
    print("Test Variant".ljust(15), test_variants_df.shape)
    print("Test Text".ljust(15), test_text_df.shape)

    print(train_variants_df.head())

    print("For training data, there are a total of:")
    print("IDs: ", len(train_variants_df.ID.unique()))
    print("unique genes: ", len(train_variants_df.Gene.unique()))
    print("unique variations :", len(train_variants_df.Variation.unique()))
    print("classes: ", len(train_variants_df.Class.unique()))

    gene_group = train_variants_df.groupby("Gene")['Gene'].count()
    minimal_occ_genes = gene_group.sort_values(ascending=True)[:10]
    print("Genes with maximal occurences\n", gene_group.sort_values(ascending=False)[:10])
    print("\nGenes with minimal occurences\n", minimal_occ_genes)


def main():
    #print_varient_data()
    #plot_classes()
    #plot_gene_by_class()

if __name__ == "__main__":
    main()