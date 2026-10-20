#Importando dados do Kaggle: https://www.kaggle.com/datasets/namespaiva/base-varejo/data

import pandas as pd
import rich

#Ler o arquivo csv

CAMINHO_CSV = "Base_varejo.csv"

def importar_dados ():
    df = pd.read_csv(CAMINHO_CSV)
    return df

if __name__ == "__main__":
    df = importar_dados()
    print(df.head())