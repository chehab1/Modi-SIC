import pandas as pd
import numpy as np

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
pd.set_option('display.max_rows', 100)

# Create intermediate file
with open('E:\\Term 7\\Systems programming\\Modi-SIC\\generated files\\intermediate_file.txt', 'a') as f:
    dfAsString = df.to_string(header=False, index=False)
    f.write(dfAsString)