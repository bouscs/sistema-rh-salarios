"""
Sistema de RH - Cálculo Salarial
Versão: 2.0.0
Autores: Artur B. Xavier, David Megumi, Miguel Teixeira Magalhães
"""

# BANCO DE DADOS:

# importando a extensao para conectar com o banco de dados oracle
import cx_Oracle

# tentativa de conexão com o banco de dados:
try:
    conn = cx_Oracle.connect('Rh/senha@localhost:1521/xe')    # aqui, a conexão oracle e sua senha são Rh e senha, respectivamente. A porta e extensão são osvalores padronizados.
# mensagem de erro de conexão:
except Exception as erro:
    print('Ocorreu um erro ao tentar conectar ao banco de dados!', erro)
# tentativa de fetch dos dados de valores de impostos:
else:
    print('\nA conexão com o banco de dados foi bem sucedida.')
    try:
        cur = conn.cursor()
        sql = """ SELECT valor FROM taxas """
        cur.execute(sql)
        valores = cur.fetchall()        # guarda valores selecionados do banco de dados em uma lista de tuples                                                             
    # erro de fetch:
    except Exception as erro:
        print('Ocorreu um erro ao tentar extrair informações do banco de dados!', erro)
    # mensagem de sucesso de conexão e fetch:
    else:
        print('Extração de dados completa.\n')
    # fechando cursor:
    finally:
        cur.close()
# fechando conexão:
finally:
    conn.close()


print('\nSISTEMA DE RH - CÁLCULO SALARIAL')
print()


# FUNÇÕES:
# função para calculo do inss
def calculo_inss(x):
    # possiveis valores de aliquotas:
    y = x  # x e y são o valor do salario bruto que será calculado
    a = float(valores[0][0])
    b = float(valores[1][0])
    c = float(valores[2][0])
    if 0 < x <= float(valores[3][0]):                           # 1a possibilidade de salario (menor salario possivel)
        return y *  float(valores[6][0])
    elif float(valores[3][0]) < x <= float(valores[4][0]):      # 2a possibilidade de salario
        y = x - float(valores[3][0])
        b = y *  float(valores[7][0])
        return a + b
    elif float(valores[4][0]) < x <= float(valores[5][0]):      # 3a possibilidade de salario
        y = x - float(valores[4][0])
        c = y *  float(valores[8][0])
        return a + b + c
    elif float(valores[5][0]) < x <= float(valores[10][0]):     # 4a possibilidade de salario
        y = x -  float(valores[5][0])
        d = y *  float(valores[9][0])
        return a + b + c + d
    else:                                                       # 5a possibilidade de salario (maior salario possivel)
        return  float(valores[11][0])

# funcao de calculo de irrf
def calculo_irrf(a, b):  # aqui, a e b são respectivamente, salario bruto e inss

    # base de calculo para o IRRF
    basec = a - b - pensao - (dependentes *  float(valores[12][0]))

    # valores de aliquotas e descontos baseados na tabela de IRRF de 2021:
    if basec <  float(valores[13][0]):
        return 0
    elif float(valores[13][0]) <= basec < float(valores[14][0]):
        return (basec * float(valores[17][0])) - float(valores[21][0])
    elif float(valores[14][0]) <= basec < float(valores[15][0]):
        return (basec * float(valores[18][0])) - float(valores[22][0])
    elif float(valores[15][0]) <= basec <= float(valores[16][0]):
        return (basec * float(valores[19][0])) - float(valores[23][0])
    elif basec > float(valores[16][0]):
        return (basec * float(valores[20][0])) - float(valores[24][0])

# função de calculo de porcentagem
def porcentagem(x, y):
    return (y * 100) / x

# Retornar input validado pela função "validar"
def input_validado(mensagem, erro, validar):
    while True:
        resposta = input(mensagem)
        try:
            if validar(resposta):
                return resposta
            else:
                print(erro)
        except:
            print(erro)


# No de funcionarios para a repetição:
n = int(input_validado('Insira o numero de funcionários a calcular: ',
                       'Favor inserir um valor válido.', 
                       lambda resposta: float(resposta) >= 1))

