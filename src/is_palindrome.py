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

