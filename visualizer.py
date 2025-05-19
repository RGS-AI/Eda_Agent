import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_plot_dir(path="plots"):
    os.makedirs(path, exist_ok=True)

def plot_univariate(df, output_dir="plots/univariate"):
    create_plot_dir(output_dir)

    for col in df.columns:
        plt.figure(figsize=(6, 4))
        if df[col].dtype == 'object' or df[col].nunique() < 15:
            # Bar plot for categorical
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Bar plot of {col}')
        else:
            # Histogram for numeric
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f'Histogram of {col}')
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{col}_univariate.png")
        plt.close()

def plot_pie_charts(df, output_dir="plots/piecharts"):
    create_plot_dir(output_dir)
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].nunique() < 10:
            plt.figure(figsize=(6, 6))
            df[col].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
            plt.title(f'Pie Chart of {col}')
            plt.ylabel("")
            plt.tight_layout()
            plt.savefig(f"{output_dir}/{col}_pie.png")
            plt.close()

def plot_boxplots(df, output_dir="plots/boxplots"):
    create_plot_dir(output_dir)
    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.tight_layout()
        plt.savefig(f"{output_dir}/{col}_box.png")
        plt.close()

def plot_bivariate(df, output_dir="plots/bivariate"):
    create_plot_dir(output_dir)
    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include='object').columns

    for cat in cat_cols:
        for num in num_cols:
            if df[cat].nunique() < 15:
                plt.figure(figsize=(8, 4))
                sns.boxplot(x=cat, y=num, data=df)
                plt.title(f'{num} by {cat}')
                plt.tight_layout()
                plt.savefig(f"{output_dir}/{num}_by_{cat}_box.png")
                plt.close()

def plot_pairplot(df, output_path="plots/multivariate/pairplot.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    num_df = df.select_dtypes(include='number')
    if num_df.shape[1] < 2:
        return
    sns.pairplot(num_df.dropna())
    plt.savefig(output_path)
    plt.close()

def plot_correlation_heatmap(df, output_path="plots/multivariate/corr_heatmap.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    corr = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def run_all_plots(df):
    plot_univariate(df)
    plot_pie_charts(df)
    plot_boxplots(df)
    plot_bivariate(df)
    plot_correlation_heatmap(df)
    plot_pairplot(df)