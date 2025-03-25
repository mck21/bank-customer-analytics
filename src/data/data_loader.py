import pandas as pd
import numpy as np

def load_customer_data():
    """
    Carga los datos de clientes desde el archivo Excel
    """
    try:
        df_customers = pd.read_excel('../data/customer-details.xlsx')
        return df_customers
    except Exception as e:
        print(f"Error al cargar datos de clientes: {e}")
        return None

def load_bank_data():
    """
    Carga los datos bancarios desde el archivo CSV
    """
    try:
        df_bank = pd.read_csv('../data/bank-additional.csv', sep=',', index_col=0)
        return df_bank
    except Exception as e:
        print(f"Error al cargar datos bancarios: {e}")
        return None

def get_basic_info(df):
    """
    Obtiene información básica del DataFrame
    """
    print("\nInformación del DataFrame:")
    print(df.info())
    print("\nPrimeras 5 filas:")
    print(df.head())
    print("\nEstadísticas descriptivas:")
    print(df.describe())
    print("\nValores nulos:")
    print(df.isnull().sum()) 