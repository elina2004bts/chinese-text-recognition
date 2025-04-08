# Распознай китайский текст с изображения!

Web-приложение для распознавания текста на китайском языке с изображения.
Используются библиотеки:

- [Streamlit](https://streamlit.io/)
- [Transformers]( https://huggingface.co/)
- [Torchvision](https://pytorch.org/vision/stable/index.html)
- [Fugashi](https://pypi.org/project/fugashi/)

Для распознавания изображений используется нейронная сеть [Hugging Face](https://huggingface.co/PaddlePaddle/PaddleOCR). 

Подробности о модели на [GitHub](https://github.com/kha-white/manga-ocr).


## Модель  
**Название:** PaddleOCR (для китайского текста)  
**Источник:** [Hugging Face](https://huggingface.co/PaddlePaddle/PaddleOCR)  
**Характеристики:**  
- Язык: Китайский (упрощенные иероглифы).  
- Точность: ~85% на стандартных текстах.  
- Требования:  
  - Python 3.6+  
  - Библиотеки: paddleocr, opencv-python  