# repetição do programa para no de funcionarios a calcular:
for i in range(n):
    m = i+1

    # informações do funcionario:
    nome = input(f'\nNome do funcionário #{m}: ') #sem validações, assim até funcionarios com nomes muito exóticos não causariam problemas 
    # setor com validações para os supostos setores da empresa:
    while True:
        setor1 = input_validado('Setor do funcionário ( ADM / FN / RH / COM / OP / TI ): ',
                            'Insira um setor válido',
                            lambda resposta: resposta.upper() == 'ADM' or           # setor administrativo
                                             resposta.upper() == 'FN' or            # setor financeiro
                                             resposta.upper() == 'RH' or            # setor de recursos humanos
                                             resposta.upper() == 'COM' or           # setor comercial
                                             resposta.upper() == 'OP' or            # setor operacional
                                             resposta.upper() == 'TI').upper()      # setor de tecnologia da informação
        # nome do setor por extenso:
        if setor1 == 'ADM':
            setor = 'Setor Administrativo'
            break
        elif setor1 == 'FN':
            setor = 'Setor Financeiro'
            break
        elif setor1 == 'RH':
            setor = 'Setor de Recursos Humanos'
            break
        elif setor1 == 'COM':
            setor = 'Setor Comercial'
            break
        elif setor1 == 'OP':
            setor = 'Setor Operacional'
            break
        elif setor1 == 'TI':
            setor = 'Setor de Tecnologia da Informação'
            break
        else:
            print('Erro de input de setor! Insira o setor novamente!')


    # entradas para cálculos:
    print(f'\n\nCÁLCULO PARA FUNCIONÁRIO #{m}:\n')
    # dados necessários para cálculos
    # Salário bruto
    salariob = float(input_validado('Valor do salário bruto: ',
                                    'Favor inserir um valor válido.',
                                    lambda resposta: float(resposta) >= float(valores[3][0])))
    # Bônus do mês atual
    bonus = float(input_validado('Valor do bônus do mês: ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) >= 0))
    # Média de bonus mensal do ano trabalhado
    bonust = float(input_validado('Bônus total do ano (media dos bônus mensais do ano): ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) >= 0))
    # Meses trabalhados no ano
    meses =  float(input_validado('Total de meses trabalhados no ano: ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) > 0))
    # Número de dependentes
    dependentes =  float(input_validado('Número de dependentes: ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) >= 0))
    # Número de dias de férias tirados
    ferias = float(input_validado('Número de dias de férias tirados: ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) >= 14))
    while True:
        global abono
        abono = input('Abono pecuniário ("s" ou "n"):').lower().strip()
        if abono == "s" or abono == "n":
            break
        else:
            print('Favor inserir um valor que seja "s" ou "n".')
    # Valor da pensão alimentícia
    pensao = float(input_validado('Valor da pensão alimentícia: ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) >= 0))
    #Valor da soma de todo e qualquer desconto (plano odontológico/plano de saude/etc)
    descontos = float(input_validado('Valor da soma de todo e qualquer desconto (plano odontológico/plano de saude/etc): ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) >= 0))


    # calculo do salario liquido
    inss = calculo_inss(salariob)
    insspor = porcentagem(salariob, inss)
    irrf = calculo_irrf(salariob, inss)
    irrfpor = porcentagem(salariob, irrf)
    salarioliq = salariob - inss - irrf - descontos - pensao  # salario liquido sem bonus
    salariobon = salarioliq + bonus  # salario liquido com bonus


    # decimo terceiro
    # primeira parcela:
    p1b = (salariob * meses) / 12  # base do decimo terceiro (total a ser pago sem aplicação de impostos)
    parcela1_13 = p1b / 2  # parcela 1 do decimo terceiro

    # segunda parcela
    # função de calculo do inss para o decimo terceiro
    inss13 = calculo_inss(p1b)
    inss13por = porcentagem(salariob, inss)
    irrf13 = calculo_irrf(p1b, inss13)
    irrf13por = porcentagem(salariob, irrf)
    # calculo final da segunda parcela
    parcela2_13 = parcela1_13 - inss13 - irrf13 + bonust

    # parcela unica do decimo terceiro
    parcelaunica = parcela1_13 + parcela2_13


    # calculo salário de férias
    diaria = (salariob + bonust) / 30
    salariobferias = diaria * ferias * (4 / 3)

    # abono pecuniário: https://www.dicionariofinanceiro.com/abono-pecuniario/
    abonopec = ((salariob / 30) * ferias) / 3
    inssferias = calculo_inss(salariobferias)
    inssferiaspor = porcentagem(salariobferias,inssferias)
    irrfferias = calculo_irrf(salariobferias, inssferias)
    irrfferiaspor = porcentagem(salariobferias,irrfferias)
    salarioliqferias = salariobferias - inssferias - irrfferias
    if abono == "s":
        salarioliqferias += abonopec


    # print dos resultados
    print()
    print(f'\n----------------------------------------------------------------------\n\nRESULTADO DO FUNCIONARIO #{m}: ')
    print()

    print(f'Nome do funcionário: {nome}\nSetor do funcionário: {setor}')

    print()

    print('SALÁRIO MENSAL:')

    print (f'O valor do INSS contribuido é de: R${inss:.3f} \033 {insspor:.3f}% do salário bruto')

    print (f'O valor do IRRF a ser pago é de: R${irrf:.3f} \033 {irrfpor:.3f}% do salário bruto')

    print (f'O salário líquido é: R${salariobon:.3f}\n')

    print('\nDÉCIMO TERCEIRO SALÁRIO:')

    print (f'O valor do INSS contribuido no Décimo Terceiro é de: R${inss13:.3f} \033 {inss13por:.3f}% do Décimo Terceiro bruto')

    print (f'O valor do IRRF a ser pago no Décimo Terceiro é de: R${irrf13:.3f} \033 {irrf13por:.3f}% do Décimo Terceiro')

    print (f'A primeira parcela do Décimo Terceiro é: R${parcela1_13:.3f}')

    print (f'A segunda parcela do Décimo Terceiro é: R${parcela2_13:.3f}')

    print (f'Parcela única: R${parcelaunica:.3f}\n')

    print('\nSALÁRIO DE FÉRIAS:')

    print(f'O valor do INSS descontado das férias é de R$ {inssferias:.3f} \033 {inssferiaspor:.3f}% do salário de férias bruto')  
    
    print(f'o do IRRF descontado das férias é de R${irrfferias:.3f} \033 {irrfferiaspor}% do salário de férias bruto')

    print(f'O valor do salário de férias é de: R$ {salarioliqferias:.3f}\n')

    print('\n----------------------------------------------------------------------\n')

# finalização do programa
input('Pressione Enter para fechar o programa...')