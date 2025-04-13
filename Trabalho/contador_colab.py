import cv2
import mediapipe as mp
import math
import os
from google.colab import files
from IPython.display import HTML
from base64 import b64encode

# Função para exibir vídeos no Colab
def show_video(video_path):
    video_file = open(video_path, "rb").read()
    video_url = f"data:video/mp4;base64,{b64encode(video_file).decode()}"
    return HTML(f"""<video width=600 controls><source src="{video_url}"></video>""")

# Upload do vídeo
uploaded = files.upload()
video_path = list(uploaded.keys())[0]

# Verifica se o vídeo foi carregado
if not video_path:
    raise Exception("❌ Não foi possível carregar o vídeo!")

# Inicializa o vídeo
video = cv2.VideoCapture(video_path)
if not video.isOpened():
    raise Exception("❌ Não foi possível abrir o vídeo!")

# Configurações de saída
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)
output_path = "/content/output.mp4"
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Inicializa o MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils

# Variáveis para contagem
contador = 0
check = True
max_frames = 300  # Limite de frames para processamento rápido
frame_count = 0

# Processamento frame a frame
while True:
    success, img = video.read()
    if not success or frame_count >= max_frames:
        break
    
    # Processamento do pose
    videoRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(videoRGB)
    points = results.pose_landmarks
    h, w, _ = img.shape
    
    if points:
        # Desenha os landmarks
        draw.draw_landmarks(img, points, mp_pose.POSE_CONNECTIONS)
        
        # Calcula distâncias
        peDY = int(points.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y * h)
        peDX = int(points.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x * w)
        peEY = int(points.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y * h)
        peEX = int(points.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x * w)
        moDY = int(points.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y * h)
        moDX = int(points.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x * w)
        moEY = int(points.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y * h)
        moEX = int(points.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x * w)
        
        distMO = math.hypot(moDX - moEX, moDY - moEY)
        distPE = math.hypot(peDX - peEX, peDY - peEY)
        
        # Lógica de contagem
        if check and distMO <= 150 and distPE > 120:
            contador += 1
            check = False
        elif distMO > 150 and distPE < 120:
            check = True
        
        # Exibe contador
        cv2.rectangle(img, (20, 20), (270, 60), (255, 0, 0), -1)
        cv2.putText(img, f'QTD {contador}', (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
    
    # Grava o frame processado
    out.write(img)
    frame_count += 1

# Libera recursos
video.release()
out.release()
pose.close()

# Garante que o vídeo foi completamente escrito
!sync

# Verifica se o vídeo foi criado
if os.path.exists(output_path):
    print(f"✅ Vídeo processado com sucesso! Contagem final: {contador}")
    print(f"📁 Tamanho do arquivo: {os.path.getsize(output_path)/1024:.2f} KB")
    
    # Exibe o vídeo processado
    display(show_video(output_path))
    
    # Opção para download
    print("\n⬇️ Faça o download do vídeo processado:")
    files.download(output_path)
else:
    print("❌ Falha ao gerar o vídeo processado!")
