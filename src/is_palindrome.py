def is_palindrome(texto):
    texto_limpio = limpiar_texto(texto)
    return texto_limpio == texto_limpio[::-1]
