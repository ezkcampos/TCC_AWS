import csv
from urllib import response
# biblioteca que se conecta com a AWS
import boto3
import openpyxl

# Cria um cliente da AWS lendo as credenciais do arquivo credentials.csv
with open('C:/Users/ezequ/Desktop/UNICARIOCA/1TCC/AWS/credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

# Usa a foto
photo = "C:/Users/ezequ/Desktop/UNICARIOCA/1TCC/AWS/desenho_carro.jpg"

# Cria o cliente
client = boto3.client('rekognition',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name='us-east-1')

# Converte uma imagem em um array de bytes
with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

# Usa o cliente para detectar as labels (camadas, o quão longe ele pode se aprofundar no reconhecimento)
response = client.detect_labels(Image={'Bytes': source_bytes},
                                MaxLabels=2,
                                MinConfidence=95)

# Imprime o resultado
print(response)

# Cria ou abre o arquivo .xlsx para escrita
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Escreve os cabeçalhos das colunas
worksheet.cell(row=1, column=1, value="Label (Rótulo)")
worksheet.cell(row=1, column=2, value="Confidence (Confiança) em %")

# Percorre as labels detectadas e escreve os resultados na planilha
for i, label in enumerate(response["Labels"]):
    worksheet.cell(row=i+2, column=1, value=label["Name"])
    worksheet.cell(row=i+2, column=2, value=label["Confidence"])

# Salva o arquivo .xlsx
workbook.save("resultado.xlsx")



