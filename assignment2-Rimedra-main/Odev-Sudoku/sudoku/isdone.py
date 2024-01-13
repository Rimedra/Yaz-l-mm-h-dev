import json
import hashlib
import math

def _isdone(parms):
    result = {}
    
    if (not(_isCompleted(parms['grid']))):
        result['status'] = 'bitmemis'
        return result
    if (_isSolved(parms['grid'])):
        result['status'] = 'çözülmüs'
        return result
    return result

def _isCompleted(grid):
    isCompleted = True 
    for entry in grid:
        if entry == '0':
            isCompleted = False 
            return isCompleted
    return isCompleted


def _isSolved(grid):
    gridIsSolved = False 
    if (_isCompleted(grid)):
        if(_isGridCompliant(grid)):
            gridIsSolved = True 
            return gridIsSolved
    return gridIsSolved
