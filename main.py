from PIL import Image
import numpy as np
from paddleocr import PaddleOCR

# Инициализация PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

# Загрузите изображение с помощью Pillow
img_path = "C:\\Users\\USer\\Desktop\\китайский.jpg"  # Путь к изображению
img = Image.open(img_path)

# Конвертируйте изображение в массив NumPy (для совместимости с PaddleOCR)
img_np = np.array(img)

# Распознавание текста
result = ocr.ocr(img_np, cls=True)

# Вывод результата
for line in result[0]:
    print(line[1])  # Выводим распознанный текст
