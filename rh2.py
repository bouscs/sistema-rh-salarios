"""
Sistema de RH - Cálculo Salarial
Versão: 1.0.0
Autores: Artur B. Xavier, David Megumi, Miguel Teixeira Magalhães
"""

print('SISTEMA DE RH - CÁLCULO SALARIAL')


# Retornar input validado pela função "validar"
def input_validado(mensagem, erro, validar):
    while True:
        try:
            resposta = input(mensagem)
            if validar(resposta):
                return resposta
            else:
                raise
        except:
            print(erro)


# Salário bruto
salariob = float(input_validado('Valor do salário bruto: ',
                                'Favor inserir um valor válido.',
                                lambda resposta: float(resposta) > 0))

# Bônus do mês atual
bonus = float(input_validado('Valor do bônus do mês: ',
                             'Favor inserir um valor válido.',
                             lambda resposta: float(resposta) >= 0))

# Média de bonus mensal do ano trabalhado
bonust = float(input_validado('Bônus total do ano (media dos bônus mensais do ano): ',
                              'Favor inserir um valor válido.',
                              lambda resposta: float(resposta) >= 0))

# Meses trabalhados no ano
meses = float(input('Número total de meses trabalhados (mais do que 15 dias trabalhados):'))

# Número de dependentes
dependentes = float(input('Número de dependentes:'))

# Número de dias de férias tirados
ferias = float(input('Dias de férias tirados:'))

while True:
    global abono
    abono = input('Abono pecuniário ("s" ou "n"):')
    if abono == "s" or abono == "n":
        break
    else:
        print('Favor inserir um valor que seja "s" ou "n".')

pensao = float(input('Valor da pensão alimentícia, se não houver, digite 0):'))
descontos = float(
    input('Valor da soma de todo e qualquer desconto (plano odontológico/plano de saude/tc),se não houver, digite 0:'))


# funções:
# função para calculo do inss
def calculo_inss(x):
    # possiveis valores de aliquotas:
    y = x  # x e y são o valor do salario bruto que será calculado
    a = 82.5
    b = 99.31
    c = 132.2076
    if 0 < x <= 1100:  # 1a possibilidade de salario (menor salario possivel)
        return y * 0.075
    elif 1100 < x <= 2203.48:  # 2a possibilidade de salario
        y = x - 1100
        b = y * 0.09
        return a + b
    elif 2203.48 < x <= 3305.22:  # 3a possibilidade de salario
        y = x - 2203.48
        c = y * 0.12
        return a + b + c
    elif 3305.22 < x <= 6433.57:  # 4a possibilidade de salario
        y = x - 3305.22
        d = y * 0.14
        return a + b + c + d
    else:  # 5a possibilidade de salario (maior salario possivel)
        return 751.97


# funcao de calculo de irrf
def calculo_irrf(a, b):  # aqui, a e b são respectivamente, salario bruto e inss

    # base de calculo para o IRRF
    basec = a - b - pensao - (dependentes * 189.59)

    # valores de aliquotas e descontos baseados na tabela de IRRF de 2021:
    if basec < 1903.98:
        return 0
    elif 1903.99 <= basec < 2826.66:
        return (basec * 0.075) - 142.8
    elif 2826.66 <= basec < 3751.06:
        return (basec * 0.15) - 354.80
    elif 3751.06 <= basec <= 4664.68:
        return (basec * 0.225) - 636.13
    elif basec > 4664.68:
        return (basec * 0.275) - 869.36


# função de calculo de porcentagem
def porcentagem(x, y):
    return (y * 100) / x


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

# calculo falário de férias
diaria = (salariob + bonust) / 30
salariobferias = diaria * ferias * (4 / 3)

# abono pecuniário: https://www.dicionariofinanceiro.com/abono-pecuniario/
abonopec = ((salariob / 30) * ferias) / 3

inssferias = calculo_inss(salariobferias)
irrfferias = calculo_irrf(salariobferias, inssferias)

salarioliqferias = salariobferias - inssferias - irrfferias

if abono == "s":
    salarioliqferias += abonopec

# print dos resultados
print(f'o valor do inss contribuido é de: {inss:.3f}({insspor:.3f}% do salário bruto)')

print(f'o valor do irrf a ser pago é de: {irrf:.3f}({irrfpor:.3f}% do salário bruto)')
print(f'O salário líquido é: {salarioliq:.3f}R$ ou, considerando os bonus recebidos: {salariobon:.3f}R$')

print(f'A primeira parcela do Décimo Terceiro é: {parcela1_13:.3f}R$')
print(f'A segunda parcela do Décimo Terceiro é: {parcela2_13:.3f}R$')

print(f'o valor do inss contribuido no Décimo Terceiro é de: {inss13:.3f}({inss13por:.3f}% do Décimo Terceiro bruto)')
print(f'o valor do irrf a ser pago no Décimo Terceiro é de: {irrf13:.3f}({irrf13por:.3f}% do Décimo Terceiro)')
print(f'Parcela unica: {parcelaunica:.3f}R$')

print(
    f'O valor do INSS descontado das férias é de R$ {inssferias:.3f} e o do IRRF descontado das férias é de R$ {irrfferias:.3f}')
print(f'O valor do salário de férias é de: R$ {salarioliqferias:.3f}')

input('Pressione Enter para fechar o programa...')
