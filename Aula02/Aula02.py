#Estruturas condicionais
#IF / ELSE / ELIF

#SE FIZER SOL
#   VOU À PRAIA
#SENÃO
#   FICO EM CASA

#SE FIZER SOL
#   VOU À PRAIA
#SENÃO SE TIVER MATE GELADO
#   VOU À PRAIA
#SENÃO
#   FICO EM CASA

#SE = IF. SENÃO = ELSE. SENÃO SE = ELIF

#EXERCÍCIO 2
#O seu gestor te solicitou a criação de uma programa, onde seja possível somar 5% de bônus
#ao salário do/a vendedor/a, quando ele/a atingir ou superar a meta em 105%
#Suponha que:
#Vendedora: Maria
#-Vendeu: R$ 1700
#-Meta: R$ 1600
#-Salário base: R$ 5400

#Sabendo das seguintes regras:
#Atingimento = (valor vendido/meta)*100
#Bonus = salario base*(5/100)
#Salario final = Salario base + bonus

#Exemplo atingindo a meta!
#Variáveis
vendedora = "Maria"
valor_vendido = 1700
meta = 1600
salario_base = 5400
bonus = 5

#cálculo do aingimento da meta
atingimento_meta = (valor_vendido/meta)*100

if (atingimento_meta >= 105):
    bonus_realizado = salario_base*(bonus/100)
    salario_final = salario_base + bonus_realizado
    print("Nome:",vendedora)
    print("Atingimento:",atingimento_meta)
    print("Salário base:",salario_base)
    print("Bônus:",bonus_realizado)
    print("Salário final:",salario_final)
else:
    print(vendedora,"não atingiu a meta!")

#Exemplo NÃO atingindo a meta!
#Variáveis
vendedora = "Maria"
valor_vendido = 1500
meta = 1600
salario_base = 5400
bonus = 5

#cálculo do aingimento da meta
atingimento_meta = (valor_vendido/meta)*100

if (atingimento_meta >= 105):
    bonus_realizado = salario_base*(bonus/100)
    salario_final = salario_base + bonus_realizado
    print("Nome:",vendedora)
    print("Atingimento:",atingimento_meta)
    print("Salário base:",salario_base)
    print("Bônus:",bonus_realizado)
    print("Salário final:",salario_final)
else:
    print(vendedora,"não atingiu a meta! Seu atingimento foi de:",atingimento_meta)

#Operadores Lógicos
#AND (E) - Todas as condições precisam ser verdadeiras, para retornar verdadeiro.
#Se apenas 1 condição for falsa. O teste lógico será falso
#Ex.: 
#Se fizer sol E tiver mate gelado (Se um das condições for Falsa, vai para o senão)
#   vou à praia (TODAS as condições precisam ser verdadeiras, para retornar verdadeiro)
#senão
#    fico em casa

#OR (ou) - Se apenas 1 condição for verdadeira, o teste lógico retornará verdadeiro.
#Para o teste lógico retornar falso, TODAS as condições precisam ser falsas.
#Ex.: 
#Se fizer sol OU tiver mate gelado (TODAS as condições precisam ser Falsa, para ir ao senão)
#   vou à praia (Basta 1 condiçaão ser verdadeira, para retornar verdadeiro)
#senão
#    fico em casa

#NOT - Inverte o resultado do AND e do OR

#EXERCÍCIO 3
#Ajustando o EXERCÍCIO 1, utilizando a estrutura condicional e operadores lógicos

#RELEMBRANDO AS REGRAS DO EXERCÍCIO 1
#AS regras para identificar o melhor custo-benefício são:
# 1 - Litro do leite tem que ser inferior a R$ 7,00
# 2 - Prazo de validade tem que ser superior a 6 meses

#Criar variáveis do custo-benefício
litro = 7
validade = 6

#Validar os dados da Empresa 1
litro_empresa1 = 7.5
validade_empresa1 = 12

#Validar os dados da Empresa 2
litro_empresa2 = 6.99
validade_empresa2 = 7

#Validar os dados da Empresa 3
litro_empresa3 = 6
validade_empresa3 = 3

if (litro_empresa1<litro and validade_empresa1>validade): #Verificando Empresa 1
    print("Empresa 1 é a vencedora! Litro:", litro_empresa1,"Validade:",validade_empresa1)
elif (litro_empresa2<litro and validade_empresa2>validade): #Verificando Empresa 2
    print("Empresa 2 é a vencedora! Litro:", litro_empresa2,"Validade:",validade_empresa2)
elif (litro_empresa3<litro and validade_empresa3>validade): #Verificando Empresa 3
    print("Empresa 3 é a vencedora! Litro:", litro_empresa3,"Validade:",validade_empresa3)
else:
    print("Nenhuma empresa atendeu as condições exigidas!")

#Interação dos/as usuários/as com o seu script(INPUT)
#A FUNÇÃO INPUT oferece a possibilidade dos/as usuários/as interagirem com o seu script
#informando seus próprios dados. É possível inserir dados de texto, número inteiro e decimal
#O padrão da FUNÇÃO input é receber dados de texto, portanto se for necessário a inserção
#de dados numéricos, nós vamos utilizar os seguintes aninhamentos de função ao input:

