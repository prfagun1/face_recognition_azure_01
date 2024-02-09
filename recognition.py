import requests
import os
import requests
import json

# Diretórios de entrada e saída
input_dir = 'input'
output_dir = 'output'

face_api_url = os.environ.get('FACE_API_URL')
subscription_key = os.environ.get('SUBSCRIPTION_KEY')

face_api_url =+ "/face/v1.0/detect"

# Caminho da imagem que você deseja analisar
image_path = 'input/foto01.png'

# Parâmetros da solicitação
params = {
    # Request parameters
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'headpose,mask,qualityforrecognition',
    'recognitionModel': 'recognition_04',
    'returnRecognitionModel': 'true',
    'detectionModel': 'detection_03',
}

for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Caminho completo da imagem de entrada
        image_path = os.path.join(input_dir, filename)

        # Ler a imagem
        image_data = open(image_path, "rb").read()

        # Enviar solicitação para o Azure
        response = requests.post(face_api_url, params=params, data=image_data, headers={'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key})

        # Obter os resultados
        faces = response.json()

        # Salvar os resultados em um arquivo JSON na pasta de saída
        output_filename = os.path.splitext(filename)[0] + '_faces.json'
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, 'w') as json_file:
            json.dump(faces, json_file)

        num_people = len(faces)
        print(f"Quantidade de pessoas encontradas: {num_people}")

        for idx, face in enumerate(faces, start=1):
            quality = face['faceAttributes']['qualityForRecognition']
            print(f"Qualidade de reconhecimento da pessoa {idx}: {quality}")


        print(f"Detecção de faces concluída para {filename}. Resultados salvos em {output_path}")
        print("----")