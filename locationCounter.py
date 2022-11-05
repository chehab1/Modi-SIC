import rsc.instructionSet as inst_set
from operator import *


def size_c(val):
    c = 0
    for i in range(0, len(val) - 1):
        if i == 0 or i == 1 or i == len(val) - 1:
            continue
        else:
            c += 1
    return c


def size_x(val):
    c = 0
    for i in range(0, len(val) - 1):
        if i == 0 or i == 1 or i == len(val) - 1:
            continue
        else:
            c += 1

    if c % 2 == 0:
        return c / 2
    return (c / 2) + 1


def size_w(val):
    return int(val) * 3


def insert_LC(df):
    lc = ['0']
    inst = inst_set.Mnemonic

    for i in range(0, len(df['inst']) - 1):
        try:
            if i == 0:
                lc.append(df.loc[0, 'value'])

            elif inst.__contains__(df.loc[i, 'inst']) or df.loc[i, 'inst'] == 'WORD':
                nlc = hex(add(int(lc[len(lc) - 1], 16), int('3', 16)))
                lc.append(nlc[2:])

            elif df.loc[i, 'inst'] == 'BYTE':
                val = df.loc[i, 'value']
                if val[0] == 'C':
                    # get the size of c
                    sc = size_c(val)
                    nlc = hex(add(int(lc[len(lc) - 1], 16), int(sc)))
                    lc.append(nlc[2:])
                else:
                    # get the size of x
                    sx = int(size_x(val))
                    nlc = hex(add(int(lc[len(lc) - 1], 16), int(sx)))
                    lc.append(nlc[2:])

            elif df.loc[i, 'inst'] == 'RESW':
                val = df.loc[i, 'value']
                sw = str(size_w(val))
                nlc = hex(add(int(lc[len(lc) - 1], 16), int(sw)))
                lc.append(nlc[2:])

            elif df.loc[i, 'inst'] == 'RESB':
                val = df.loc[i, 'value']
                nlc = hex(add(int(lc[len(lc) - 1], 16), int(val)))
                lc.append(nlc[2:])
            else:
                lc.append(' ')
        except:
            lc.append(' ')

    df.insert(loc=0, column='Location_counter', value=lc)
    return df
