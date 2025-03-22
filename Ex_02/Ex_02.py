

# Exercício 1
# - Crie uma variável chamada nome e atribua o seu nome a ela.
# - Crie uma variável chamada idade e atribua sua idade a ela.
# - Crie uma variável chamada altura e atribua sua altura (em metros) a ela.
# - Mostre na tela a concatenação das informações: "Meu nome é [nome], tenho [idade] anos e
# minha altura é [altura] metros."

nome = 'Mateus Cristian'
idade = 22
altura = 1.76
print(f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura}")


# Exercício 2
# Crie uma variável chamada frase e atribua a seguinte frase a ela:
# "Python é uma linguagem de programação muito poderosa."
# - Utilize o método .upper() para transformar toda a frase em maiúsculas e imprima o
# resultado.
# - Utilize o método .lower() para transformar toda a frase em minúsculas e imprima o
# resultado.
# - Utilize o método .replace() para substituir a palavra "muito" por "extremamente". Imprima o
# resultado.
# - Utilize o método .split() para dividir a frase em palavras e imprima o resultado como uma
# lista

frase = """Python é uma linguagem de programação muito poderosa"""
print(frase.upper())
print(frase.lower())
print(frase.replace("muito", "extremamente"))
print(frase.split(' '))



#Exercício 3
# - Crie uma lista chamada frutas contendo os seguintes itens: "maçã", "banana", "laranja",
# "uva", "abacaxi".
# - Imprima a lista frutas.
# - Adicione o item "manga" à lista frutas utilizando o método .append() e imprima a lista
# novamente.
# - Remova o item "laranja" da lista frutas utilizando o método .remove() e imprima a lista.
# - Acesse o terceiro item da lista frutas (lembrando que as listas começam em 0) e imprima-o.
# - Ordene a lista frutas em ordem alfabética utilizando o método .sort() e imprima a lista.
# - Crie uma lista chamada numeros com os valores [10, 5, 8, 3, 6]. Utilize a função sum() para
# calcular a soma de todos os elementos dessa lista e imprima o resultado.

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
print(frutas)
frutas.append("manga")
print(frutas)
frutas.remove("laranja")
print(frutas)
print(frutas[2])
print(sorted(frutas))
numeros = [10, 5, 8, 3, 6]
print(sum(numeros))


# Exercício 4
# - Crie um dicionário chamado pessoa com as seguintes chaves e valores:
# "nome": "Carlos"
# "idade": 30
# "cidade": "São Paulo"
# - Imprima o dicionário pessoa.
# - Acesse e imprima o valor associado à chave "nome".
# - Altere a idade de "Carlos" para 31 e imprima o dicionário novamente.
# - Adicione uma nova chave "profissão" ao dicionário com o valor "engenheiro". Imprima o
# dicionário atualizado.
# - Remova a chave "cidade" do dicionário e imprima o dicionário após a remoção.
# - Utilize o método .keys() para imprimir todas as chaves do dicionário.
# - Utilize o método .values() para imprimir todos os valores do dicionário.


pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo",
}
print(pessoa["nome"])
pessoa["idade"] = 31
print(pessoa["idade"])
pessoa["profissão"] = "engenheiro"
print(pessoa)
del pessoa["cidade"]
print(pessoa)
print(pessoa.keys())
print(pessoa.values())


# Exercício 6
# Crie um programa que receba a altura e o peso de uma pessoa e imprima seu IMC.

height = float(input('Digite a altua: '))
weight = float(input('Digite sua massa: '))

imc = weight / (height**2)

print(f'IMC: {imc:.2f}')



#Exercício 7
# Escreva um programa que pergunte o nome completo do usuário e o cumprimente pelo
# primeiro nome.

nome = str(input('Digite seu nome: '))
firts_name = nome.split()[0]
print(f'Olá: {firts_name}')

# Exercício 8
# Escreva um código que extraia o domínio de um e-mail informado.

email = str(input('Digite seu email: '))
dominio = email.split('@')
print(f'Seu domínio é: {dominio[1]}')
