import pandas as pd

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

print(df)
