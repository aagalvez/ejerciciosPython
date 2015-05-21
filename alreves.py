txt = input("Teclea una palabra o frase: ")
i = -1
contador = len(txt)
invertir = ""
while contador > 0:
        invertir += txt[i]
        contador -= 1
        i -= 1
print(invertir)
