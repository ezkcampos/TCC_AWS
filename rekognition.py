import csv
from urllib import response
import boto3

# cria um cliente da aws lendo as credenciais do arquivo credentials.csv
with open('C:/Users/ezequ/Desktop/UNICARIOCA/1TCC/AWS/credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

#usa a foto
photo = "C:/Users/ezequ/Desktop/UNICARIOCA/1TCC/AWS/desenho_carro.jpg"

#cria o cliente
client=boto3.client('rekognition',
                    aws_access_key_id=access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name='us-east-1')

#converte uma imagem em um array de bytes
with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()

#usa o cliente para detectar as labels(camadas, o quão longe ele pode se aprofundar no reconhecimento)
response = client.detect_labels(Image={'Bytes': source_bytes},
                                MaxLabels=2,
                                MinConfidence=95)

print(response)