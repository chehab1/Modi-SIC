import pandas as pd


def getSybmolTable(df):
    df_symbolTable = pd.DataFrame(columns=['LCounter', 'label'])
<<<<<<< HEAD
    # print(df_symbolTable)
=======
>>>>>>> 9f64a9836963c37b9d1dc221281f2bd72b17e1d8
    try:
        for i in df.index:
            if df['label'][i] != '':
                row = {'LCounter': str(df['LCounter'][i]), 'label': df['label'][i]}
                df_temp = pd.DataFrame([row])
                df_symbolTable = pd.concat([df_symbolTable, df_temp], axis=0, ignore_index=True)
<<<<<<< HEAD
        # df_symbolTable.set_index('Location_counter', inplace=True)
=======
>>>>>>> 9f64a9836963c37b9d1dc221281f2bd72b17e1d8
    except:
        print('Error')
    return df_symbolTable
