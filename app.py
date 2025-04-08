import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image

# Инициализация OCR
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

# Заголовок приложения
st.title('Распознавание китайского текста с PaddleOCR')

# Загрузка изображения
uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Загруженное изображение", use_column_width=True)

    # Преобразование изображения в формат, подходящий для OCR
    result = ocr.ocr(uploaded_file, cls=True)

    # Печать результатов
    st.subheader("Распознанный текст:")
    for line in result[0]:
        st.write(line[1])
