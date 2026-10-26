import pandas as pd
from rich.panel import Panel

from Importacao_dados import importar_dados
from Formatacao import console, numero_br

def mostrar_resumo(df):
    contagem_por_data = df["DATA"].value_counts()
    dias_com_mais_compras = ", ".join(                         #Feito o join para caso haja mais de um dia com mais compras (empate), todos sejam exibidas
        contagem_por_data[contagem_por_data == contagem_por_data.max()]
        .index.strftime("%d/%m/%Y")
    )
    total_registros = len(df)
    total_compras = df["CO_ID"].nunique()
    total_clientes = df["CL_ID"].nunique()
    total_mulheres = df.loc[df["CL_GENERO"] == "F", "CL_ID"].nunique()
    total_homens = df.loc[df["CL_GENERO"] == "M", "CL_ID"].nunique()
    total_casados = df.loc[df["CL_EC"] == 1, "CL_ID"].nunique()
    total_divorciados =df.loc[df["CL_EC"] == 2, "CL_ID"].nunique()
    total_separado = df.loc[df["CL_EC"] == 3, "CL_ID"].nunique()
    total_solteiro = df.loc[df["CL_EC"] == 4, "CL_ID"].nunique()
    total_viuvo = df.loc[df["CL_EC"] == 5, "CL_ID"].nunique()
    compras_mais_recentes = (                                       #Filtrando as compras mais recentes de cada cliente, pois ele pode ter tido mais filhos 
        df.assign(DATA=pd.to_datetime(df["DATA"], dayfirst=True))
        .sort_values("DATA")
        .drop_duplicates(subset="CL_ID", keep="last")
    )
    media_filhos = compras_mais_recentes["CL_FHL"].mean()
    total_classe_a = df.loc[df["CL_SEG"] == "A", "CL_ID"].nunique()
    total_classe_b = df.loc[df["CL_SEG"] == "B", "CL_ID"].nunique()
    total_classe_c = df.loc[df["CL_SEG"] == "C", "CL_ID"].nunique()
    categorias_mais_compradas = ", ".join(df["PR_CAT"].mode().astype(str))   #Feito o join para caso haja mais de uma categoria mais comprada (empate), todas sejam exibidas
    contagem_produtos = df.groupby(["PR_ID", "PR_NOME"]).size()
    maior_contagem_produto = contagem_produtos.max()
    produtos_mais_comprados = ", ".join(
        f"SKU {sku} - {nome} ({numero_br(maior_contagem_produto)} unidades)"
        for sku, nome in contagem_produtos[
            contagem_produtos == maior_contagem_produto
        ].index
    )

    texto =(
        f"[bold] Dia(s) com mais compras: [/] {dias_com_mais_compras}\n"
        f"[bold] Total de registros: [/] {numero_br(total_registros)}\n"
        f"[bold] Total de compras: [/] {numero_br(total_compras)}\n"
        f"[bold] Total de clientes: [/] {numero_br(total_clientes)}\n"
        f"[bold] Total de mulheres: [/] {numero_br(total_mulheres)}\n"
        f"[bold] Total de homens: [/] {numero_br(total_homens)}\n"
        f"[bold] Total de casados(as): [/] {numero_br(total_casados)}\n"
        f"[bold] Total de divorciados(as): [/] {numero_br(total_divorciados)}\n"
        f"[bold] Total de separados(as): [/] {numero_br(total_separado)}\n"
        f"[bold] Total de solteiros(as): [/] {numero_br(total_solteiro)}\n"
        f"[bold] Total de viúvos(as): [/] {numero_br(total_viuvo)}\n"
        f"[bold] Média de filhos: [/] {numero_br(media_filhos)}\n"
        f"[bold] Total de clientes classe A: [/] {numero_br(total_classe_a)}\n"
        f"[bold] Total de clientes classe B: [/] {numero_br(total_classe_b)}\n"
        f"[bold] Total de clientes classe C: [/] {numero_br(total_classe_c)}\n"
        f"[bold] Categoria(s) mais comprada(s): [/] {categorias_mais_compradas}\n"
        f"[bold] Produto(s) mais comprado(s): [/] {produtos_mais_comprados}\n"
    )

    console.print(Panel(texto, title="Resumo varejo:", expand=False))

if __name__ == "__main__":
    df = importar_dados()
    mostrar_resumo(df)

    