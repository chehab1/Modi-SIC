import pandas as pd


def getSybmolTable(df):
    df_symbolTable = pd.DataFrame(columns=['LCounter', 'label'])
    try:
        for i in df.index:
            if df['label'][i] != '':
                row = {'LCounter': str(df['LCounter'][i]), 'label': df['label'][i]}
                df_temp = pd.DataFrame([row])
                df_symbolTable = pd.concat([df_symbolTable, df_temp], axis=0, ignore_index=True)
    except:
        print('Error')
    return df_symbolTable
