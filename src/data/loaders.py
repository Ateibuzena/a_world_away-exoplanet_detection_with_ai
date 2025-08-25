import pandas as pd

def load_sample_dataset(file):
    """Carga CSV de ejemplo con curvas de luz"""
    df = pd.read_csv(file)
    return df
