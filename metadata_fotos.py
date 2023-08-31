from util.libreria import *

nombre_carpeta = 'files'
csv_file_path = 'metadata.csv'


metadata_map = get_metadata_del_map(nombre_carpeta)
create_csv_from_map(metadata_map, csv_file_path)

print(f"Se han escrito los metadatos en el archivo {csv_file_path}")
