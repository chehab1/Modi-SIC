import rsc.instructionSet as inst
import math


def immediateObjectCode(instruction, value, index):
    if len(value) == 1:
        raise Exception('Not Accurate value in intermediate file line -> ' + str(index+1))
    opcode = inst.Mnemonic[instruction][2:]
    # Code to convert hex to binary
    opcode_bin = "{0:08b}".format(int(opcode, 16))
    # change immediate flag to one
    opcode_bin = opcode_bin[0:7] + '1'
    # get the value
    address = value[1:]
    # convert value to hexadecimal
    address = hex(int(address))[2:]
    address_bin = "{0:016b}".format(int(address, 16))
    # concat the opcode to address
    objectCode = opcode_bin + address_bin
    # convert the binary to hex
    objectCode = hex(int(objectCode, 2))[2:]
    objectCode = objectCode.zfill(6)
    return objectCode
