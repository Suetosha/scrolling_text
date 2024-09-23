import math

import cv2
from datetime import datetime

import numpy as np


def create_video(text: str):
    width, height = 100, 100
    duration = 3
    name = f'{str(datetime.now().timestamp())}.mp4'
    fps = 24
    color = (255, 255, 255)
    font = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 2
    font_thickness = 3

    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    out_video = cv2.VideoWriter(name, fourcc, fps, (width, height))

    text_size_w, text_size_h = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    px_per_frame = math.ceil(text_size_w / (fps * duration))  # Сдвиг пикселей в одном кадре
    x, y = width, (height + text_size_h) // 2  # Начальная позиция текста

    # Генерация кадров с бегущей строкой
    for _ in range(fps * duration):
        frame = np.zeros((height, width, 3), dtype=np.uint8)  # Новый кадр
        cv2.putText(frame, text, (x, y), font, font_scale, color, font_thickness, cv2.LINE_AA)  # Добавление текста
        out_video.write(frame)  # Запись кадра
        x -= px_per_frame  # Двигаем текст влево

    out_video.release()
    cv2.destroyAllWindows()


create_video(text='test')


