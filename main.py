import base64

def decoding_ascii(num, decoding='utf-8'):
    try:
        return bytes([num]).decode(decoding)
    except UnicodeDecodeError:
        return f"Ошибка: символ {num} не найден в {decoding}"

def decoding_unicode(num, decoding='utf-8'):
    try:
        if decoding == "utf-8":
            return chr(int(num))
        else:
            return num.encode().decode(f'{decoding}')
    except UnicodeDecodeError:
        return f"Ошибка: символ {num} не найден в {decoding}"

def coding_ascii(num, coding='utf-8'):
    try:
        return ord(num.encode(coding))
    except UnicodeDecodeError:
        return f"Ошибка: символ {str} не найден в {coding}"

def coding_unicode(num, coding='utf-8'):
    try:
        if coding == "utf-8":
            return ord(num)
        else:
            return num.decode().encode(f'{coding}')
    except UnicodeDecodeError:
        return f"Ошибка: символ {num} не найден в {coding}"

selectcodingordecoding = input("coding or decoding?: ")
if selectcodingordecoding == "decoding":
    selectdecoding = input("ASCII Type, Unicode or Base65?: ")
    if selectdecoding == "ASCII":
        shar = int(input("Введите символ: "))
        decoding = input("Введите кодировку: ")
        print(decoding_ascii(shar, decoding))
    elif selectdecoding == "Unicode":
        shar = input("Введите символ: ")
        decoding = input("Введите кодировку: ")
        print(decoding_unicode(shar, decoding))
    elif selectdecoding == "Base65":
        base65str = input("Введите Base65 строку: ")
        print(base64.b64decode(base65str).decode('windows-1251'))
elif selectcodingordecoding == "coding":
    selectcoding = input("ASCII Type, Unicode or Base65?: ")
    if selectcoding == "ASCII":
        shar = input("Введите символ: ")
        coding = input("Введите кодировку: ")
        print(coding_ascii(shar, coding))
    elif selectcoding == "Unicode":
        shar = input("Введите символ: ")
        coding = input("Введите кодировку: ")
        print(coding_unicode(shar, coding))
    elif selectcoding == "Base65":
        base65str = input("Введите строку: ")
        print(base64.b64encode(base65str.encode('windows-1251')))
