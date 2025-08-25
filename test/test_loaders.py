import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.loaders import load_sample_dataset
import pandas as pd
import io

def test_load_sample_dataset():
    csv = io.StringIO("time,flux\n0,1.0\n1,0.98\n2,0.95")
    df = load_sample_dataset(csv)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["time", "flux"]
