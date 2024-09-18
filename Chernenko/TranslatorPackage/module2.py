from tabulate import tabulate
from googletrans import Translator
def LanguageList(out : str,text : str) -> str:
    translator = Translator()

    langcode = {
        "english": "en",
        "ukrainian": "uk",
        "ufrikaans": "af",
        "umharic": "am",
        "urabic": "ar",
        "armenian": "hy"
        # etc
    }

    headers = ["№", "Language", "ISO-639 code", "Text"]
    data = []
    for n, (key, value) in enumerate(langcode.items(),start = 1):
        if text == "":
            data.append([n, key, value])
        else:
            tr_text = translator.translate(text, dest=value, src='auto')
            data.append([n, key, value, tr_text.text])
    table = tabulate(data,headers, tablefmt='grid')
    try:
        if out == "file":
            with open("translation_table.txt", "w", encoding="utf-8") as file:
                file.write(table)
            return "OK"
        elif out == "screen" or out == "":
            print(table)
            return "OK"
    except Exception as e:
        return f"Error{e}"


