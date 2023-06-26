# TCC - Explorando a visão computacional com análises de imagens utilizando AWS Rekognition

Este repositório contém o código-fonte e o TCC relacionado ao projeto de detecção de labels em imagens utilizando a biblioteca AWS Rekognition.

## Descrição do Projeto

O objetivo deste projeto foi explorar as capacidades da plataforma AWS e sua ferramenta AWS Rekognition para aplicar técnicas de visão computacional e inteligência artificial na análise de imagens. O estudo foi motivado pela curiosidade em compreender o funcionamento das câmeras de dispositivos móveis, especialmente devido ao aumento do uso de inteligência artificial e visão computacional nesses dispositivos nos últimos anos.

O código-fonte desenvolvido consiste em um script em Python que utiliza a biblioteca Boto3 para se conectar à API Rekognition da AWS. O script realiza as seguintes etapas:

1. Lê as credenciais de acesso à AWS a partir de um arquivo `credentials.csv`.
2. Cria o cliente de acesso à API Rekognition.
3. Carrega uma imagem a ser analisada.
4. Converte a imagem em um array de bytes.
5. Utiliza o cliente para detectar as labels presentes na imagem.
6. Verifica se há rostos na imagem.
7. Salva os resultados em uma planilha Excel (.xlsx).

## Pré-requisitos

Antes de executar o código, certifique-se de que os seguintes requisitos foram atendidos:

1. Tenha uma conta ativa na AWS com permissões para acessar a API Rekognition.
2. Tenha o Python 3.x instalado em seu ambiente.
3. Instale as bibliotecas necessárias executando o comando `pip install boto3 openpyxl`.

## Utilização

1. Clone este repositório em sua máquina local.
2. Abra o arquivo `credentials.csv` e preencha-o com suas credenciais de acesso à AWS.
3. Modifique o caminho da imagem (`photo`) no código para a imagem que deseja analisar.
4. Execute o script Python `detecao_labels.py`.
5. Verifique o arquivo `resultado.xlsx` gerado para ver os resultados da detecção de labels.


## Autores

Este projeto foi desenvolvido por Ezequiel Nascimento Campos como parte do Trabalho de Conclusão de Curso na faculdade Unicarioca.

## Agradecimentos

Agradecemos aos professores e orientadores que nos auxiliaram ao longo deste projeto.

