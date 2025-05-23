import duckdb
import os
import pandas as pd

# Define o caminho base do projeto (pasta acima do arquivo atual)
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define os caminhos dos arquivos (dinâmico e portátil)
csv_compras = os.path.join(base_dir, "dados", "compras.csv")
sql_path = os.path.join(base_dir, "transformacoes", "transformar.sql")
saida_path = os.path.join(base_dir, "saida", "resultado.csv")

# Lê o CSV
df = pd.read_csv(csv_compras)

# Padroniza os nomes das colunas (sem acentos, minúsculas)
df.columns = [col.lower().replace("ç", "c").replace("ã", "a").replace("í", "i")
              .replace("ú", "u").replace("é", "e").replace("á", "a") for col in df.columns]

# Salva o CSV padronizado (sobrescreve o original)
df.to_csv(csv_compras, index=False)

# Conecta ao DuckDB
con = duckdb.connect()

# Lê o conteúdo do SQL
with open(sql_path, "r", encoding="utf-8") as f:
    query = f.read()

# Executa a consulta passando o caminho do CSV como parâmetro
resultado = con.execute(query, {"caminho_compras": csv_compras}).fetchdf()

# Exporta o resultado para CSV
resultado.to_csv(saida_path, index=False)

print("✅ Consulta concluída com sucesso!")
print("📄 Resultado salvo em:", saida_path)
