print ("----- Inicio del programa ------")

edad1 = int(input("Cual es tu edad "))


if edad1 > 18:
    print ("Eres mayor de edad")
    print ("--------------------------------")
    print ("----- Modulo de seguridad ------")

    #Despues de establecer si es mayor de edad, le solicitamos una contraseña 

    print ("Su contraseña fue enviada a su correo")
    ClaveMayorEdad = "contraseña"
    password = input("Por favor digita tu clave ")

    if ClaveMayorEdad ==  password.lower ():
        print ("Contraseña correcta :)")
    else:    
        print ("Contraseña incorrecta :(")

    print ("--------------------------------")
    print("----- Módulo de interacción ------")

    validacion = input("¿Quieres cambiar tu contraseña? (Si / No): ")

    if validacion.lower() == "si":
        nueva_contraseña = input("Escribe tu nueva contraseña: ")
        clave_mayor_edad = nueva_contraseña
        print("Contraseña cambiada exitosamente.")
    else:
        print("Escribe una frase o palabra para continuar con la autenticación.")
        frase = input("Introduce tu palabra o frase: ")
else:    
    print ("Eres menor de edad")






