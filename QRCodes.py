#instalar qrcode e pillow pip install qrcode & pip install pillow
#Primeiramente devemos importar as bibliotecas necessárias
import csv
from PIL import Image, ImageDraw, ImageFont
import qrcode

def gerar_qrcode(arquivo_csv, pasta_saida, fonte_path):
    #Abrir o arquivo CSV
    with open(arquivo_csv, newline='') as file:
        #Para resolver o problema do excel usando ; no csv
        reader = csv.DictReader(file, delimiter=';')
        #Iterando por todas as linhas do csv
        for row in reader:
            #legenda e conteúdo do qrcode
            legenda = row['Legenda']
            conteudo_qr = row['URL']
            
            #Criando o objeto do qrcode
            qr = qrcode.QRCode(
                version=1, 
                error_correction=qrcode.constants.ERROR_CORRECT_L, 
                box_size=800, 
                border=8
                )
            qr.add_data(conteudo_qr)
            qr.make(fit=True)
            
            #Imagem do qrcode
            qr_img = qr.make_image(fill_color="black", back_color="#DCDCDC")
            qr_img = qr_img.convert("RGBA")
            qr_img = qr_img.resize((500, 500), Image.LANCZOS)

            #Carregar o logotipo
            logotipo = Image.open("C:\\Users\\vt418428\\Códigos\\QRCodes\\vtal_white.png").convert("RGBA")
            logotipo_width, logotipo_height = logotipo.size
            logotipo_max_size = min(qr_img.size) // 4
            logotipo_resized = logotipo.resize((5, 5), Image.LANCZOS)
            #Redimensionamento do logotipo
            if logotipo_width > logotipo_max_size or logotipo_height > logotipo_max_size:
                logotipo.thumbnail((logotipo_max_size, logotipo_max_size), Image.LANCZOS)
                logotipo_width, logotipo_height = logotipo.size
            #posicionamento do logotipo
            logotipo_pos_x = (qr_img.size[0] - logotipo_width) // 2
            logotipo_pos_y = (qr_img.size[1] - logotipo_height) // 2
            #Colar o logotipo no qrcode
            qr_img.paste(logotipo, (logotipo_pos_x, logotipo_pos_y), logotipo)
            #Fonte da legenda
            draw = ImageDraw.Draw(qr_img)
            fonte = ImageFont.truetype(fonte_path, 20)
            #Tamanho e posicionamento da legenda
            legenda_width, legenda_height = fonte.getsize(legenda)
            legenda_pos_x = (qr_img.size[0] - legenda_width) // 2
            legenda_pos_y = qr_img.size[1] + 20
            legenda_box = (legenda_pos_x, legenda_pos_y, legenda_pos_x + legenda_width, legenda_pos_y + legenda_height)
            draw.text((legenda_pos_x, legenda_pos_y), legenda, font=fonte, fill="black")

            
            #Para salvar o arquivo com o nome da legenda
            nome_arquivo = f"{legenda}.png"
            caminho_arquivo = f"{pasta_saida}/{nome_arquivo}"
            qr_img.save(caminho_arquivo)

            print(f"QR code gerado: {caminho_arquivo}")
#os caminhos dos arquivos, saída e fonte para a legenda
arquivo_csv = "C:\\Users\\vt418428\\Códigos\\QRCodes\\Modelo_CSV.csv"  # Insira o caminho correto do arquivo CSV
pasta_saida = "C:\\Users\\vt418428\\Códigos\\QRCodes\\QRGerados"  # Insira o caminho correto da pasta de saída
fonte_path = "C:\\Windows\\Fonts\\arial.ttf"  # Insira o caminho correto do arquivo de fonte TrueType

gerar_qrcode(arquivo_csv, pasta_saida, fonte_path)
