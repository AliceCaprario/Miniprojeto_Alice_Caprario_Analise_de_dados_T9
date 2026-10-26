#Importando dados do Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

import os
from datetime import datetime
import pandas as pd

#Ler o arquivo csv

CAMINHO_CSV = "Base_varejo.csv"

PASTA = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV_ORIGINAL = os.path.join(PASTA, "Base_varejo_original.csv")  
CAMINHO_CSV = os.path.join(PASTA, "Base_varejo.csv")

def importar_dados ():
    df = pd.read_csv(CAMINHO_CSV_ORIGINAL, sep=";")
    df["DATA"] = df["DATA"].map(
        lambda data: datetime.strptime(data, "%d/%m/%Y")
    )
    return df

if __name__ == "__main__":
    df = importar_dados()
    print (f"{len(df)} registros carregados")
    print(df.head())
