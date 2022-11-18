import rsc.instructionSet as inst_set
from operator import *
import ErrorHandling.byteValues as InvalidByte


def size_c(val):
    return len(val) - 3


def size_x(val):
    size = len(val) - 3
    if size % 2 == 0:
        return size / 2
    return (size / 2) + 1


def size_w(val):
    return int(val) * 3


def insert_LC(df):
    lc = ['0']
    inst = inst_set.Mnemonic

    for i in range(0, len(df['inst'])):
        instInput = df.loc[i, 'inst'].upper()
        # for start line
        if i == 0:
            lc.append(str(df.loc[0, 'value']))
        # instructions and word
        elif inst.__contains__(instInput) or instInput == 'WORD':
            # format_1
            if instInput != 'WORD' and isinstance(inst[instInput], list):
                # nlc -> new locationCounter
                nlc = hex(add(int(lc[len(lc) - 1], 16), int('1', 16)))
            else:
                nlc = hex(add(int(lc[len(lc) - 1], 16), int('3', 16)))
            lc.append(nlc[2:].zfill(4))

        elif instInput == 'BYTE':
            val = df.loc[i, 'value']
            # check val of byte C' '
            if val[0] == 'C' and val[1] == '\'' and val[len(val) - 1] == '\'':
                # get the size of c
                sc = size_c(val)
                nlc = hex(add(int(lc[len(lc) - 1], 16), int(sc)))
                lc.append(nlc[2:].zfill(4))
            # check val of byte X' '
            elif val[0] == 'X' and val[1] == '\'' and val[len(val) - 1] == '\'':
                # get the size of x
                sx = int(size_x(val))
                nlc = hex(add(int(lc[len(lc) - 1], 16), int(sx)))
                lc.append(nlc[2:].zfill(4))
            # RAISE ERROR IF VALUE OF BYTE IS INVALID
            else:
                raise InvalidByte.invalidByteValue \
                    (str(i + 1), "Invalid Byte Value in Intermediate_File line -> ")
        elif instInput == 'RESW':
            val = df.loc[i, 'value']
            sw = str(size_w(val))
            nlc = hex(add(int(lc[len(lc) - 1], 16), int(sw)))
            lc.append(nlc[2:].zfill(4))

        elif instInput == 'RESB':
            val = df.loc[i, 'value']
            nlc = hex(add(int(lc[len(lc) - 1], 16), int(val)))
            lc.append(nlc[2:].zfill(4))
        # if there is no end then it will be added
        if i == len(df['inst']) - 1 and instInput != 'END':
            df.loc[i + 1, 'inst'] = 'END'
            df.loc[i + 1, 'value'] = df.loc[0, 'value']
            df.loc[i + 1, 'label'] = ''

    df.insert(loc=0, column='LCounter', value=lc)
    return df
