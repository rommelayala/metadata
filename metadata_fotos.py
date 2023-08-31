import csv
import os
import exifread
from util.libreria import *

nombre_carpeta = 'files'
csv_file_path = 'metadata.csv'


def get_metadata_del_map(nombre_carpeta):
    try:
        contenido = os.listdir(nombre_carpeta)
        metadata_map = {}

        '''
        Lee directorio y construye un diccionario con los metadatos de todos los archivos
        '''
        print(f"leyendo metadatos de los archivos")
        for archivo in contenido:
            image_path = os.path.join(nombre_carpeta, archivo)
            # if 'A00B64A62873' in archivo:
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

        elif extension.lower() == '.heic':
            metadata = read_metadata_exiftool(file_path)

            gps_latitude = metadata.get('GPSLatitude')
            gps_longitude = metadata.get('GPSLongitude')
            gps_latitude_ref = metadata.get('GPSLatitudeRef')
            gps_longitude_ref = metadata.get('GPSLongitudeRef')
            exif_date_time_original = metadata.get('FileModifyDate')

            if gps_latitude is not None and gps_longitude is not None and gps_latitude_ref is not None and gps_longitude_ref is not None:
                latitude = convert_to_decimal_heic(gps_latitude)
                longitude = convert_to_decimal_heic(gps_longitude)

                if gps_latitude_ref == 'S':
                    latitude = -latitude
                if gps_longitude_ref == 'W':
                    longitude = -longitude

                return latitude, longitude, exif_date_time_original

        return metadata
    except Exception as e:
        print(f"😱 Error al leer los metadatos del archivo {file_path}: {e}")


def create_csv_from_map(metadata_map, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Archivo', 'Tag', 'Latitud', 'Longitud', 'Fecha'])  # Cabecera

            print(f"Escribiendo el csv con los metadatos")
            for archivo, metadata in metadata_map.items():
                if isinstance(metadata, dict):
                    gps_latitude = "No hay parametros en el archivo para latitud"
                    gps_longitude = "No hay parametros en el archivo para longitud"
                    date = "No hay parametros en el archivo para fecha"
                else:
                    gps_latitude = metadata[0] if len(metadata) > 0 else "No hay parametros en el archivo para latitud"
                    gps_longitude = metadata[1] if len(
                        metadata) > 1 else "No hay parametros en el archivo para longitud"
                    date = metadata[2] if len(metadata) > 2 else "No hay parametros en el archivo para fecha"

                row_data = [archivo, 'GPS Coordinates', gps_latitude, gps_longitude, date]
                csv_writer.writerow(row_data)
                # print(f"{archivo} Latitud/Longitud: {gps_latitude}, {gps_longitude}, Fecha: {date}")

    except Exception as e:
        print(f"😱 Error al crear el archivo {archivo} CSV de metadatos {metadata} "
              f":ERROR {e}")


metadata_map = get_metadata_del_map(nombre_carpeta)
create_csv_from_map(metadata_map, csv_file_path)

print(f"🚀 Se han escrito los metadatos en el archivo {csv_file_path}")
