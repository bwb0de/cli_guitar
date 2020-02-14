#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import os
import itertools

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


def print_pima(cord, tab):
    out = tab.copy()
    cad = 0
    for idx in range(0,6):
        if cord[0[idx] == None:
            pass
        else:
            if cad == 0:
                out[idx] = out[idx] + cord[0][idx].ljust('4') + '({})'.format(str(cord[1][idx]))
                out[idx] = out[idx].ljust(6)
        


E B C#m A

I V VI IV

I IV III IV V I

I IV III III IV I (trocar a cada duas)

