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
    header += df.loc[1, 'LCounter'].zfill(6) + '.'
    # get the length of program
    str = int(df.loc[1, 'LCounter'], 16)
    end = int(df.loc[len(df) - 1, 'LCounter'], 16)
    length = hex(end - str)[2:].zfill(6)
    header += length
    return header


def getHTE(df):
    header = getTheHeader(df)
    f = 0
    l = 1
    text = []
    temp = 'T'
    while l < len(df):
        inst = df.loc[l, 'inst']
        # check if the pointer is in START program or not
        if f == 0:
            string = df.loc[f + 1, 'LCounter'].zfill(6)
            str = int(df.loc[f + 1, 'LCounter'], 16)
        else:
            str = int(df.loc[f, 'LCounter'], 16)
            string = df.loc[f, 'LCounter'].zfill(6)
        end = int(df.loc[l, 'LCounter'], 16)
        length = hex(end - str)
        diff = int(length, 16) - int('1E', 16)

        if inst == 'END':
            string = df.loc[f, 'LCounter'].zfill(6)
            temp = temp[:2] + string + temp[1:]
            str = int(df.loc[f, 'LCounter'], 16)
            end = int(df.loc[len(df) - 1, 'LCounter'], 16)
            length = hex(end - str)[2:].zfill(2)
            temp = temp[:8] + '.' + length + '.' + temp[9:]
            text.append(temp)
            break

        elif inst == 'RESW' or inst == 'RESB':
            temp = temp[:2] + string + temp[1:]
            length = hex(end - str)[2:].zfill(2)
            temp = temp[:8] + '.' + length + '.' + temp[9:]
            text.append(temp)
            f = l + 1
            l = f
            temp = 'T'
        # if the length between two pointers are equal or more than 1E
        elif diff >= 0:
            temp = temp[:2] + string + temp[1:]
            if diff > 0:
                end = int(df.loc[l - 1, 'LCounter'], 16)
                length = hex(end - str)
                temp = temp[0: len(temp) - 7]
                l -= 1
            if len(length) > 4:
                length = length[4:].zfill(2)
            else:
                length = length[2:].zfill(2)
            temp = temp[:8] + '.' + length + '.' + temp[9:]
            # print(temp)
            text.append(temp)
            f = l
            temp = 'T'

        # if length less than 1E
        else:
            temp += '.' + df.loc[l, 'objCode']
            l += 1

    text = [i for i in text if len(i) > 11]
    End = 'E' + '.' + df.loc[1, 'LCounter'].zfill(6)

    # change it to string
    textRecord = ''
    for i in text:
        textRecord += i + '\n'
    hteRecord = header + '\n' + textRecord + End
    return hteRecord
