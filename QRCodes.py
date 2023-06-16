#instalar qrcode e pillow pip install qrcode & pip install pillow
#Primeiramente devemos importar as bibliotecas necessárias
import csv #importar a biblioteca padrão csv
import os
from PIL import Image #para trabalhar com imagens pillow
from qrcode import QRCode, constants

#Definir o csv para gerar vários qrcodes e o caminho de saída
arquivo_csv = "C:\Users\vt418428\Códigos\QRCodes\Modelo_CSV.csv"
saida = "C:\Users\vt418428\Códigos\QRCodes\QRGerados"

