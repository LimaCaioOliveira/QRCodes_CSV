#instalar qrcode e pillow pip install qrcode & pip install pillow
#Primeiramente devemos importar as bibliotecas necessárias
import csv #importar a biblioteca padrão csv
import os
from PIL import Image #para trabalhar com imagens pillow
from qrcode import QRCode, constants

#Definir o csv para gerar vários qrcodes e o caminho de saída
arquivo_csv = "C:\Users\vt418428\Códigos\QRCodes\Modelo_CSV.csv" #esse é a planilha que usaremos
saida = "C:\Users\vt418428\Códigos\QRCodes\QRGerados" #caminho de sáida para salvar os qrcodes
logo = "C:\Users\vt418428\Códigos\QRCodes\vtal logo.png" #logo que usaremos


#Função para gerar os qrcodes
def gerar_qrcode(arquivo_csv, saida):
    #Segurança para funcionalidade do código: verificar se há a pasta de saída
    if not os.path.exists(saida):
        os.makedirs(saida)
        
    #Ler o CSV
    with open(arquivo_csv, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            url = row["URL"]
            legenda = row["Legenda"]
            
            #criar o qrcode
            qr=QRCode(
                version=1,
                error_correction=constants.ERROR_CORRECT_L,
                box_size=20,
                border=4,
            )
            
            qr.add_data(url)
            qr.make(fit=True)
            
            #Imagem do qr
            qr_img = qr.make_image(fill_color="black", back_color="white")
            
            #Para diferenciar os qrcodes, gerar uma legenda padrão abaixo deles lida no csv
            qr_img_width, qr_img_height = qr_img.size
            legenda_img = Image.new("RGB", (qr_img_width, 30), color=(255, 255, 255))
            legenda_text = Image.new("RGB", (qr_img_width, qr_img_height + 30))
            legenda_text.paste(qr_img, (10, 5))
            qr_with_legenda = Image.new("RGB", (qr_img_width, qr_img_height + 30))
            qr_with_legenda.paste(qr_img, (0,0))
            qr_with_legenda.paste(legenda_img, (0, qr_img_height))
            qr_with_legenda.paste(legenda_text, (0, qr_img_height))
            
            #Colocar o logo
            logotipo_path = "C:\Users\vt418428\Códigos\QRCodes\vtal logo.png"
            logotipo = Image.open(logotipo_path)
            logotipo_width, logotipo_height = logotipo.size
            
            #Achar a posição central
            pos_x = int((qr_img_width - logotipo_width)/2)
            pos_y = int((qr_img_height - logotipo_height)/2)
            
            #Adicionando o logo no qr
            qr_with_logotipo = qr_with_legenda.copy()
            qr_with_logotipo.paste(logotipo, (pos_x, pos_y), logotipo)
            
            #Nome do qr
            nome_arquivo = f"{legenda}.png"
            caminho_saida = os.path.join(saida, nome_arquivo)
            
            #Salvando
            qr_with_logotipo.save(saida)
            

#Bora chamar a função!
gerar_qrcode(arquivo_csv, saida)