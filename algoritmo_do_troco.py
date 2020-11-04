"""Algoritmo do troco baseado em algoritmo guloso, buscando 
trocar valores inputados com a menor quantidade possível de moedas
"""

import os


def calcular_troco(moedas, valor):
    """ Troca as moedas de acordo com o valor passado.

    param: dict com as moedas existentes e o valor a ser trocado.
    return: list com quantidade de troco de moedas por valor de cada moeda.
    """
    restante = valor  # Verificador de valor restante durante execução
    soma = 0  # Acumulador do valor já trocado durante execução
    i = 0
    # List com quantidade de moedas por valor de moeda
    troco = [0 for i in moedas['moeda']]

    while soma != valor and i <= len(moedas['moeda'])-1:
        # Quantidade de moedas para valor de moeda
        troco[i] = restante//moedas['moeda'][i]
        # Se necessário mais moedas do que a quantidade existente,
        # Usa-se o que estiver disponível
        if troco[i] > moedas['quantidade'][i]:
            troco[i] = moedas['quantidade'][i]
        restante -= moedas['moeda'][i]*troco[i]
        soma += moedas['moeda'][i]*troco[i]
        i += 1

    if soma == valor:
        return troco
    else:
        troco = False
        return troco


def mostrar_moedas(moedas):
    """ Exibe as moedas e a quantidade e suas respectivas
    quantidades disponíveis.

    param: dict com as moedas e suas respectivas quantidades disponíveis 
    return: sem retorno
    """
    print("-"*21)
    print("{:>19}" .format('MOEDAS DISPONIVEIS'))
    print("-"*21)
    print("{:<10} {:<20}" .format('MOEDA', 'QUANTIDADE'))
    for i in range(len(moedas['moeda'])):
        print("{:<10} {:<11}" .format(
            moedas['moeda'][i], moedas['quantidade'][i]))
    print("-"*21)


def mostrar_troco(troco):
    """Mostra as moedas que foram trocadas;"""
    os.system("cls")
    print("-"*21)
    print("{:>18}" .format('MOEDAS TROCADAS'))
    print("-"*21)
    print("{:<10} {:<20}" .format('MOEDA', 'QUANTIDADE'))
    for i in range(len(troco)):
        if troco[i] != 0:
            print("{:<10} {:<11}" .format(moedas['moeda'][i], troco[i]))
    print("-"*21)


moedas = {
    'moeda': [50, 20, 10, 5, 2],
    'quantidade': [10, 10, 10, 10, 10]
}

while moedas['quantidade']:
    mostrar_moedas(moedas)
    valor = int(input("Digite a quantidade do troco desejada: "))
    troco = calcular_troco(moedas, valor)

    #  Subtrai as moedas trocadas da quantidade total de moedas existentes
    if troco:
        for i in range(len(moedas['moeda'])):
            moedas['quantidade'][i] -= troco[i]
        mostrar_troco(troco)
    else:
        os.system("cls")
        print("Moedas insuficientes, desculpe!\n")

    opcao = str(input("Deseja outro valor de troco?:(s/n): "))
    if opcao == 'n':
        break

    os.system("cls")
