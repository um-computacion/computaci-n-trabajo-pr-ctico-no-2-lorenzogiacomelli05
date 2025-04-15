def limpiar_texto(texto):
    texto = texto.lower()
    limpio = ""
    for letra in texto:
        if letra.isalnum():
            limpio += letra
    return limpio

def is_palindrome(texto):
    texto_limpio = limpiar_texto(texto)
    return texto_limpio == texto_limpio[::-1]

print("Ingresá una palabra o frase para verificar si es un palíndromo.")
print("Para salir del programa, presioná Ctrl+C.")

if __name__ == "__main__":
    while True:
        entrada = input(">> ")
        if is_palindrome(entrada):
            print(f'"{entrada}" es un palíndromo.')
        else:
            print(f'"{entrada}" no es un palíndromo.')

