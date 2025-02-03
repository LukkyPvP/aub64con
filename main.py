import base64

def decoding_ascii(text, decoding='utf-8'):
    try:
        return bytes(map(int, text.split())).decode(decoding)
    except (ValueError, UnicodeDecodeError) as e:
        return f"Ошибка: {e}"

def decoding_unicode(text, decoding='utf-8'):
    try:
        if decoding == "utf-8":
            return ''.join(chr(int(num)) for num in text.split())
        else:
            return text.encode().decode(f'{decoding}')
    except UnicodeDecodeError:
        return f"Ошибка: строка {text} не найдена в {decoding}"

def decoding_base65(text, decoding='utf-8'):
    try:
        return base64.b64decode(text).decode(decoding)
    except UnicodeDecodeError:
        return f"Ошибка: строка {text} не найдена в {decoding}"

def coding_ascii(text, coding='utf-8'):
    try:
        return ' '.join(str(ord(char)) for char in text.encode(coding).decode('latin1'))
    except UnicodeEncodeError:
        return f"Ошибка: строка {text} не смогла закодироваться с помощью {coding}"

def coding_unicode(text, coding='utf-8'):
    try:
        if coding == "utf-8":
            return ' '.join(str(ord(char)) for char in text)
        else:
            return text.decode().encode(f'{coding}')
    except UnicodeEncodeError:
        return f"Ошибка: строка {text} не смогла закодироваться с помощью {coding}"

def coding_base65(text, coding='utf-8'):
    try:
        return base64.b64encode(text.encode(coding)).decode('utf-8')
    except UnicodeDecodeError:
        return f"Ошибка: строка {text} не смогла закодироваться с помощью {coding}"

selectcodingordecoding = input("coding или decoding?: ")
if selectcodingordecoding == "decoding":
    selectdecoding = input("ASCII Type, Unicode или Base65?: ")
    if selectdecoding == "ASCII":
        text = input("Введите строку: ")
        decoding = input("Введите кодировку: ")
        print(decoding_ascii(text, decoding))
    elif selectdecoding == "Unicode":
        text = input("Введите строку: ")
        decoding = input("Введите кодировку: ")
        print(decoding_unicode(text, decoding))
    elif selectdecoding == "Base65":
        base65str = input("Введите Base65 строку: ")
        base65decoding = input("Введите кодировку: ")
        print(decoding_base65(base65str, base65decoding))
elif selectcodingordecoding == "coding":
    selectcoding = input("ASCII Type, Unicode or Base65?: ")
    if selectcoding == "ASCII":
        text = input("Введите строку: ")
        coding = input("Введите кодировку: ")
        print(coding_ascii(text, coding))
    elif selectcoding == "Unicode":
        text = input("Введите строку: ")
        coding = input("Введите кодировку: ")
        print(coding_unicode(text, coding))
    elif selectcoding == "Base65":
        base65str = input("Введите строку: ")
        base65coding = input("Введите кодировку: ")
        print(coding_base65(base65str, base65coding))
