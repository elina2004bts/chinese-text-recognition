import streamlit as st
from paddleocr import PaddleOCR

# Инициализация PaddleOCR с параметрами для китайского языка
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

st.title("Китайский текст - Распознавание с помощью PaddleOCR")

# Указание статического пути к изображению
img_path = "C:\\Users\\USer\\Desktop\\китайский.jpg"  # Путь к изображению на вашем компьютере

# Проверка, существует ли файл по указанному пути
import os
if os.path.exists(img_path):
    st.write(f"Изображение найдено: {img_path}")
else:
    st.write(f"Изображение не найдено по пути: {img_path}")

# Распознавание текста
result = ocr.ocr(img_path, cls=True)

# Показ результатов
st.image(img_path, caption="Загруженное изображение", use_column_width=True)
st.write("Распознанный текст:")
for line in result[0]:
    st.write(line[1])
