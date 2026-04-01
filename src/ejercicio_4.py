# Valide una dirección de email ingresada por el usuario con los siguientes
# criterios:
# Contiene exactamente un @.
# Tiene al menos un carácter antes del @.
# Tiene al menos un punto (.) después del @.
# No empieza ni termina con @ ni con ..
# La parte después del último punto tiene al menos 2 caracteres (el dominio).

while True:
    mail = input("Ingrese un email: ")
    if mail.count("@") == 1:
        pos = mail.index("@")
        if (pos > 0) and ("." in mail[pos:]):
            if not (mail.endswith("@") or mail.endswith(".") or mail.startswith(".")):
                if ((len(mail)-mail.rfind(".")-1) >= 2):
                    print("El email es válido.")
                    break
    print("El email no es válido.")
    
    
