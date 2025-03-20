import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_distribution(data, column, title=None):
    """
    Crea un gráfico de distribución para una columna numérica
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=column, kde=True)
    plt.title(title or f'Distribución de {column}')
    plt.savefig(f'../../results/figures/distribution_{column}.png')
    plt.close()

def plot_correlation_matrix(data, title=None):
    """
    Crea una matriz de correlación para variables numéricas
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title(title or 'Matriz de Correlación')
    plt.tight_layout()
    plt.savefig('../../results/figures/correlation_matrix.png')
    plt.close()

def plot_categorical_counts(data, column, title=None):
    """
    Crea un gráfico de barras para contar categorías
    """
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar')
    plt.title(title or f'Conteo de {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'../../results/figures/counts_{column}.png')
    plt.close() 