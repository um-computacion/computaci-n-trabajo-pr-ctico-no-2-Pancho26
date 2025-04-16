def comparar_caracteres(texto: str) -> bool:

    return texto == texto[::-1]

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
    return comparar_caracteres(texto_limpio)


if __name__ == "__main__":
        frase = input("Ingresá una palabra o frase: ")
        if is_palindrome(frase):
            print("Es un palíndromo.")
        else:
            print(" No es un palíndromo.")

