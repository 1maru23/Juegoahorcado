import random

PALABRAS = [
    "PYTHON",
    "COMPUTADORA",
    "AHORCADO",
    "UNIVERSIDAD",
    "SEGURIDAD",
    "PROGRAMACION",
    "ESTUDIANTE",
    "CIBERSEGURIDAD"
]

# Número máximo de intentos fallidos permitidos
MAX_INTENTOS = 6


# -----------------------------
# FUNCIONES DEL JUEGO
# -----------------------------

def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n==============================")
    print("      JUEGO DEL AHORCADO      ")
    print("==============================")
    print("1. Jugar")
    print("2. Ver instrucciones")
    print("0. Salir")
    print("==============================")


def mostrar_instrucciones():
    """
    Muestra las instrucciones básicas del juego.
    """
    print("\nINSTRUCCIONES:")
    print("- El sistema elige una palabra secreta al azar.")
    print("- Debes adivinar la palabra letra por letra.")
    print("- Cada vez que fallas, pierdes un intento.")
    print(f"- Si llegas a {MAX_INTENTOS} intentos fallidos, pierdes la partida.")
    print("- Si completas la palabra antes de quedarte sin intentos, ganas.")
    print("- Solo se pueden ingresar letras, no números ni símbolos.")


def elegir_palabra():
    """
    Elige y retorna una palabra al azar de la lista PALABRAS.
    """
    return random.choice(PALABRAS)


def dibujar_ahorcado(intentos_fallidos):
    """
    Dibuja una representación simple del ahorcado en función
    de la cantidad de intentos fallidos.
    Esto ayuda a visualizar el avance del juego.

    Esta función es una de las más "complejas" visualmente,
    por eso se deja bien separada y clara.
    """
    etapas = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]

    # Nos aseguramos de no salirnos del rango de la lista
    indice = min(intentos_fallidos, len(etapas) - 1)
    print(etapas[indice])


def mostrar_estado_juego(palabra_secreta, letras_adivinadas, intentos_fallidos):
    """
    Muestra el estado actual del juego:
    - Palabra con letras adivinadas y guiones bajos.
    - Letras utilizadas.
    - Intentos restantes.
    - Dibujo del ahorcado.
    """
    # Construimos la palabra mostrando solo las letras que ya se adivinaron
    estado_palabra = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            estado_palabra += letra + " "
        else:
            estado_palabra += "_ "

    print("\nPalabra: ", estado_palabra)
    print("Letras adivinadas: ", " ".join(sorted(letras_adivinadas)) if letras_adivinadas else "-")
    print(f"Intentos fallidos: {intentos_fallidos} / {MAX_INTENTOS}")
    dibujar_ahorcado(intentos_fallidos)


def pedir_letra(letras_usadas):
    """
    Pide al usuario que ingrese una letra válida.
    Valida que:
    - Sea una única letra.
    - Sea alfabética.
    - No se haya usado antes.
    """
    while True:
        letra = input("Ingresa una letra: ").strip().upper()

        # Estructura lógica para validar entrada
        if len(letra) != 1:
            print("✋ Debes ingresar solo UNA letra.")
        elif not letra.isalpha():
            print("✋ Solo se permiten letras (no números ni símbolos).")
        elif letra in letras_usadas:
            print("⚠ Esa letra ya la usaste, intenta con otra.")
        else:
            return letra


def jugar_partida():
    """
    Controla el flujo completo de una partida del ahorcado.
    Esta función integra:
    - Selección de palabra.
    - Bucle principal del juego (estructura repetitiva).
    - Uso de estructuras lógicas (if/else) para decidir
      qué ocurre en cada intento.
    """
    palabra_secreta = elegir_palabra()
    letras_adivinadas = set()
    letras_usadas = set()
    intentos_fallidos = 0

    print("\n¡Nueva partida de Ahorcado!")
    # Bucle principal: se repite hasta que el jugador gane o pierda
    while True:
        mostrar_estado_juego(palabra_secreta, letras_adivinadas, intentos_fallidos)

        # Verificamos condiciones de fin de juego
        # 1. Si ya adivinó todas las letras
        todas_adivinadas = all(letra in letras_adivinadas for letra in palabra_secreta)
        if todas_adivinadas:
            print("\n🎉 ¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break

        # 2. Si ya se alcanzó el máximo de intentos
        if intentos_fallidos >= MAX_INTENTOS:
            print("\n💀 Has perdido. La palabra era:", palabra_secreta)
            break

        # Pedimos una nueva letra al usuario
        letra = pedir_letra(letras_usadas)
        letras_usadas.add(letra)

        # Estructura lógica para saber si la letra está en la palabra
        if letra in palabra_secreta:
            print("✅ ¡Bien! La letra está en la palabra.")
            letras_adivinadas.add(letra)
        else:
            print("❌ La letra NO está en la palabra.")
            intentos_fallidos += 1


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------

def main():
    """
    Función principal del programa.
    Contiene el menú y el ciclo general de la aplicación.
    """
    opcion = ""

    # Bucle principal del sistema: se repite hasta que el usuario elija salir.
    while opcion != "0":
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        # Estructuras lógicas para controlar el flujo según la opción
        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            mostrar_instrucciones()
        elif opcion == "0":
            print("\nSaliendo del juego... ¡Hasta pronto!")
        else:
            print("\nOpción no válida. Intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
