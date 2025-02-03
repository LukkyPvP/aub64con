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

def decoding_base65(num, decoding='utf-8'):
    try:
        return base64.b64decode(num).decode(decoding)
    except UnicodeDecodeError:
        return f"Ошибка: символ {num} не найден в {decoding}"

def coding_ascii(num, coding='utf-8'):
    try:
        return ord(num.encode(coding))
    except UnicodeEncodeError:
        return f"Ошибка: строка {str} не смогла закодироваться с помощью {coding}"

def coding_unicode(num, coding='utf-8'):
    try:
        if coding == "utf-8":
            return ord(num)
        else:
            return num.decode().encode(f'{coding}')
    except UnicodeEncodeError:
        return f"Ошибка: строка {num} не смогла закодироваться с помощью {coding}"

def coding_base65(num, coding='utf-8'):
    try:
        return base64.b64encode(num).encode(coding)
    except UnicodeDecodeError:
        return f"Ошибка: строка {num} не смогла закодироваться с помощью {coding}"

selectcodingordecoding = input("coding или decoding?: ")
if selectcodingordecoding == "decoding":
    selectdecoding = input("ASCII Type, Unicode или Base65?: ")
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
        base65decoding = input("Введите кодировку: ")
        print(decoding_base65(base65str, base65decoding))
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
        base65coding = input("Введите кодировку: ")
        print(coding_base65(base65str, base65coding))
