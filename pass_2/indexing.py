import pass_2.objectCode as objectCode
import rsc.instructionSet as inst


def handleIndexing(df, instruction, value):
    empty_dict = objectCode.df_to_dict(df)
    opcode = inst.Mnemonic[instruction][2:]
    # convert hex opcode to binary
    opcode_bin = "{0:08b}".format(int(opcode, 16))
    # convert value of address from hex to decimal
    address = empty_dict[value[0:len(value) - 2]]
    address_bin = "{0:016b}".format(int(address, 16))
    address_bin = '1' + address_bin[1:]
    object_code = opcode_bin + address_bin
    object_code = hex(int(object_code, 2))[2:]
    object_code = object_code.zfill(6)
    return object_code