#Exemplo:
#input("Qual seu nome?")

#Exemplo número inteiro (aninhar com a função int)
#int(input("Qual sua idade?"))

#Exemplo número decimal (aninhar com a função float)
#float(input("Qual o seu tamanho?"))

#EXERCÍCIO 4 - AJUSTANDO O EXERCÍCIO 3, PARA SOLICITAR OS VALORES DAS EMPRESAS!
#Solicitando informações das concorrentes
nome_concorrente = input("Nome da concorrente:")
litro_concorrente = float(input("Valor do litro(R$):"))
validade_concorrente = int(input("Validade e meses:"))

if (litro_concorrente < litro and validade_concorrente > validade):
    print(nome_concorrente,"atende aos requisitos de compra! Litro:",litro_concorrente,"Validade:",validade_concorrente,"meses.")
else:
    print(nome_concorrente,"NÃO atendeu as condições exigidas!")

#Armazendo dados inseridos pelo/a usuário/a
#Usando mais um tipo de variável!
#Variável LISTA

#A lista ela é delimitada pelos sinais de "[" e "]" e todos os elementos pertencentes
#a lista, estarõ separados por vírgula. Os valores armazenados em uma lista podem (e devem)
#ser manipulados, utilizando MÉTODOS específicos da lista
#As listas são úteis para armazenar vários dados em uma única variável. Uma lista pode
#armazenar diversos tipos de dados, como textos e números, porém a boa prática é
#criar uma lista para cada tipo de entrada, de forma a categorizar o dado.

#EXERCÍCIO 5 - AJUSTANDO o EXERCÍCIO 4, PARA ARMAZENAR OS VALORES INSERIDOS
#Para utilizar um lista, ela precisa ser criada vazia

#Criando listas - É EXECUTADA SOMENTE UMA VEZ!!!
#concorrentes que atendem
lista_concorrentes_atendem = []
lista_litro_atendem = []
lista_validade_atendem = []

#concorrentes que NÃO atendem
lista_concorrentes_nao_atendem = []
lista_litro_nao_atendem = []
lista_validade_nao_atendem = []
#FIM DA CRIAÇÃO DAS LISTAS

nome_concorrente = input("Nome da concorrente:")
litro_concorrente = float(input("Valor do litro(R$):"))
validade_concorrente = int(input("Validade e meses:"))

if (litro_concorrente < litro and validade_concorrente > validade):
    print(nome_concorrente,"atende aos requisitos de compra! Litro:",litro_concorrente,"Validade:",validade_concorrente,"meses.")
    lista_concorrentes_atendem.append(nome_concorrente)
    lista_litro_atendem.append(litro_concorrente)
    lista_validade_atendem.append(validade_concorrente)
else:
    print(nome_concorrente,"NÃO atendeu as condições exigidas!")
    lista_concorrentes_nao_atendem.append(nome_concorrente)
    lista_litro_nao_atendem.append(litro_concorrente)
    lista_validade_nao_atendem.append(validade_concorrente) 

print("Registro dos dados das concorrentes que atedem aos requisitos!")
print("Concorrentes:", lista_concorrentes_atendem)
print("Valor do litro(R$):",lista_litro_atendem)
print("Validade em meses:", lista_validade_atendem)
print("---")
print("Registro dos dados das concorrentes que NÃO atedem aos requisitos!")
print("Concorrentes:", lista_concorrentes_nao_atendem)
print("Valor do litro(R$):",lista_litro_nao_atendem)
print("Validade em meses:", lista_validade_nao_atendem)


#Manipulando dados nas listas
#Remover os dados da Empresa 7, de suas listas
#Removendo nome
lista_concorrentes_atendem.pop(2)
#Removendo litro
lista_litro_atendem.pop(2)
#removendo validade
lista_validade_atendem.pop(2)
#Alterando valor do litro
lista_litro_atendem[1]=6

#EXERCÍCIO 6 - VERIFICANDO QUAL A MELHOR EMPRESA, DENTRE TODAS AS EMPRESA QUE ATENDEM
#PARA CENÁRIOS COMO ESTE, SEGUIR AS REGRAS:
#SOMAR VALOR DO LITRO + VALIDADE. 
#A EMPRESA ESCOLHIDA SERÁ A QUE TIVER O MENOR VALOR

valida_empresa1 = lista_litro_atendem[0]+lista_validade_atendem[0]
valida_empresa3 = lista_litro_atendem[1]+lista_validade_atendem[1]

if (valida_empresa1 < valida_empresa3):
    print(lista_concorrentes_atendem[0],"é a vencedora! Preço:",lista_litro_atendem[0],"e validade de",lista_validade_atendem[0],"meses!")
else:
    print(lista_concorrentes_atendem[1],"é a vencedora! Preço:",lista_litro_atendem[1],"e validade de",lista_validade_atendem[1],"meses!")