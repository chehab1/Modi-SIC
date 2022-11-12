import rsc.instructionSet as inst_set
from operator import *
import ErrorHandling.byteValues as InvalidByte


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

    for i in range(0, len(df['inst'])):
        try:
            if i == 0:
                lc.append(str(df.loc[0, 'value']))
            elif inst.__contains__(df.loc[i, 'inst']) or df.loc[i, 'inst'] == 'WORD':
                if df.loc[i, 'inst'] != 'WORD' and isinstance(inst[df.loc[i, 'inst']], list):
                    nlc = hex(add(int(lc[len(lc) - 1], 16), int('1', 16)))
                else:
                    nlc = hex(add(int(lc[len(lc) - 1], 16), int('3', 16)))
                lc.append(nlc[2:].zfill(4))

            elif df.loc[i, 'inst'] == 'BYTE':
                val = df.loc[i, 'value']
                if val[0] == 'C':
                    # get the size of c
                    sc = size_c(val)
                    nlc = hex(add(int(lc[len(lc) - 1], 16), int(sc)))
                    lc.append(nlc[2:].zfill(4))
                elif val[0] == 'X':
                    # get the size of x
                    sx = int(size_x(val))
                    nlc = hex(add(int(lc[len(lc) - 1], 16), int(sx)))
                    lc.append(nlc[2:].zfill(4))
                else:
                    raise InvalidByte.invalidByteValue\
                        (str(i + 1), "Invalid Byte Value in Intermediate_File line -> ")
            elif df.loc[i, 'inst'] == 'RESW':
                val = df.loc[i, 'value']
                sw = str(size_w(val))
                nlc = hex(add(int(lc[len(lc) - 1], 16), int(sw)))
                lc.append(nlc[2:].zfill(4))

            elif df.loc[i, 'inst'] == 'RESB':
                val = df.loc[i, 'value']
                nlc = hex(add(int(lc[len(lc) - 1], 16), int(val)))
                lc.append(nlc[2:].zfill(4))
            # if there is no end then it will be added it
            if i == len(df['inst']) -1 and df.loc[i, 'inst'] != 'END':
                df.loc[i+1, 'inst'] = 'END'
                df.loc[i+1, 'value'] = df.loc[0, 'value']
                df.loc[i+1, 'label'] = ''


        except InvalidByte.invalidByteValue as e:
            raise e

    df.insert(loc=0, column='LCounter', value=lc)
    return df
