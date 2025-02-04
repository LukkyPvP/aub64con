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

def decoding_binary(text):
    return " ".join([str(int(b, 2)) for b in text.split()])

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

def coding_binary(text):
    textlist = [int(d) for d in text.split()]
    return " ".join([bin(d)[2:].zfill(11) for d in textlist])

selectcodingordecoding = input("coding или decoding?: ")
if selectcodingordecoding == "decoding":
    selectdecoding = input("ASCII Type, Unicode, Base65 или Binary?: ")
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
    elif selectdecoding == "Binary":
        binary = input("Введите бинарный код: ")
        print(decoding_binary(binary))
elif selectcodingordecoding == "coding":
    selectcoding = input("ASCII Type, Unicode, Base65 или Binary?: ")
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
    elif selectcoding == "Binary":
        binary = input("Введите двоичный код: ")
        print(coding_binary(binary))