import rsc.instructionSet as inst
from pass_2 import immediate, indexing
import ErrorHandling.labelNotFound as notFound
objectCodeList = []


def df_to_dict(df):
    temp = {}
    for i in range(len(df)):
        if df.loc[i, 'label'] != '':
            temp[df.loc[i, 'label']] = df.loc[i, 'LCounter']
    return temp


def getObjectCode(df):
    empty_dict = df_to_dict(df)

    for i in range(len(df)):
        temp = df.loc[i, 'inst']
        value = df.loc[i, 'value']
        #  FULL INSTRUCTION SET OF modi-SIC
        if inst.Mnemonic.__contains__(temp):
            # check for values end with ,X
            if len(value) > 1 and value[len(value) - 2:] == ',X':
                if not empty_dict.__contains__(value[0:len(value)-2]):
                    raise notFound.LabelNotFound('Value ' + value + ' Not Found in Labels in the instruction ' + temp)
                objectCodeList.append(indexing.handleIndexing(df, temp, value))
            # if it immediate value
            elif len(value) >= 1 and value[0] == '#':
                objectCodeList.append(immediate.immediateObjectCode(temp, value))
            # Handling if value not found in label
            elif not temp == 'RSUB' and not empty_dict.__contains__(value):
                raise notFound.LabelNotFound('Value ' + value + ' Not Found in Labels in the instruction ' + temp)
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
        else:
            objectCodeList.append(' ')

    for i in range(len(df)):
        temp = df.loc[i, 'value']
        if empty_dict.__contains__(temp):
            if temp[0] == '#':
                continue
            else:
                objectCodeList[i] += empty_dict[temp]

    df.insert(loc=4, column='objCode', value=objectCodeList)
    return df
