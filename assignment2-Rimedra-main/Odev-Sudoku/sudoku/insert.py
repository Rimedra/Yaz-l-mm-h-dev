import hashlib
import json

def _insert(parms):
    result = {'status': 'ok'}

    if 'grid' in parms and 'position' in parms and 'value' in parms:
        grid = parms['grid']
        position = int(parms['position'])
        value = int(parms['value'])

        if 0 <= position < len(grid) and 1 <= value <= 9:
            if grid[position] == 0:
                grid[position] = value
                result['integrity'] = hashlib.sha256(json.dumps(grid).encode()).hexdigest()
            else:
                result['status'] = 'hata: pozisyon dolu'
        else:
            result['status'] = 'hata: yanlıs pozisyon ya da deger'
    else:
        result['status'] = 'hata: eksik parametre'

    return result
