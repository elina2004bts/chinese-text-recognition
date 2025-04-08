import streamlit as st
from paddleocr import PaddleOCR
import os

# Инициализация PaddleOCR с параметрами для китайского языка
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

st.title("Китайский текст - Распознавание с помощью PaddleOCR")

# Загрузка изображения через интерфейс Streamlit
img_file = st.file_uploader("Загрузите изображение с китайским текстом", type=["png", "jpg", "jpeg", "webp"])

if img_file is not None:
    # Считывание изображения
    img_path = f"./{img_file.name}"
    with open(img_path, "wb") as f:
        f.write(img_file.getbuffer())

    # Проверка, существует ли файл по указанному пути
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

