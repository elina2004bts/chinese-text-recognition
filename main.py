from paddleocr import PaddleOCR
from PIL import Image
import os

# Инициализация PaddleOCR с параметрами для китайского языка
ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # lang='ch' для китайского языка

# Укажите путь к вашему изображению
img_path = "C:\\Users\\USer\\Desktop\\китайский.webp"  # Замените на путь к вашему изображению

# Распознавание текста на изображении
result = ocr.ocr(img_path, cls=True)

# Печать результатов
for line in result[0]:
    print(line[1])
