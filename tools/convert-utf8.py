def convert_to_utf8(input_file, output_file=None):
    """
    Convierte un archivo JSON a UTF-8 y reemplaza cualquier error de codificación.

    :param input_file: Ruta al archivo JSON original con posibles problemas de codificación.
    :param output_file: Ruta al archivo corregido y guardado como UTF-8.
    """
    if output_file is None:
        output_file = input_file

    try:
        # Abre el archivo en una codificación alternativa para tratar caracteres problemáticos
        with open(input_file, "r", encoding="latin-1", errors="replace") as f:
            content = f.read()

        # Vuelve a guardar el archivo como UTF-8
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Archivo convertido correctamente y guardado como: {output_file}")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

if __name__ == '__main__':
    # LLama a la función con las rutas del archivo original y el archivo de salida
    # convert_to_utf8(r"apps/api/fixtures/services.json")
    # convert_to_utf8(r"apps/api/fixtures/locations.json")
    # convert_to_utf8(r"apps/api/fixtures/hotels.json")
    convert_to_utf8(r"D:\Coders\harmonyhotel_service\apps\api\fixtures\socialplatform.json")
