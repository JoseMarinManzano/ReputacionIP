import requests
import csv
import json

api_key = "82d8ca63ed2cf3717f2288f16f774371a6d0657be94e06a25392363ca925a54d"

# Create an empty list to store the IP addresses
listado_ip = []

# Open the CSV file and read the IP addresses
with open('listado_ip.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:  # Check if the row is not empty
            listado_ip.append(row[0])  # Assuming the IP addresses are in the first column

# Define the VirusTotal API endpoint
base_url = "https://www.virustotal.com/api/v3/ip_addresses/"

# Iterate through the list of IP addresses and make API requests
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
    print(f"IP {ip}, reportes negativos {reportes}, votos negativos {votos}")

