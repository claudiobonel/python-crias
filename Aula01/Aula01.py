#Primeiro código em Python
print("Hello World!")

#Variáveis
#Tipos de variáveis
#Número Inteiro
numero_inteiro = 5
print(numero_inteiro) 

#Texto (String)
texto = "Aula 1 - Básico do báscio de Python"
print(texto)

#Número decimal
numero_decimal = 0.5
print(numero_decimal)

#Forma ERRADA de se utilizar o número decimal
numero_decimal_errado = 0,5
print(numero_decimal_errado)

#Lógica (Boolean). PT-BR - Boleana
#Operadores de comparação
# == Igual. Exemplo.: 15 == 20 (15 é igual a 20?)
# > Maior que. Exemplo: 15 > 10 (15 é maior que 10?)
# >= Maior ou igual que. Exemplo: 15 >= 15 (15 é maior ou igual a 15?)
# < Menor que. Exemplo: 15 < 15 (15 é menor que 15?)
# <= Menor ou igual que. Exemplo: 15 <= 15 (15 é menor ou igual a 15?)
# != Diferente. Exemplo: 15 != 15 (15 é diferente de 15?)

valor = 15 > 15
print(valor)

valor = 15 >= 15
print(valor)

#Exercício 1 - Cotação do dólar
cotacao_dolar_14092022 = 5.17
cotacao_alvo = 5.04
valida_cotacao = cotacao_dolar_14092022 < cotacao_alvo
print("A cotação do dólar é menor que R$5,04?",valida_cotacao,". O valor atual é de R$",cotacao_dolar_14092022)

#Funções e Métodos
#exemplo de função
print("print é uma função!")

#exemplo de método
texto = texto.replace("báscio","básico")
print(texto)

texto = texto.upper()
print(texto)

texto_inicial = texto[:6]
print(texto_inicial)

texto_final = texto[-9:]
print(texto_final)

texto_meio = texto[9:25]
print(texto_meio)

#EXERCÍCIO 1
#Imagine que vc seja o/a comprador/a da sua empresa e, durante a licitação vc precisa avaliar alguns pontos
#para que vc possa realizar a compra com o melhor custo-benefício
#Neste momento vc está gerenciando uma licitação de compra de leite e, as regras
#para identificar o melhor custo-benefício são:
# 1 - Litro do leite tem que ser inferior a R$ 7,00
# 2 - Prazo de validade tem que ser superior a 6 meses

#Suponha que vc recebeu as seguintes propostas comerciais
#Empresa 1:
#Litro: R$ 7,50
#Validade: 12 meses

#Empresa 2:
#Litro: R$ 6,99
#Validade: 3 meses

#Empresa 3:
#Litro: R$ 6,00
#Validade: 3 meses

#Desenvolver um pequeno algorítmo, onde seja possível identificar a Empresa vencedora.
#Sabendo que, os seus testes lógicos precisam retornar como "Verdadeiro", para ambos (Litro e Validade)

#Criar variáveis do custo-benefício
litro = 7
validade = 6

#Validar os dados da Empresa 1
litro_empresa1 = 7.5
validade_empresa1 = 12

#Validando custo-benefício Empresa 1
valida_litro_empresa1 = litro_empresa1 < litro
valida_validade_empresa1 = validade_empresa1 > validade

#Exibir resultados
print("Litro Empresa 1:",valida_litro_empresa1)
print("Validade Empresa 1:", valida_validade_empresa1)

#Validar os dados da Empresa 2
litro_empresa2 = 6.99
validade_empresa2 = 7

#Validando custo-benefício Empresa 2
valida_litro_empresa2 = litro_empresa2 < litro
valida_validade_empresa2 = validade_empresa2 > validade

#Exibir resultados
print("Litro Empresa 2:",valida_litro_empresa2)
print("Validade Empresa 2:", valida_validade_empresa2)

#Validar os dados da Empresa 3
litro_empresa3 = 6
validade_empresa3 = 3

#Validando custo-benefício Empresa 3
valida_litro_empresa3 = litro_empresa3 < litro
valida_validade_empresa3 = validade_empresa3 > validade

#Exibir resultados
print("Litro Empresa 3:",valida_litro_empresa3)
print("Validade Empresa 3:", valida_validade_empresa3)

#Exibir o Resultado Final
print("A Empresa vencedora da Licitação é a Empresa 2, com preço do litro de R$",litro_empresa2,"e a validade de",validade_empresa2,"meses.")