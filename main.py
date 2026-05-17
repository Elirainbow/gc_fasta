def leer_fasta(ruta_archivo):
    """Lee un archivo FASTA y concatena todas las secuencias de DNA.

    Esta función lee un archivo en formato FASTA, ignorando las líneas de
    encabezado (que comienzan con '>'), y concatena todas las líneas de
    secuencia en un único string.

    Args:
        ruta_archivo (str): Ruta del archivo FASTA a leer.

    Returns:
        str: String con todas las secuencias de DNA concatenadas.
    """
    secuencias = {}
    id_actual = None

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if linea.startswith(">"):
                id_actual = linea[1:]  # Elimina el '>' del identificador
                secuencias[id_actual] = ""  # Inicializa la secuencia para este ID
            else:
                if not linea.startswith(">"):
                    secuencias[
                        id_actual
                    ] += linea  # La variable `secuencia` es un string, es decir, una cadena de texto. Estaamos concatenando strings.
    return secuencias


secuencias = leer_fasta("secuencia.fasta")
# print(secuencias)


def calcular_gc(secuencia):
    """Calcula el porcentaje de bases G y C en una secuencia de DNA.

    Cuenta el número de bases G (guanina) y C (citosina) en la secuencia
    y calcula qué porcentaje representan del total de nucleótidos.
    Esta es una métrica importante para caracterizar secuencias de DNA.

    Args:
        secuencia (str): variable que contiene la secuencia de DNA
        (esperada en mayúsculas) concatenada en la función leer_fasta.

    Returns:
        float: Porcentaje de GC en la secuencia (0-100).
    """

    cantidad_g = secuencia.count("G")
    cantidad_c = secuencia.count("C")

    gc = cantidad_c + cantidad_g
    longitud = len(secuencia)
    porcentaje_gc = gc / longitud * 100
    return porcentaje_gc


# resultado = calcular_gc("GGGGTTTT")
# print(resultado)


def main():
    """Función principal que integra la lectura FASTA y el cálculo de GC.

    Lee una secuencia de DNA desde un archivo FASTA y calcula el porcentaje
    de contenido GC, mostrando el resultado en la consola con dos decimales
    de precisión.

    Returns:
        None: Solo imprime el resultado en consola.
    """

    ruta_archivo = "secuencia.fasta"
    secuencias = leer_fasta(ruta_archivo)

    for identificador, secuencia in secuencias.items():
        contenido_gc = calcular_gc(secuencia)

        print(f"{identificador}: {contenido_gc:.2f}% GC")


if __name__ == "__main__":
    main()

# > Si este archivo se está ejecutando directamente como programa principal, entonces llama a `main()`.
