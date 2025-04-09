
# importa as libs: opencv-python e mediapipe.

import cv2 # [1]
import mediapipe as mp # [1]
import math # [5]

# Abre o vídeo [1]
cap = cv2.VideoCapture('polichinelos.mp4') # [1]
# Você também pode usar a webcam: cap = cv2.VideoCapture(0) # [1]

# Inicializa as soluções do MediaPipe Pose [2]
mp_pose = mp.solutions.pose # [2]
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5, # [2]
    min_tracking_confidence=0.5 # [2]
)
mp_drawing = mp.solutions.drawing_utils # [2]

# Inicializa o contador [6]
contador = 0 # [6]
cheque = True # [6]

while True: # [1]
    success, img = cap.read() # [1]
    if not success:
        break

    # Converte a imagem para RGB [2]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # [2]

    # Processa a imagem com o MediaPipe Pose [3]
    results = pose.process(imgRGB) # [3]

    # Extrai os pontos de referência (landmarks) [3]
    points = results.pose_landmarks # [3]

    h, w, _ = img.shape # [5]

    if points: # [4]
        # Desenha os pontos e as conexões na imagem [3]
        mp_drawing.draw_landmarks(img, points, mp_pose.POSE_CONNECTIONS) # [3]

        # Extrai as coordenadas dos pontos de referência [4]
        landmarks = points.landmark # [4]

        # Define os pontos de referência para mãos e pés [4]
        right_foot_index = 32 # [4]
        left_foot_index = 31 # [4]
        right_hand_index = 20 # [4]
        left_hand_index = 19 # [4]

        # Extrai as coordenadas Y e X dos pontos e converte para pixels [4, 5]
        try:
            # Pé direito [4]
            pd_y = int(landmarks[right_foot_index].y * h) # [4, 5]
            pd_x = int(landmarks[right_foot_index].x * w) # [4, 5]
            # Pé esquerdo [5]
            pe_y = int(landmarks[left_foot_index].y * h) # [5]
            pe_x = int(landmarks[left_foot_index].x * w) # [5]
            # Mão direita [5]
            md_y = int(landmarks[right_hand_index].y * h) # [5]
            md_x = int(landmarks[right_hand_index].x * w) # [5]
            # Mão esquerda [5]
            me_y = int(landmarks[left_hand_index].y * h) # [5]
            me_x = int(landmarks[left_hand_index].x * w) # [5]

            # Calcula a distância entre as mãos [5]
            dist_manos = math.hypot(md_x - me_x, md_y - me_y) # [5]
            # Calcula a distância entre os pés [5]
            dist_pies = math.hypot(pd_x - pe_x, pd_y - pe_y) # [5]

            # Define as condições para contabilizar o polichinelo [6]
            if dist_manos < 150 and dist_pies > 150 and cheque: # [6]
                contador += 1 # [6]
                cheque = False # [7]
            elif dist_manos > 150 and dist_pies < 150: # [7]
                cheque = True # [7]

            # Mostra a contagem na tela [7]
            cv2.rectangle(img, (20, 20), (280, 120), (255, 0, 0), -1) # [7]
            cv2.putText(img, f'Quantidade: {contador}', (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5) # [7]

        except:
            pass

    # Exibe o vídeo com os resultados [2]
    cv2.imshow("Resultado", img) # [2]
    cv2.waitKey(40) # [2]

# Libera a captura de vídeo e fecha as janelas [1]
cap.release() # [1]
cv2.destroyAllWindows() # [2]
