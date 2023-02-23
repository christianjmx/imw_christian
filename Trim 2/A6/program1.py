import sys


def count_words(sentence):
    summary = {}
    palabras = sentence.split(" ")

    for palabra in palabras:
        if palabra in summary:
            summary[palabra] += 1
        else:
            summary[palabra] = 1
    return summary

if __name__ == '__main__':
    sentence = sys.argv[1]
    # Esto es opcional:
    # La varibale quitar es para que no cuente lo caracteres que le digamos

    quitar = ",;:.\n!"
    for caracter in quitar:
        sentence = sentence.replace(caracter,"")

    sentence = sentence.lower()
    # Y este es para para dejarlo todo el minuscula porque la misma letra en mayuscula y miniscula cuentan como diferentes

    r = count_words(sentence)
    for palabra, x in r.items():
        print(f'{palabra}:{x}')