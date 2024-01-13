import sudoku.create as create
import sudoku.insert as insert
import sudoku.isdone as isdone
import sudoku.solve as solve

ERROR01 = 'hata: islem belirtilmedi'
ERROR02 = 'hata: girilen parametreler bir sozluk degil'
ERROR03 = 'hata: gecerli bir islem degil'
STATUS = 'status'
OP = 'op'
OPS = {
    'create' : create._create,
    'isdone' : isdone._isdone,
    'insert' : insert._insert,
    'solve' : solve._solve,
    }

def _dispatch(parms = None):

    result = {}
    
   
    if(parms == None):
        result = {STATUS: ERROR01}
    elif(not(isinstance(parms, dict))):
        result = {STATUS: ERROR02}
    elif (not(OP in parms)):
        result = {STATUS: ERROR01}
    elif(not(parms[OP] in OPS)):
        result[STATUS] = ERROR03
    else:
        result = OPS[parms[OP]](parms)
    return result
