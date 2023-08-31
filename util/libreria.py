import json
import subprocess


def read_metadata_exiftool(file_path):
    metadatos = {}  # Diccionario para almacenar los metadatos

    try:
        # Ejecuta exiftool en el archivo y obtiene la salida como JSON
        cmd = ["exiftool", "-json", file_path]
        output = subprocess.check_output(cmd, text=True)

        # Parsea la salida JSON
        metadata = json.loads(output)[0]

        # Extrae los datos de GPS y Fecha
        raw_gps_data = metadata.get("GPSLatitude", "").split(" ")
        gps_latitude_coor = [raw_gps_data[0], raw_gps_data[2].replace("'", ""), raw_gps_data[3].replace('"', "")]
        gps_latitude_ref = [raw_gps_data[4]]

        raw_gps_data = metadata.get("GPSLongitude", "").split(" ")
        gps_longitude_coor = [raw_gps_data[0], raw_gps_data[2].replace("'", ""), raw_gps_data[3].replace('"', "")]
        gps_longitude_ref = [raw_gps_data[4]]

        raw_date = metadata.get("FileModifyDate", "")

        # Agrega los datos al diccionario de metadatos
        metadatos["GPSLatitude"] = gps_latitude_coor
        metadatos["GPSLatitudeRef"] = gps_latitude_ref
        metadatos["GPSLongitude"] = gps_longitude_coor
        metadatos["GPSLongitudeRef"] = gps_longitude_ref
        metadatos["FileModifyDate"] = raw_date

        return metadatos

    except Exception as e:
        print(f"😱 Error al leer los metadatos del archivo {file_path}: {e}")


def convert_to_decimal(coord):
    try:
        degrees = coord.values[0].num / coord.values[0].den
        minutes = coord.values[1].num / coord.values[1].den / 60
        seconds = coord.values[2].num / coord.values[2].den / 3600
        decimal_coord = degrees + minutes + seconds
        return decimal_coord

    except Exception as e:
        print(f"😱 Error al convertir las coordenadas a decimal: {e}")
        return None  # Valor por defecto en caso de error


def convert_to_decimal_heic(coord):
    try:
        degrees = float(coord[0])
        minutes = float(coord[1]) / 60
        seconds = float(coord[2]) / 3600
        decimal_coord = degrees + minutes + seconds
        return decimal_coord

    except Exception as e:
        print(f"😱 Error al convertir las coordenadas a decimal: {e}")
        return None  # Valor por defecto en caso de error
