# informacion de algun artista, pelicula, etc del agrado del usuario...

opcion = input("Ingresa el nombre de un artista, película o serie de tu preferencia: ").lower()

match opcion:
    case "mf doom":
        informacion = "MF DOOM fue un rapero y productor británico-estadounidense."
    case "nujabes":
        informacion = "Nujabes fue un productor y DJ japonés."
    case "avengers":
        informacion = "Pelicula de superhéroes del MCU"
    case "inception":
        informacion = "Pelicula de ciencia ficción dirigida por Christopher Nolan"
    case "breaking bad":
        informacion = "Serie de televisión estadounidense creada por Vince Gilligan."
    case "the sopranos":
        informacion = "Serie de televisión estadounidense creada por David Chase."
    case "frank zappa":
        informacion = "Frank Zappa fue un músico, compositor y productor estadounidense"
    case "the beatles":
        informacion = "Banda de rock británica formada en Liverpool en 1960"
    case "stranger things":
        informacion = "Serie de terror y ciencia ficción de Netflix"
    case _:
        informacion = "ERROR, no existe información sobre el artista, película o serie que ingresaste. Intenta con otro nombre."

print(f"Información: {informacion}")
