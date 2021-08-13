import snap7
import snap7.client as c
from snap7.util import *
from snap7.types import *


def ReadMemory(plc,byte,bit,datatype):
    result = plc.read_area(areas['MK'], 0, byte, datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,bit)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

    #def as_tm_read(self, start: int, amount: int, data) -> bytearray:
        #result = self._library.Cli_AsTMRead(self._pointer, start, amount, byref(data))
        #check_error(result, context="client")
        #return result




if __name__=="__main__":
    plc = snap7.client.Client()
    plc.connect('192.168.0.1',0,1)
    timer = plc.read_area(areas["TM"], 1, 5, S7WLTimer)
    print(timer)

