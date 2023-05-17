import os
import pandas as pd
import zipfile


def load_data(path):
    df = pd.read_csv(path, sep='\t', header=None)
    return df