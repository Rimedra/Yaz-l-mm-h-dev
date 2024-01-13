import hashlib
import json

def _isValidGrid(grid):
    isGrid = True
    for entry in grid:
        if entry.isalpha():
            isGrid = False
            return isGrid
    gridArray = json.loads(grid)
    if len(gridArray) != 81:
        isGrid = False 
        return isGrid
    return isGrid

def _insert(parms):
    result = {'status': 'ok'}
    
  
    if 'cell' not in parms:
        result['status'] = 'error: eksik hücre adresi'
        return result
    if len(parms['cell']) != 4:
        result['status'] = 'error: geçersiz hücre adresi'
        return result
    if not parms['cell'][1].isnumeric() or not parms['cell'][3].isnumeric():
        result['status'] = 'error: geçersiz hücre adresi'
        return result
    if parms['cell'][0] not in ('r', 'R') or parms['cell'][2] not in ('c', 'C'):
        result['status'] = 'error: geçersiz hücre adresi'
        return result 
    if int(parms['cell'][1]) < 1 or int(parms['cell'][3]) < 1:
        result['status'] = 'error: geçersiz hücre adresi'
        return result

    if 'grid' not in parms:
        result['status'] = 'error: eksik grid'
        return result
    if not _isValidGrid(parms['grid']):
        result['status'] = 'error: geçersiz grid'
        return result
    
    rowNumber = int(parms['cell'][1])
    columnNumber = int(parms['cell'][3])

    if _isCellAHint(parms['grid'], rowNumber, columnNumber):
        result['status'] = 'error: sabit olarak belirlenmiş bir hücreye değer ekleme girişiminde bulunuldu'
        return result

    if 'value' in parms:
        returnGrid = _insertValue(parms['grid'], int(parms['value']), rowNumber, columnNumber)
        result['grid'] = returnGrid
        result['status'] = 'ok'
        gridToHash = json.dumps(returnGrid)
        result['integrity'] = _calculateHash(gridToHash)
    else:
        result['status'] = 'error: eksik parametre'

    return result

