import os
import sys


def select_mode(mode: str):
    """Returns the mode chosen the user
    
    Args:
    mode -- user request
    Return: Returns the mode chosen the user
    """
    
    mode_list = {
        "1": ['cyr-lat', 'Cyr-Lat', 'CYR-LAT', '1', 'Cyril', 'CYRIL', 'cyril' 'кир-лат', 'Кир-Лат', 'КИР-ЛАТ', 'КИРИЛИЦЯ', 'кирилиця', 'Кирилиця'],
        "2": ['lat-cyr', 'Lat-Cyr', 'LAT-CYR', '2', 'Latin', 'LATIN', 'lantin', 'лат-кир', 'Лат-Кир', 'ЛАТ-КИР', 'ЛАТИНИЦЯ', 'латиниця', 'Латиниця']
    }
    
    for k in mode_list:
        for i in mode_list["%s" % k]:
            if mode == i:
                return k
    else:
        return f'File "{os.path.abspath(__file__)}", ValueError: Such a mode does not exist'


def convert(mode: int, value: str):
    lat_cyr = {
        'a': 'а',
        'b': 'б',
        'v': 'в',
        'g': 'г',
        'ĝ': 'ґ',
        'd': 'д',
        'e': 'е',
        'je': 'є',
        'z': 'з',
        'ž': 'ж',
        'y': 'и',
        'i': 'і',
        'ji': 'ї',
        'j': 'й',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'o': 'о',
        'p': 'п',
        'r': 'р',
        's': 'с',
        't': 'т',
        'u': 'у',
        'f': 'ф',
        'h': 'х',
        'c': 'ц',
        'č': 'ч',
        'š': 'ш',
        'šč': 'щ',
        '\'': 'ь',
        'ju': 'ю',
        'ja': 'я',
        'A': 'А',
        'B': 'Б',
        'V': 'В',
        'G': 'Г',
        'Ĝ': 'Ґ',
        'D': 'Д',
        'E': 'Е',
        'JE': 'Є',
        'Z': 'З',
        'Ž': 'Ж',
        'Y': 'И',
        'I': 'І',
        'JI': 'Ї',
        'J': 'Й',
        'K': 'К',
        'L': 'Л',
        'M': 'М',
        'N': 'Н',
        'O': 'О',
        'P': 'П',
        'R': 'Р',
        'S': 'С',
        'T': 'Т',
        'U': 'У',
        'F': 'Ф',
        'H': 'Х',
        'C': 'Ц',
        'Č': 'Ч',
        'Š': 'Ш',
        'ŠČ': 'Щ',
        'JU': 'Ю',
        'JA': 'Я'
    }
    cyr_lat = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'ґ': 'ĝ',
        'д': 'd',
        'е': 'e',
        'є': 'je',
        'з': 'z',
        'ж': 'ž',
        'и': 'y',
        'і': 'i',
        'ї': 'ji',
        'й': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'č',
        'ш': 'š',
        'щ': 'šč',
        'ь': '\'',
        'ю': 'ju',
        'я': 'ja',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Ґ': 'Ĝ',
        'Д': 'D',
        'Е': 'E',
        'Є': 'JE',
        'З': 'Z',
        'Ж': 'Ž',
        'И': 'Y',
        'І': 'I',
        'Ї': 'JI',
        'Й': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'C',
        'Ч': 'Č',
        'Ш': 'Š',
        'Щ': 'ŠČ',
        'Ю': 'JU',
        'Я': 'JA'
    }
    
    mode_list = {
        "1": ['cyr-lat', 'Cyr-Lat', 'CYR-LAT', '1', 'Cyril', 'CYRIL', 'cyril' 'кир-лат', 'Кир-Лат', 'КИР-ЛАТ', 'КИРИЛИЦЯ', 'кирилиця', 'Кирилиця'],
        "2": ['lat-cyr', 'Lat-Cyr', 'LAT-CYR', '2', 'Latin', 'LATIN', 'lantin', 'лат-кир', 'Лат-Кир', 'ЛАТ-КИР', 'ЛАТИНИЦЯ', 'латиниця', 'Латиниця']
    }
    
    for k in mode_list:
        for i in mode_list["%s" % k]:
            if mode == i:
                mode =  k

    if mode == 1:
        for key in cyr_lat:
            value = value.replace(key, cyr_lat[key])
        return value
    else:
        for key in lat_cyr:
            value = value.replace(key, lat_cyr[key])
        return value


def main():
    while True:
        user_mode = input("Enter mode: ")
        mode_user_result = f'File "{os.path.abspath(__file__)}", ValueError: Such a mode does not exist'
        
        if select_mode(user_mode) == mode_user_result:
            sys.exit(mode_user_result)

        value = str(input("Enter text for conversion: "))
        var = ''.join(convert(int(select_mode(user_mode)), value))
        print(var)
    
if __name__ == "__main__":
    main()
    