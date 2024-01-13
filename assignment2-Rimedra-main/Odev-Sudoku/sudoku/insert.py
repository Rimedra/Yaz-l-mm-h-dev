import hashlib
import json

def _insert(parameters):
    result = {'status': 'ok'}

    if 'cell' not in parameters:
        result['status'] = 'hata: eksik hücre adresi'
        return result
    if len(parameters['cell']) != 4:
        result['status'] = 'hata: geçersiz hücre adresi'
        return result
    if not parameters['cell'][1].isnumeric() or not parameters['cell'][3].isnumeric():
        result['status'] = 'hata: geçersiz hücre adresi'
        return result
    if parameters['cell'][0] not in ('r', 'R') or parameters['cell'][2] not in ('c', 'C'):
        result['status'] = 'hata: geçersiz hücre adresi'
        return result 
    if int(parameters['cell'][1]) < 1 or int(parameters['cell'][3]) < 1:
        result['status'] = 'hata: geçersiz hücre adresi'
        return result
    
    if 'grid' not in parameters:
        result['status'] = 'hata: eksik grid'
        return result
    if not _is_valid_grid(parameters['grid']):
        result['status'] = 'hata: geçersiz grid'
        return result
    
    row_number = int(parameters['cell'][1])
    column_number = int(parameters['cell'][3])

    if _is_cell_a_hint(parameters['grid'], row_number, column_number):
        result['status'] = 'hata: sabit olarak belirlenmiş bir hücreye değer ekleme girişiminde bulunuldu'
        return result

    if 'value' in parameters:
        return_grid = _insert_value(parameters['grid'], int(parameters['value']), row_number, column_number)
        result['grid'] = return_grid
        result['status'] = 'ok'
        grid_to_hash = json.dumps(return_grid)
        result['integrity'] = _calculate_hash(grid_to_hash)
    else:
        result['status'] = 'hata: eksik parametre'

    return result

def _is_cell_a_hint(grid, row, column):
    is_hint = False
    grid_array = json.loads(grid)
    index_in_grid = (9 * (row - 1)) + (column - 1)
    if int(grid_array[index_in_grid]) < 0:
        is_hint = True 
    return is_hint

def _insert_value(grid, value, row, col):
    grid_array = json.loads(grid)
    index_in_grid = (9 * (row - 1)) + col
    grid_array[index_in_grid - 1] = value
    return grid_array

def _calculate_hash(grid):
    matrix = [[0 for row_num in range(9)] for col_num in range(9)]
    str_to_be_hashed = ""
    grid_array = json.loads(grid)
    grid_index = 0
    for row_index in range(9):
        for col_index in range(9):
            matrix[row_index][col_index] = grid_array[grid_index]
            grid_index += 1
    for col_index in range(9):
        for row_index in range(9):
            str_to_be_hashed += str(matrix[row_index][col_index])
    hash_value = hashlib.sha256()
    encoded_str = str_to_be_hashed.encode()
    hash_value.update(encoded_str)
    str_to_return = hash_value.hexdigest()
    return str_to_return

def _is_valid_grid(grid):
    is_grid = True
    for entry in grid:
        if entry.isalpha():
            is_grid = False
            break
    grid_array = json.loads(grid)
    if len(grid_array) != 81:
        is_grid = False 
    return is_grid
