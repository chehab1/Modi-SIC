import rsc.instructionSet as inst
from pass_2 import immediate, indexing
import ErrorHandling.labelNotFound as notFound

objectCodeList = []


# convert symbol table to a dictionary
def df_to_dict(df):
    temp = {}
    for i in range(len(df)):
        if df.loc[i, 'label'] != '':
            temp[df.loc[i, 'label']] = df.loc[i, 'LCounter']
    return temp


def getObjectCode(df):
    empty_dict = df_to_dict(df)
    for i in range(len(df)):
        temp = df.loc[i, 'inst'].upper()
        value = df.loc[i, 'value']

        #  FULL INSTRUCTION SET OF modi-SIC
        if inst.Mnemonic.__contains__(temp):
            # check if it is format 1
            if isinstance(inst.Mnemonic[temp], list):
                objectCodeList.append(inst.Mnemonic[temp][1][2:])
            # check for values end with ,X
            elif len(value) > 1 and value[len(value) - 2:] == ',X':
                # check if this value is already in labels or not
                if not empty_dict.__contains__(value[0:len(value) - 2]):
                    raise notFound.LabelNotFound(value, temp)
                objectCodeList.append(indexing.handleIndexing(df, temp, value))
            # if it immediate value
            elif len(value) >= 1 and value[0] == '#':
                objectCodeList.append(immediate.immediateObjectCode(temp, value, i))
            # Handling if value not found in labels
            elif not temp == 'RSUB' and not empty_dict.__contains__(value):
                raise notFound.LabelNotFound(value, temp)
            elif temp == 'RSUB':
                objectCodeList.append(inst.Mnemonic[temp][2:] + '0000')
            # for LDL, LDX, LDA, STA
            elif temp == 'LDL' or temp == 'LDX' or temp == 'LDA' or temp == 'STA':
                if len(inst.Mnemonic[temp]) == 4:
                    objectCodeList.append('0' + inst.Mnemonic[temp][3:])
                else:
                    objectCodeList.append('0' + inst.Mnemonic[temp][2:])
            # for normal instructions
            else:
                objectCodeList.append(inst.Mnemonic[temp][2:])

        elif temp == 'WORD':
            dec = int(df.loc[i, 'value'])
            hexSt = format(dec, '02x')
            hexSt = hexSt.zfill((6 - len(hexSt)) + len(hexSt))
            objectCodeList.append(hexSt)

        elif temp == 'BYTE':
            # value begin with X
            val = df.loc[i, 'value']
            if val[0] == 'X':
                ob_code = val[2:len(val) - 1]
                objectCodeList.append(ob_code)
            # value begin with C
            elif val[0] == 'C':
                # convert ascii to hex
                txt = val[2:len(val) - 1]
                ob_code = txt.encode('utf-8').hex().upper()
                objectCodeList.append(ob_code)
        elif temp == 'END':
            objectCodeList.append('      ')
        else:
            objectCodeList.append(' ')

    for i in range(len(df)):
        temp = df.loc[i, 'value']
        if empty_dict.__contains__(temp):
            if temp[0] == '#' or len(objectCodeList[i]) == 6:
                continue
            else:
                objectCodeList[i] += empty_dict[temp]

    df.insert(loc=4, column='objCode', value=objectCodeList)
    return df
