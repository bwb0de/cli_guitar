#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import os
import itertools
import time

from collections import OrderedDict
from cli_tools import limpar_tela, amarelo, vermelho
from musicas import notas_amostra

C = (
      (None, 'Dó', 'Mi', 'Sol', 'Dó', 'Mi'),
      (None, 3, 2, 0, 1, 0)
    )

Dm = (
      (None, None, 'Ré', 'Lá', 'Ré', 'Fá'),
      (None, None, 0, 2, 3, 1 )
     )

Em = (
      ('Mi', 'Si', 'Mi', 'Sol', 'Si', 'Mi'),
      (0, 2, 2, 0, 0, 0)
     )  

F = (
      ('Fá', 'Dó', 'Fá', 'Lá', 'Dó', 'Fá'),
      (1, 3, 3, 2, 1, 1)
)

G = (
      ('Sol', 'Si', 'Ré', 'Sol', 'Ré', 'Sol'),
      (3, 2, 0, 0, 3, 3)
    )

Am = (
    (None, 'Lá', 'Mi', 'Lá', 'Dó', 'Mi'),
    (None, 0, 2, 2, 1, 0)
)

Bø = (
    (None, 'Si', 'Fá', 'Sol#', 'Ré', None),
    (None, 2, 3, 1, 3, None)
)

c_major_labels = ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bø']
c_major_cords = [C, Dm, Em, F, G, Am, Bø]
c_major_end = [('G', 'C'), ('G', 'Em'), ('G', 'F')]

def print_cadence(list_of_cords, list_of_dedilhados):
    line6 = ''
    line5 = ''
    line4 = ''
    line3 = ''
    line2 = ''
    line1 = ''

    tab = [line6, line5, line4, line3, line2, line1]

    for cord in list_of_cords:
        for ded in list_of_dedilhados:
            if ded == pima:
                tab = print_pima(cord, tab)


def tempo(andamento):
    a = int(andamento)
    minima = (60/a * 1.0) * 2
    seminima = (60/a * 1.0) / 1
    colcheia = (60/a * 1.0) / 2
    semicolcheia = (60/a * 1.0) / 4
    return minima, seminima, colcheia, semicolcheia


def compasso(proporcao, andamento):
    
    minima, seminima, colcheia, semicolcheia = tempo(andamento)

    tic_nums = int(proporcao.split(':')[0])
    tempo_referencia = int(proporcao.split(':')[1])

    if tempo_referencia == 2:
        tempo_compasso = tic_nums * minima

    elif tempo_referencia == 4:
        tempo_compasso = tic_nums * seminima

    elif tempo_referencia == 8:
        tempo_compasso = tic_nums * colcheia

    elif tempo_referencia == 16:
        tempo_compasso = tic_nums * semicolcheia


    return tic_nums, tempo_compasso
    
    
def metronomo(proporcao, andamento, notas):

    tamanho_musica = len(notas.keys())

    limpar_tela()
    tic_nums, tempo_compasso = compasso(proporcao, andamento)
    tempo_step = tempo_compasso/tic_nums
    n = 0
    m = 0
    compassos = 1
    mostrar_compasso = True
    limpar_tela_ao_final = False

    cd = int(tic_nums) * 2
    print ('Iniciando m´usica em compasso {} e andamento {} em...'.format(proporcao, andamento))
    while cd != 0:
        print(cd)
        cd -= 1
        time.sleep(tempo_step)

    print('')

    contratempo_duracao = tempo_step/2

    tp = True
    concluir_musica = False
    lirics_em_contratempo = False
    escrever_lirics_em_contratempo = False
    limpar_tela()

    output_lines = {'head': '', 'body': ''}

    while True:
        if tp:
            tp = False
            if mostrar_compasso:
                mostrar_compasso = False
                output_lines['body'] += "Compasso:" + str(compassos) + os.linesep
                #print("Compasso:", str(compassos))
            n += 1
            m += 1
            nota_da_vez = '{}:{}'.format(compassos, m)
            if notas.get(nota_da_vez):
                nota = notas[nota_da_vez][0]
                lirics = notas[nota_da_vez][1]
                if len(notas[nota_da_vez]) > 2:
                    lirics_em_contratempo = True
                tamanho_musica -= 1
            else:
                nota = ''
                lirics = False
            
            output_lines['head'] = '↓' + ' ' + os.linesep
            output_lines['body'] += str(m) + ' ' + vermelho(str(nota))
            if lirics:
                if lirics_em_contratempo:
                    escrever_lirics_em_contratempo = True
                    lirics_em_contratempo = False
                else:
                    output_lines['body'] += os.linesep + amarelo(lirics)
            output_lines['body'] += os.linesep

            limpar_tela(msg=output_lines['head'] + output_lines['body'])
            if n % tic_nums == 0:
                m = 0
                mostrar_compasso = True
                compassos += 1
                limpar_tela_ao_final = True
                if tamanho_musica == 0:
                    concluir_musica = True

        else:
            tp = True
            output_lines['head'] = '↑' + os.linesep

            if escrever_lirics_em_contratempo:
                output_lines['body'] += '  ·' + amarelo(lirics) + os.linesep
                escrever_lirics_em_contratempo = False
            else:
                output_lines['body'] += '  ·' + os.linesep 
            limpar_tela(msg=output_lines['head'] + output_lines['body'])
            if concluir_musica:
                break
            if limpar_tela_ao_final:
                limpar_tela()
                limpar_tela_ao_final = False
                output_lines = {'head': '', 'body': ''}
            

        time.sleep(contratempo_duracao)
            






def print_pima(cord, tab):
    out = tab.copy()
    cad = 0
    for idx in range(0,6):
        if cord[0][idx] == None:
            pass
        else:
            if cad == 0:
                out[idx] = out[idx] + cord[0][idx].ljust('4') + '({})'.format(str(cord[1][idx]))
                out[idx] = out[idx].ljust(6)
        


'''

E B C#m A

I V VI IV

I IV III IV V I

I IV III III IV I (trocar a cada duas)

'''