
import json
import hashlib
import math

def _solve(parms):
    result = {}
    if (not('grid' in parms)):
        result['status'] = 'hata: eksik grid'
        return result
    if (not('integrity' in parms)):
        result['status'] = 'hata: eksik integrity'
        return result
    if (not(_isValidGrid(parms['grid']))):
        result['status'] = 'hata: yanlıs grid'
        return result
  
    suggestedArray = _suggestSolution(parms['grid'])
    result['grid'] = suggestedArray
    result['status'] = 'ok'
 
    return result



def _isValidGrid(grid):
    isGrid = True
    for entry in grid:
        if (entry.isalpha()):
            isGrid = False
            return isGrid
    gridArray = json.loads(grid)
    if (len(gridArray) != 81):
        isGrid = False 
        return isGrid
    return isGrid



def _isCompleted(grid):
    isCompleted = True 
    for entry in grid:
        if entry == '0':
            isCompleted = False 
            return isCompleted
    return isCompleted







