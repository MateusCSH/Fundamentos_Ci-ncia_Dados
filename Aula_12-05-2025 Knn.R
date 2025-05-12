
######################
# Preparação dos dados
######################

# Removendo o atributo id
dados = dados[-1]


# Remover a coluna "bugada"
dados = dados[-32]



# Analisando a coluna de diagnóstico

table(dados$diagnosis)


# Códificando a variável como fator

dados$diagnosis = factor(dados$diagnosis,
                         levels = c('B','M'),
                         labels = c('Benigno','Maligno'))



#criando uma funçã que normaliza


normaliza = function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}


# Testando a função criada
normaliza(c(1,2,3,4))

# Normalizando os dados numéricos

dados_n = as.data.frame(lapply(dados[2:31], normaliza)) #Pega cada coluna e aplica a função, normalizando todos.


# Separando dados de treino e teste

dados_treino = dados_n[1:469,]
dados_teste = dados_n[470:569,]

# Separando rótulos

dados_treino_rotulos = dados[1:469, 1]
dados_teste_rotulos = dados[470:569, 1]


###############
# Aplicação do KNn para classificação de células em tumor benigno ou maligno
###############
# Instalando e carregando o pacote Class

install.packages("class")
library(class)

dados_pred = knn(train = dados_treino, 
                 test = dados_teste,
                 cl = dados_treino_rotulos,
                 k = 21)
