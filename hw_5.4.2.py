from googletrans import Translator

with open("text_translate.txt", "w", encoding='utf-8') as f:
    with open("text.txt", "r", encoding='utf-8') as f1:
        text = f1.read()
        f.write(Translator().translate(text, dest='ru').text)

    