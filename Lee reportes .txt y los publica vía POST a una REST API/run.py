#! /usr/bin/env python3
# Analiza archivos .txt de reportes en BASEPATH y envía el reporte
# por REST API y método POST a un servidor

import os 
from os import path
import requests

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
BASEPATH = '/data/feedback/'
folder = os.listdir(d+BASEPATH)
list = []

# Ciclo for que abre la ruta, lee cada archivo y agrega el contenido a list
for file in folder:
    with open((d+BASEPATH) + file, 'r') as f:
        list.append({"title":f.readline().rstrip("\n"),
            "name":f.readline().rstrip("\n"),
            "date":f.readline().rstrip("\n"),
            "feedback":f.read().rstrip("\n")})

# Ciclo for que envía los resultados de list a la REST API para ser publicados
"""for item in list:
    resp = requests.post('http://[corp-web-external-IP]/feedback/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))"""