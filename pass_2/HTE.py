def fill(progName):
    if len(progName) == 6:
        return progName
    elif len(progName) > 6:
        raise Exception('Program Name Length is ' + str(len(progName)) + ' exceeds more than 6 bits')
    else:
        for i in range(len(progName), 6):
            progName += 'x'
    return progName


# put it in map
def df_to_dict(df):
    temp = {}
    for i in range(len(df)):
        if df.loc[i, 'objCode'] != '':
            temp[df.loc[i, 'objCode']] = df.loc[i, 'LCounter']
    return temp


def getTheHeader(df):
    header = 'H.'
    header += fill(df.loc[0, 'label']) + '.'
    header += df.loc[0, 'LCounter'].zfill(6) + '.'
    # get the length of program
    str = int(df.loc[0, 'LCounter'], 16)
    end = int(df.loc[len(df) - 1, 'LCounter'], 16)
    length = hex(end - str)[2:].zfill(6)
    header += length
    return header


def getHTE(df):
    header = getTheHeader(df)
    f = 0
    l = 1
    c = 0
    text = []
    temp = 'T'
    while l < len(df):
        inst = df.loc[l, 'inst']
        if inst == 'END':
            string = df.loc[f, 'LCounter'].zfill(6)
            temp = temp[:2] + string + temp[1:]
            str = int(df.loc[f, 'LCounter'], 16)
            end = int(df.loc[len(df)-1, 'LCounter'], 16)
            length = hex(end - str)[2:].zfill(2)
            temp = temp[:8] + '.' + length + '.' + temp[9:]
            text.append(temp)
            f = l+1
            l += 1
            c = 0
            temp = 'T'
        elif inst == 'RESW' or inst == 'RESB':
            string = df.loc[f, 'LCounter'].zfill(6)
            temp = temp[:2] + string + temp[1:]
            str = int(df.loc[f, 'LCounter'], 16)
            end = int(df.loc[l, 'LCounter'], 16)
            length = hex(end - str)[2:].zfill(2)
            temp = temp[:8] + '.' + length + '.' + temp[9:]
            text.append(temp)
            f = l+1
            l = f
            c = 0
            temp = 'T'
        elif c == 10:
            string = df.loc[f, 'LCounter'].zfill(6)
            temp = temp[:2] + string + temp[1:]
            str = int(df.loc[f, 'LCounter'], 16)
            end = int(df.loc[l, 'LCounter'], 16)
            length = hex(end - str)
            if len(length) > 4:
                length = length[4:].zfill(2)
            else:
                length = length[2:].zfill(2)
            temp = temp[:8] + '.' + length + '.' + temp[9:]
            # print(temp)
            text.append(temp)
            f = l
            c = 0
            temp = 'T'
        else:
            temp += '.' + df.loc[l, 'objCode'].zfill(6)
            # print(temp)
            c += 1
            l += 1

    text = [i for i in text if len(i) > 11]
    End = 'E' + '.' + df.loc[1, 'LCounter'].zfill(6)

    #change it to string
    textRecord = ''
    for i in text:
        textRecord += i + '\n'
    hteRecord = header + '\n' + textRecord + End
    return hteRecord
