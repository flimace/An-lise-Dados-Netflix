import pandas as pd

df = pd.read_csv('netflix_titles.csv')

# limpar valores nulos onde o titulo é nulo pois é esssencial pra análise.
df_limpo = df.dropna(subset=['title'])

# preencher valores nulos como "Não Informado" para colunas de director, cast e country pois são as que mais tem valor nulo!

colunas_para_preencher = ['director', 'country', 'cast', 'duration', 'rating', 'description', 'listed_in', 'date_added', 'release_year']
for coluna in colunas_para_preencher:
    df = df.fillna({coluna: 'Não Informado'})
    
# Garante que NADA na coluna duration saia vazio

# dividir os valores da coluna por virgula e espaço pra criar listas

df_limpo = df['country'].str.split(',').str[0]
df_limpo = df['country'].str.strip()

# passando o arquivo para o sql!! ^^
df.to_csv('netflix_limpoNOVO.csv', index=False, encoding='utf-8')

# # index=False: Não salva a coluna de numeração do Pandas (evita erro no SQL)
# # encoding='utf-8': Garante que acentos (ex: "Não Informado") não fiquem ilegíveis

print("Arquivo 'netflix_limpoNOVO.csv' gerado com sucesso!")

