from rich.panel import Panel

from Importacao_dados import importar_dados
from Formatacao import console, numero_br

def mostrar_resumo(df):
    total_registros = len(df)
    total_compras = df["CO_ID"].nunique()
    total_clientes = df["CL_ID"].nunique()
    total_mulheres = df["CL_GENERO"].len == "F"
    total_homens = df["CL_GENERO"].len == "M"
    total_casados = df["CL_EC"].len == "1"
    total_divorciados =df["CL_EC"].len == "2"
    total_separado = df["CL_EC"].len == "3"
    total_solteiro = df["CL_EC"].len == "4"
    total_viuvo = df["CL_EC"].len == "5"
    media_filhos = 
    total_classe_a = 
    total_classe_b = 
    total_classe_c = 
    ?
    ?
    ?