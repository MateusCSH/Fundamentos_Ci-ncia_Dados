
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Ex_01/areas.csv", sep=";", decimal=',')

print(df.head(10))

# Qual o número total de apartamentos no empreendimento?

print(f'Quantidade de apartamentos: {len(df)}')

# Quantos apartamentos existem por bloco?

print(f'Quantidade de apartamento por bloco: \n{df.groupby(['Bloco'])['Id'].count()}')

# Quantos apartamentos existem por andar

print(f'Quantidade de apartamento por andar: \n{df.groupby(['Andar'])['Id'].count()}')


# Existe a suspeita de que os apartamentos tenham sido construídos com metragens diferentes. O arquivo de dados traz as áreas de cada cômodo em separado. Acrescente uma nova coluna  calculando a área útil total de cada apartamento.

df["Nova_metragem"] = df["Sala"] + df["Cozinha"] + df['Banheiro'] + df['Dorm']

print(f"Nova metragem: \n{df['Nova_metragem'].head(10)}")

# Para a área de cada cômodo e para a área útil total (isto é, para as variáveis quantitativas contínuas), faça um histograma.


# 3. Visualização de dados.
# Histograma para cada cômodo
plt.figure(figsize=(12, 8))

# SALA
plt.subplot(2, 3, 1)
plt.hist(df['Sala'], bins=10, color='blue', alpha=0.7)
plt.title('Histograma da Sala')
plt.xlabel('Área (m²)')
plt.ylabel('Frequência')

# COZINHA
plt.subplot(2, 3, 2)
plt.hist(df['Cozinha'], bins=10, color='green', alpha=0.7)
plt.title('Histograma da Cozinha')
plt.xlabel('Área (m²)')
plt.ylabel('Frequência')

# BANHEIRO
plt.subplot(2, 3, 3)
plt.hist(df['Banheiro'], bins=10, color='red', alpha=0.7)
plt.title('Histograma do Banheiro')
plt.xlabel('Área (m²)')
plt.ylabel('Frequência')

# DORMITÓRIO
plt.subplot(2, 3, 4)
plt.hist(df['Dorm'], bins=10, color='purple', alpha=0.7)
plt.title('Histograma do Dormitório')
plt.xlabel('Área (m²)')
plt.ylabel('Frequência')


plt.tight_layout()
plt.show()



# Agora, em separado para o bloco A e o bloco B: a. Calcule a média e o desvio-padrão da área de cada cômodo e também da área total.

BL_A = df[df['Bloco'] == "A"]
BL_B = df[df['Bloco'] == "B"]

# Bloco A
print(f"\nÁrea média e desvio-padrão para Sala do Bloco A")
print(f"Média: {BL_A['Sala'].mean()}\n Desvio padrão: {BL_A['Sala'].std():.2f}")


print(f"\nÁrea média e desvio-padrão para Cozinha do Bloco A")
print(f"Média: {BL_A['Cozinha'].mean()}\n Desvio padrão: {BL_A['Cozinha'].std():.2f}")



print(f"\nÁrea média e desvio-padrão para Banheiro do Bloco A")
print(f"Média: {BL_A['Banheiro'].mean()}\n Desvio padrão: {BL_A['Banheiro'].std():.2f}")



print(f"\nÁrea média e desvio-padrão para Dormitório do Bloco A")
print(f"Média: {BL_A['Dorm'].mean()}\n Desvio padrão: {BL_A['Dorm'].std():.2f}")

print("\nPara nova área total")
BL_A["Nova_metragem"] = BL_A["Sala"] + BL_A["Cozinha"] + BL_A["Banheiro"] + BL_A["Dorm"]
print(f"Média: {BL_A['Nova_metragem'].mean()}\n Desvio-padrão: {BL_A['Nova_metragem'].std()}")


# Bloco B
print(f"\nÁrea média e desvio-padrão para Sala do Bloco B")
print(f"Média: {BL_B['Sala'].mean()}\n Desvio padrão: {BL_B['Sala'].std():.2f}")


print(f"\nÁrea média e desvio-padrão para Cozinha do Bloco B")
print(f"Média: {BL_B['Cozinha'].mean()}\n Desvio padrão: {BL_B['Cozinha'].std():.2f}")



print(f"\nÁrea média e desvio-padrão para Banheiro do Bloco B")
print(f"Média: {BL_B['Banheiro'].mean()}\n Desvio padrão: {BL_B['Banheiro'].std():.2f}")



print(f"\nÁrea média e desvio-padrão para Dormitório do Bloco B")
print(f"Média: {BL_B['Dorm'].mean()}\n Desvio padrão: {BL_B['Dorm'].std():.2f}")

print("\nPara nova área total")
BL_B["Nova_metragem"] = BL_B["Sala"] + BL_B["Cozinha"] + BL_B["Banheiro"] + BL_B["Dorm"]
print(f"Média: {BL_B['Nova_metragem'].mean()}\n Desvio-padrão: {BL_B['Nova_metragem'].std()}")




# Construa boxplots e compare as áreas para cada cômodo considerado


dados = [BL_A['Sala'], BL_A['Cozinha'], BL_A['Banheiro'], BL_A['Dorm']]
plt.boxplot(dados, positions=[1,2,3,4],labels=['Sala', 'Cozinha', 'Banheiro','Dormitório'])

plt.show()



dados2 = [BL_B['Sala'], BL_B['Cozinha'], BL_B['Banheiro'], BL_B['Dorm']]
plt.boxplot(dados2, positions=[1,2,3,4],labels=['Sala', 'Cozinha', 'Banheiro','Dormitório'])

plt.show()


print(f"\n PARA DORMITÓRIO\nBloco A: {BL_A['Dorm'].max() - BL_A['Dorm'].min()}")
print(f"Bloco B: {BL_B['Dorm'].max() - BL_B['Dorm'].min()}")

print(f"\n PARA SALA\nBloco A: {BL_A['Sala'].max() - BL_A['Sala'].min():.2f}")
print(f"Bloco B: {BL_B['Sala'].max() - BL_B['Sala'].min():.2f}")

# Os que apresentam maior variação entre as áreas são Sala com cerca de 1.1m² e Dormitório com 0.8m².



# Agora vamos explorar os dados referentes a problemas estruturais (rachaduras e infiltrações).a. Construa tabelas de frequências e gráficos (barras ou pizza) para cada uma das duas variáveis

# Rachadura
qtd = df['Rachadura'].value_counts()
grafico = qtd.plot.bar(color=['lightseagreen', 'tomato'])
grafico.set_xticklabels(['Presente', 'Ausente'], rotation=0)
grafico.set_title('Frequência de Rachadura')
grafico.set_xlabel('Rachadura')
grafico.set_ylabel('Frequência')

plt.tight_layout()
plt.show()

# Infiltr
qtd = df['Infiltr'].value_counts()
grafico = qtd.plot.bar(color=['lightseagreen', 'tomato'])
grafico.set_xticklabels(['Presente', 'Ausente'], rotation=0)
grafico.set_title('Frequência de Infiltração')
grafico.set_xlabel('Infiltr')
grafico.set_ylabel('Frequência')

plt.tight_layout()
plt.show()
