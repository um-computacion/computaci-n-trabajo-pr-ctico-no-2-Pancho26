def is_palindrome(frase: str) -> bool:
    frase = frase.lower()
    frase = (
        frase.replace("á", "a")
             .replace("é", "e")
             .replace("í", "i")
             .replace("ó", "o")
             .replace("ú", "u")
    )

    
    texto_limpio = ""
    letras_validas = "abcdefghijklmnopqrstuvwxyz0123456789"
    for letra in frase:
        if letra in letras_validas:
            texto_limpio += letra
    return texto_limpio == texto_limpio[::-1]

    
