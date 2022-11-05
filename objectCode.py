import pandas as pd
import rsc.instructionSet as inst

objectCodeList = []


def df_to_dict(df):
    temp = {}
    for i in range(len(df)):
        if (df.loc[i, 'label'] != ''):
            temp[df.loc[i, 'label']] = df.loc[i, 'LCounter']
    return temp


def getObjectCode(df):
    for i in range(len(df)):
        temp = df.loc[i, 'inst']
        if temp == 'RSUB':
            objectCodeList.append('4c0000')
        # for All instructions
        elif inst.Mnemonic.__contains__(temp):
            # for LDL, LDX, LDA, STA
            if temp == 'LDL' or temp == 'LDX' or temp == 'LDA' or temp == 'STA':
                if len(inst.Mnemonic[temp]) == 4:
                    objectCodeList.append('0' + inst.Mnemonic[temp][3:])
                else:
                    objectCodeList.append('0' + inst.Mnemonic[temp][2:])
            # for normal instructions
            else:
                objectCodeList.append(inst.Mnemonic[temp][2:])

        elif temp == 'WORD':
            dec = int(df.loc[i, 'value'])
            hexa = format(dec, '02x')
            hexa = hexa.zfill((6 - len(hexa)) + len(hexa))
            objectCodeList.append(hexa)

        elif temp == 'BYTE':
            ## value begin with X
            val = df.loc[i, 'value']
            if val[0] == 'X':
                ob_code = val[2:len(val) - 1]
                ob_code = ob_code.zfill((6 - len(ob_code)) + len(ob_code))
                objectCodeList.append(ob_code)
            ## value begin with C
            else:
                # convert ascii to hex
                txt = val[2:len(val) - 1]
                ob_code = txt.encode('utf-8').hex().upper()
                objectCodeList.append(ob_code)

        else:
            objectCodeList.append(' ')

    empty_dict = df_to_dict(df)

    for i in range(len(df)):
        temp = df.loc[i, 'value']
        if temp.isnumeric():
            objectCodeList[i] += ''
        elif empty_dict.__contains__(temp):
            objectCodeList[i] += empty_dict[temp]
    df.insert(loc=4, column='objCode', value=objectCodeList)
    return df