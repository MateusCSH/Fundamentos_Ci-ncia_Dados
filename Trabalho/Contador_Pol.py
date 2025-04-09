
import cv2
import mediapipe as mp
import math


video = cv2.VideoCapture("C:/Users/20231ENPRO0038/Fund_Ciencia_Dados/Polichinelo2.mp4")
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5, min_detection_confidence=0.5)
draw = mp.solutions.drawing_utils
contador = 0
check = True



while True:
    success, img = video.read()
    videoRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Pose.process(videoRBG)
    points = results.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h, w, _ = img.shape #EXTRAINDO DIMENSÃO DA IMG
    #CONVERTENDO EM PIXEL

    # Verificar se os pontos não estão vazios.
    if points:
        peDY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y*h)
        peDX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x*w)

        peEY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y*h)
        peEX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x*w)

        moDY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y*h)
        moDX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x*w)

        moEY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y*h)
        moEX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x*w)

        # DITÂNCIA ENTRE 2 PONTOS
        distMO = math.hypot(moDX - moEX, moDY - moEY)
        distPE = math.hypot(peDX - peEX, peDY-peEY)

        print(f'maos {distMO} pés {distPE}')
        
        #maos <=150 pes >= 120
        #CRIANDO CONDIÇÕES
        if check == True and distMO <= 150 and distPE > 120:
            contador +=1
            check = False #Para não contabilizar 2 vezes até que a situação inversa seja encontrada.
        
        if distMO > 150 and distPE < 120:
            check = True
        print(contador)
        texto = f'QTD {contador}'
        cv2.rectangle(img, (20,20), (270,60), (255,0,0),-1)
        cv2.putText(img, texto,(30,60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 5)

    cv2.imshow('Resultado', img)
    cv2.waitKey(40)
