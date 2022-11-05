import pandas as pd
import rsc.instructionSet as inst

objectCodeList = []


def df_to_dict(df):
    temp = {}
    for i in range(len(df)):
        temp[df.loc[i, 'label']] = df.loc[i, 'LCounter']
    return temp


def getObjectCode(df):
    for i in range(len(df)):
        temp = df.loc[i, 'inst']
        if inst.Mnemonic.__contains__(temp):
            if temp == 'LDL' or temp == 'LDX' or temp == 'LDA' or temp == 'STA':
                objectCodeList.append('0' + inst.Mnemonic[temp][2:])
            else:
                objectCodeList.append(inst.Mnemonic[temp][2:])
        else:
            objectCodeList.append(' ')
    empty_dict = df_to_dict(df)
    for i in range(len(df)):
        temp = df.loc[i, 'value']
        if empty_dict.__contains__(temp):
            objectCodeList[i] += empty_dict[temp]

    df.insert(loc=4, column='objCode', value=objectCodeList)
    print(df)
