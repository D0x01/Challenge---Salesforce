#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Login e Cadastro do usuario 
# Redefinnicao de senha para o portal
# Briefing 
# Gerar relatorio com dados do cliente para retorno
# /Users/daniel.magalhaes/Documents/logins/

# criacao do arquivo de armazenamento de registros
with open('/Users/daniel.magalhaes/Documents/logins/' + 'registrados.txt', 'w') as arquivo: 
    arquivo.write('Bem vindo ao relatório de registros: ')


# In[33]:


def login(): 
    login = input(str('Digite seu login: '))
    senha = input(str('Digite sua senha: '))
    
    login = login + senha
    
    with open('/Users/daniel.magalhaes/Documents/logins/registrados.txt', 'r') as arquivo: 
        check = arquivo.readlines()
        while not login in check:
            print('login nao encontrado!')
            break
        while login in check:
            print('login efetuado com sucesso')
            break


# In[32]:


def cadastro(): 
    print('Olá, vamos criar as credenciais de sua nova conta!')
    
    nome = input(str('Digite seu nome: '))
    
    print('''
    Voce é PJ ou PF? 
    1 - PJ
    2 - PF
    ''')
    n = input(str('Digite o numero que se identifica: '))
    
    if n == '1':
        entrada = input(str('Digite seu CNPJ: '))
        while len(entrada) < 14:
            print('Digite o CNPJ com 14 digitos corretamente!')
            entrada = input(str('Digite seu CNPJ: '))
            break
    elif n == '2':
        entrada = input(str('Digite seu CPf: '))
        while len(entrada) < 11:
            print('Digite o CNPJ com 11 digitos corretamente!')
            entrada = input(str('Digite seu CPF: '))
            break    

    senha = input(str('Defina sua senha: '))
    
    # validar senha
    valida_senha = input(str('Repita sua senha: '))

    if senha != valida_senha:

            print('As senhas nao coincidem!')
            definicao_senha()
    else:
            print(valida_senha)
            print('Senha valida!')
            
    cadastro = str(entrada + senha)
    
    check = str(entrada + senha)
    
    with open('/Users/daniel.magalhaes/Documents/logins/registrados.txt', 'r') as arquivo:
        while not cadastro in check:
            with open('/Users/daniel.magalhaes/Documents/logins/registrados.txt', 'w') as arquivo:
                arquivo.write(str(cadastro))
                print('Armazenado com sucesso')
        while cadastro in check:
            print('faça login!')
            break


# In[48]:


def briefing():
    print('Preencha o formulario abaixo para relacionarmos a melhor solucao a voce!')
    print('''
    Industria
    1 - Financeiro
    2 - Alimenticio
    3 - Textil
    ''')
    industria = input(str('Digite o numero referente a industria relacionada a seu negocio: '))
    if industria > '3':
        print('Digite uma opcao valida!')
    industria = input(str('Digite o numero referente a industria relacionada a seu negocio: '))
        
    
    print('''
    Porte (Faturamento mensal)
    1 - < 100k
    2 - 100k - 500k
    3 - > 500k 
    ''')
    porte = input(str('Digite o numero identificador do porte de seu negocio: '))
    if porte > '3':
        print('Digite uma opcao valida!')
    porte = input(str('Digite o numero identificador do porte de seu negocio: '))
    
    
    print('''
    Clientes (Mensal)
    1 - < 100
    2 - 100 - 500
    3 - > 500 
    ''')
    clientes = input(str('Digite o numero identificador do numero de clientes mensais de seu negocio: '))
    if clientes > '3':
        print('Digite uma opcao valida!')
    clientes = input(str('Digite o numero identificador do numero de clientes mensais de seu negocio: '))
    
    print('''
    Objetivo
    1 - Ampliar meu negocio
    2 - Reduzir custos
    3 - Aumentar vendas 
    ''')
    objetivo = input(str('Digite o numero identificador do obetivo de seu negocio: '))
    if objetivo > '3':
        print('Digite uma opcao valida!')
    objetivo = input(str('Digite o numero identificador do obetivo de seu negocio: '))
    
    key = int(industria + porte + clientes + objetivo)
    
    print(key)
    
    if (key > 1000) and (key < 2000):
        print('O Produto ideal ao seu negocio é o xpto')
    elif (key > 2000) and (key < 3000):
        print('O Produto ideal ao seu negocio é o xpto')
    elif key > 3000:
        print('O Produto ideal ao seu negocio é o xpto')


# In[15]:


# o nome do documento gerado servira como suporte para identificacao do acesso, sera o cpf ou cnpj
def compra():
    print('Preencha o formulario abaixo e o time de vendas entrará em contato!')
    print('''
    1 - MuleSoft
    2 - IA
    3 - Tableau
    4 - Vendas
    5 - Commerce
    ''')
    produto = input(str('Digite o numero identificador do produto que necessita: '))
    contato = input(str('Digite o principal telefone para contato: '))
    
    relatorio = produto + contato
    
    # gerar relatorio
    
    with open('path', 'w') as arquivo:
        arquivo.write(relatorio)
    
    print('Contato encaminhado ao time de vendas relacionado a seu produto, o time entrara em contato!')


# In[45]:


def sistema(): 
    print(' --- Seja bem vindo ao Portal Salesforce ---')
    print(' - Developed by: Unilmited Tech -')
    print(' --------------- Menu --------------')
    print('''
    1 - Qual produto se adequa a mim?
    2 - Comprar
    3 - Sair
    ''')
    print(' -----------------------------------')
    n = input(str('Digite o que deseja acessar: '))
    if n == '1': 
        print('Vamos lá!')
        briefing()
    elif n == '2':
        print('Vamos lá!')
        compra()
    elif n == '3':
        print('até logo!')
        
    dec = input(str('Podemos ajudar em algo mais? (S/N)'))
    if dec == 'S':
        sistema()
    elif dec == 'N':
        print('até logo!')
    else:
        print('Digite com S ou N!')
        dec = input(str('Podemos ajudar em algo mais? (S/N)'))


# In[46]:


def execucao():
    print('--- Bem vindo ao portal Salesforce ---')
    print('--- Developed by: Unlimited Tech ---')
    print('--------------------------------------')
    print('''
    --- Menu ---
    1 - Cadastro 
    2 - Login 
    ''')
    acesso = input(str('Digite o que deseja acessar: '))
    if acesso == '1':
        cadastro()
        print('Faca seu login!')
        execucao()
    elif acesso == '2':
        login()
        sistema()
    else: 
        print('A opcao digitada nao está listada em nosso alcance, tente novamente!')
        execucao()


# In[49]:


execucao()

