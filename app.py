import streamlit as st
from paddleocr import PaddleOCR

# Инициализация PaddleOCR с параметрами для китайского языка
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

st.title("Распознавание китайского текста с помощью PaddleOCR")

img_file = st.file_uploader("Загрузите изображение с китайским текстом", type=["png", "jpg", "jpeg"])

if img_file is not None:
    img_path = f"./{img_file.name}"
    with open(img_path, "wb") as f:
        f.write(img_file.getbuffer())
    
    # Распознавание текста
    result = ocr.ocr(img_path, cls=True)

    st.image(img_path, caption="Загруженное изображение", use_column_width=True)
    st.write("Распознанный текст:")
    for line in result[0]:
        st.write(line[1])
