
import pandas as pd

# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
# A mensagem "Reprovado", se a média for menor do que 7;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota = float(input("Digite a nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota + nota2)/2
if media == 10:
    print("Aprovado com Distinção")

elif media >= 7:
    print("Aprovado")

else:
    print("Reprovado")


# Escreva um script que leia três números e mostre o maior e o menor deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


numeros = [num1, num2, num3]

print(f"Maior {max(numeros)}, \nMenor: {min(numeros)}")

# Nome na vertical em escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input("Digite o nome: ")
nome = nome.upper()
for i in range(len(nome)+1):
    print(nome[:i])

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro, é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).


numero = int(input("Digite a quantidade: "))

value = [1,1]
for x in range(2, numero):

    value.append(value[x-2] + value[x-1])

print(value)



# Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';


nome = input("Digite o nome: ")
if len(nome) > 3:
    print("Nome aceito")

elif len(nome) > 30:
    print("Nome muito grande")

else:
    print("Nome não aceito")

idade = int(input("Digite a idade: "))
if idade >= 0 and idade <= 150:
    print("Idade aceita")
else:
    print("Idade não aceita")


salario = float(input("Digite o salário: R$ "))
if salario > 0:
    print("Salário aceito")

else:
    print("Salário não aceito")

sexo = input("Digite o sexo: (m) ou (f)")
sexo.lower()
if sexo == 'f' or sexo == 'm':
    print("Sexo aceito")

else:
    print("Sexo não aceito")

# Estado Civil: 's', 'c', 'v', 'd';
estado_civil = input("Digite o estado civil: \n(s) - (c) - (v) ou (d): ")
estado_civil.lower()
if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
    print("Estado civil aceito")

else:
    print("Estado civil não aceito")


# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.

numero = int(input("Digite um número: "))

if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"{numero} não é um número primo")

        else:
            print(f"{numero} é um número primo")

else:
    print(f"{numero} não é um número primo")

