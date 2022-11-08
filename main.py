import pandas as pd
from pass_1 import locationCounter, symbolTable
from pass_2 import objectCode

labels = []
insts = []
values = []

data = {
    'label': labels,
    'inst': insts,
    'value': values
}
f = open('rsc\\inputs\\input_program.txt', 'r')

for line in f.readlines():
    temp = line.split('\t')
    if temp[1] == '.\n' or temp[1] == '.':
        continue
    else:
        labels.append(temp[1])
        insts.append(temp[2])
        t = temp[3]
        if t[len(t) - 1:len(t)] == '\n':
            values.append(t[0:-1])
        else:
            values.append(t)

df = pd.DataFrame(data)

# to get intermediate file
f = open('generated files\\intermediate_file.txt', 'w')
dfAsString = df.to_string(header=False, index=False)
f.write(dfAsString)
f.close()

# to get location counter
df = locationCounter.insert_LC(df)
f = open('generated files\\location_counter.txt', 'w')
dfAsString = df.to_string(header=False, index=False)
f.write(dfAsString)
f.close()
# to get symbol_table
df_symbolTable = symbolTable.getSybmolTable(df)
f = open('generated files\\symbol_table.txt', 'w')
dfAsString = df_symbolTable.to_string(header=False, index=False)
f.write(dfAsString)
f.close()

# OBJECT CODE
df_objectCode = objectCode.getObjectCode(df)
f = open('generated files\\out_pass2.txt', 'w')
dfAsString = df_objectCode.to_string(header=False, index=False)
f.write(dfAsString)
f.close()

print(df_objectCode)
