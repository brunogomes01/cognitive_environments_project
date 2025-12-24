import io
import re
from google.cloud import vision
from google.oauth2 import service_account
from deepface import DeepFace
import cv2

# CONFIGURAÇÕES
SERVICE_ACCOUNT_FILE = "service_account.json"
IMG_CNH = "imagens/cnh.jpg"
IMG_SELFIE = "imagens/selfie.jpg"
IMG_COMPROVANTE = "imagens/comprovante.jpg"
IMG_FACE_EXTRAIDA = "imagens/face_extraida.jpg"

# AUTENTICAÇÃO GOOGLE CLOUD
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)
client = vision.ImageAnnotatorClient(credentials=credentials)

# 1. OCR da CNH e Extração de Nome e CPF
def extrair_dados_cnh():
    with io.open(IMG_CNH, 'rb') as f:
        content = f.read()

    image = vision.Image(content=content)
    response_text = client.text_detection(image=image)
    response_face = client.face_detection(image=image)

    nome_extraido = ""
    cpf_extraido = ""

    if response_text.text_annotations:
        texto = response_text.text_annotations[0].description.upper()
        linhas = texto.split('\n')
        for linha in linhas:
            if "NOME" in linha:
                nome_extraido = linha.replace("NOME", "").strip()
            if "CPF" in linha:
                cpf_extraido = re.sub(r'\D', '', linha)

    # 1.1 Extração da face
    faces = response_face.face_annotations
    if faces:
        box = faces[0].bounding_poly.vertices
        x1, y1 = box[0].x, box[0].y
        x2, y2 = box[2].x, box[2].y
        img = cv2.imread(IMG_CNH)
        face_crop = img[y1:y2, x1:x2]
        cv2.imwrite(IMG_FACE_EXTRAIDA, face_crop)

    return nome_extraido, cpf_extraido

# 2. Comparação Facial
def comparar_faces():
    result = DeepFace.verify(IMG_FACE_EXTRAIDA, IMG_SELFIE, model_name="VGG-Face", enforce_detection=True)
    return result['verified'], result['distance']

# 3. Validação de Nome no Comprovante
def validar_nome_comprovante(nome_cnh):
    with io.open(IMG_COMPROVANTE, 'rb') as f:
        content = f.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    if not response.text_annotations:
        return False, ""

    texto = response.text_annotations[0].description.upper()
    nome_encontrado = nome_cnh in texto
    return nome_encontrado, texto

# Exeçução Integrada
def executar_validacao():
    print("Iniciando validação...\n")

    nome, cpf = extrair_dados_cnh()
    print(f"Nome extraído: {nome}")
    print(f"CPF extraído: {cpf}\n")

    match, distancia = comparar_faces()
    print(f"Match Facial: {match} (Distância: {distancia:.4f})\n")

    nome_valido, texto_comprovante = validar_nome_comprovante(nome)
    print(f"Nome no comprovante confere com CNH: {nome_valido}\n")

    # Resultado final
    if match and distancia <= 0.4 and nome_valido:
        status = "APROVADO"
    else:
        status = "REPROVADO"

    print("=== RESULTADO FINAL ===")
    print(f"Status: {status}")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Match Facial: {'Sim' if match else 'Não'}")
    print(f"Distância: {distancia:.4f}")
    print(f"Nome no Comprovante: {'Presente' if nome_valido else 'Ausente'}")

# Run
if __name__ == "__main__":
    executar_validacao()

# Certifique-se de que a imagem da CNH, Selfie e Comprovante de Endereço estejam no diretório "imagens" para execução correta.