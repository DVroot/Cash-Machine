# Author: Daniel Vieira
# Email: danielsrosa13@gmail.com

import os

def setNotas():
    print('ADICIONANDO NOTAS...')
    arrayNotas = []
    pausa = True
    while pausa:
        try:
            # verifica se e inteiro ou escapa um erro
            valorNota = int(input('Digite o valor da nota e aperte ENTER para salvar: '))
            #verifica chave de parada
            if valorNota == 0:
                pausa = False
            else:
                # verifica se a nota esta entre 1 e 1000
                if valorNota >= 1 and valorNota <= 1000:
                    # verifica se o valor da nota ja foi adicionado
                    if valorNota in arrayNotas:
                        print('\nERRO: Esta nota ja foi adicionada!\n')
                    else:
                        # insere a nota no vetor de notas
                        arrayNotas.append(valorNota)
                else:
                    print('\nERRO: A nota precisa ser maior que 1 e menor que 1000!\n')
        except ValueError:
            # escapa erro se a nota no for um numero inteiro
            print('\nERRO: A nota precisa ser um numero inteiro!\n')
    # Alinha as notas na ordem cescente
    arrayNotas.sort()
    # Inverte o array na ordem decrescente 
    arrayNotas.reverse()
    return arrayNotas


def saque(notas):
    print('\nRETIRAR NOTAS...')
    if(len(notas) != 0):
        pausa = True
        while pausa:
            try:
                valorSaque = int(input('\nValor desjado: '))
                if valorSaque == 0:
                    pausa = False
                    # os.system('pause')
                elif valorSaque < 0:
                    print('Erro: O valor do saque deve ser um valor maior que zero!')
                else:
                    notasSaque = []
                    while (valorSaque >= min(notas)):
                        for i in range(len(notas)):
                            if valorSaque >= notas[i]:
                                valorSaque = valorSaque - notas[i]
                                notasSaque.append(notas[i])
                                break
                    
                    # Exibe todas as notas
                    # print(notasSaque)
                    
                    if valorSaque > 0:
                        print('Erro: Notas indisponíveis')
                    else:
                        print('RESULTADO:', end=' ')

                        # Conta a quantidade de cada nota
                        for j in range(len(notas)):
                            # resposta no singular para contagem de notas igual a 1 (X = um)
                            if notasSaque.count(notas[j]) == 1:
                                print('{} nota de {},' .format(notasSaque.count(notas[j]), notas[j]), end=' ')
                            # respostas no plural para contagem de notas maior que 1 (X > um)
                            elif notasSaque.count(notas[j]) != 0:
                                print('{} notas de {},' .format(notasSaque.count(notas[j]), notas[j]), end=' ')

            except ValueError:
                print('Erro: Valor invalido. ')
    else:
        print('Erro: Nao existe notas para sacar')
        os.system('pause')


def Main():
    print('...:::  CASH MACHINE  :::...')
    print('PARA SAIR DIGITE 0 (ZERO)...\n')
    print('')
    notas = setNotas()
    print('\nNotas disponíveis\n{}\n'.format(notas))
    saque(notas)

   
Main()



