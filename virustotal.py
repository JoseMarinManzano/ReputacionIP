import requests
import csv
import json
from tabulate import tabulate

api_key = "pon_aqui_tu_api_key"

# Creamos la lista para almacenar las direcciones IP
listado_ip = []

# Abrimos el fichero CSV donde le pasamos el listado de IPs
with open('listado_ip.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:  
            listado_ip.append(row[0])  

# URL de la API de virustotal
base_url = "https://www.virustotal.com/api/v3/ip_addresses/"

# Creamos la tabla para almacenar la info
table_data = []

# Iteracion de la API y solicitudes
for cada_ip in listado_ip:
    url = f"{base_url}{cada_ip}"

    api_headers = {
        "x-apikey": api_key,
        "accept": "application/json",
    }

    response = requests.get(url, headers=api_headers)
    respuesta = response.json()
    ip = respuesta['data']['id']
    reportes = respuesta['data']['attributes']['last_analysis_stats']['malicious']
    votos = respuesta['data']['attributes']['total_votes']['malicious']
    
    # Solo almacenamos las IPs que no sean igual a 0
    if reportes != 0:
        table_data.append([ip, reportes, votos])

# Definimos los encabezados
headers = ["IP Address", "Malicious Reports", "Malicious Votes"]


table_data = sorted(table_data, key=lambda x: x[1], reverse=True)

# Comprobamos si la tabla esta vacia
if not table_data:
    print("No hay ninguna IP con reputación.")
else:
    # Generamos la tabla
    table = tabulate(table_data, headers, tablefmt="grid", colalign=("left", "right", "right"))

    
    print(table)

    # Guardamos la salida del output en el fichero output.csv
    with open("output.csv", "w", newline="") as csv_output_file:
        csv_writer = csv.writer(csv_output_file)
        
        
        csv_writer.writerow(headers)
        
        
        csv_writer.writerows(table_data)
