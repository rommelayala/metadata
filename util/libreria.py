import csv
import json
import os
import subprocess

import exifread
from PIL import Image


def get_metadata_del_map(nombre_carpeta):
    try:
        contenido = os.listdir(nombre_carpeta)
        metadata_map = {}

        '''
        Lee directorio y construye un diccionario con los metadatos de todos los archivos
        '''
        for archivo in contenido:
            image_path = os.path.join(nombre_carpeta, archivo)
            metadata = get_archivo_metadata(image_path, archivo)
            metadata_map[archivo] = metadata

        return metadata_map

    except Exception as e:
        print(f"😱 Error al crear el mapa de metadatos: {e}")
        return {}


def get_archivo_metadata(file_path, archivo):
    """
    Lee los metadatos de un archivo de imagen.

    Args:
        file_path (str): La ruta al archivo de imagen.

    Returns:
        dict: Un diccionario con los metadatos del archivo.
    """
    try:
        metadata = {}

        _, extension = os.path.splitext(file_path)

        if extension.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
            with open(file_path, 'rb') as f:
                metadata = exifread.process_file(f)

        elif extension.lower() == '.heic':
            metadata = read_heic_metadata(file_path)

        return metadata
    except Exception as e:
        print(f"😱 Error al leer los metadatos del archivo {file_path}: {e}")
        return {}


def create_csv_from_map(metadata_map, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Archivo', 'Tag', 'Latitud', 'Longitud', 'Fecha'])  # Cabecera

            for archivo, metadata in metadata_map.items():
                # 00B95CE1-D794-47D7-8565-CF91FD73EFB8_1_105_c
                # if '0B8F2BB9-4598-4F80-8DF7-096F30C62A28' in archivo:
                print(f"Archivo: {archivo}")
                # for tag, value in metadata.items():
                # print(f"El tag es {tag}")
                # Obtiene el GPS coordenadas desde los metadatos
                gps_data = process_gps_metadata(metadata, archivo)
                if gps_data is not None:
                    gps_latitude, gps_longitude, date = gps_data
                    row_data = [archivo, 'GPS Coordinates', '', gps_latitude, gps_longitude, date]
                    csv_writer.writerow(row_data)
                    print(f"Latitud/Longitud: {gps_latitude}, {gps_longitude}, Fecha: {date}")
                    '''
                    else:
                        row_data = [nombre_archivo, tag, str(value), '', '']
                        csv_writer.writerow(row_data)
                        print(f"tag: {tag} -- value: {value}")
                    '''
                else:
                    print(f"XXXX EL archivo {archivo} tiene coord Latitud/Longitud: {gps_latitude}, {gps_longitude}, Fecha: {date}")

    except Exception as e:
        print(f"😱 Error al crear el archivo {archivo} CSV de metadatos {metadata} "
              f":ERROR {e}")


def read_heic_metadata(file_path):
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

        print(f"{file_path} - Latitude/Longitud {metadata['GPSLatitude']}, {metadata['GPSLongitude']}")

    except Exception as e:
        print(f"😱 Error al leer los metadatos del archivo {file_path}: {e}")

    return metadatos


def process_gps_metadata(metadata, archivo):
    """
    Procesa los metadatos GPS y convierte las coordenadas a formato decimal.

    Args:
        metadata (dict): El diccionario de metadatos.
        archivo (str): El nombre del archivo.

    Returns:
        tuple: Una tupla con las coordenadas en formato decimal (latitud, longitud, fecha).
    """
    try:
        #if '0A45696B-37C6-41C6-902C-A00B64A62873_1_105_c' in archivo:
        if '.jpeg' in archivo:
            gps_latitude = metadata.get('GPS GPSLatitude')
            gps_longitude = metadata.get('GPS GPSLongitude')
            gps_latitude_ref = metadata.get('GPS GPSLatitudeRef')
            gps_longitude_ref = metadata.get('GPS GPSLongitudeRef')
            exif_date_time_original = metadata.get('EXIF DateTimeOriginal')

            if gps_latitude is not None and gps_longitude is not None and gps_latitude_ref is not None and gps_longitude_ref is not None:
                latitude = convert_to_decimal(gps_latitude)
                longitude = convert_to_decimal(gps_longitude)

                if gps_latitude_ref.values == 'S':
                    latitude = -latitude
                if gps_longitude_ref.values == 'W':
                    longitude = -longitude

                return latitude, longitude, exif_date_time_original
        elif '.heic' in archivo:
            gps_latitude = metadata.get('GPSLatitude')
            gps_longitude = metadata.get('GPSLongitude')
            gps_latitude_ref = metadata.get('GPSLatitudeRef')
            gps_longitude_ref = metadata.get('GPSLongitudeRef')
            exif_date_time_original = metadata.get('FileModifyDate')

            if gps_latitude is not None and gps_longitude is not None and gps_latitude_ref is not None and gps_longitude_ref is not None:
                latitude = convert_to_decimal(gps_latitude)
                longitude = convert_to_decimal(gps_longitude)

                if gps_latitude_ref.values == 'S':
                    latitude = -latitude
                if gps_longitude_ref.values == 'W':
                    longitude = -longitude

                return latitude, longitude, exif_date_time_original


    except Exception as e:
        print(f"😱 Error al procesar los metadatos GPS para el archivo {archivo}: {e}")


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

