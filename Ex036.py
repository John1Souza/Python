while True:
    casa = float(input('Digite o valor da casa: '))
    sal = float(input('Digite seu salário R$ : '))
    mes = int(input('Quantos anos de financiamento? '))
    prest = casa / (mes * 12)
    if prest > (sal * 0.3):
        print(f'Para pagar a casa no valor de R$ {casa:.2f} em {mes} anos a  prestação será de {prest:.2f} por mês, \nesse valor supera o limite de 30,00% do seu salário atual, o empréstimo foi negado!')
    elif prest <= (sal * 0.3):
        print('PARABÉNS!!! empréstimo aprovado com sucesso!')
        print(f'Seu empréstimo de R$ {casa:.2f} será pago em pequenas parcelas de R$ {prest:.2f} por Mês durante os {mes} Anos')
    q = input('Quer continuar? [S/N] ').upper()
    if q == 'S':
        continue
    else:
        break
