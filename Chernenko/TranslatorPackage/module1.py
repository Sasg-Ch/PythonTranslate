from googletrans import Translator

def Translate(text : str, scr : str, dest : str) -> str:
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest,src=scr)
        return translation.text
    except Exception as e:
        return "Error Translate"

def LangDetect(text : str,set : str) -> str:
    translator = Translator()
    try:
        detectlang = translator.detect(text)
        if set == "lang":
            return detectlang.lang
        elif set == "confidence":
            return detectlang.confidence
        elif set == "all" or set == "":
            return detectlang
        else:
            return "Неправильний параметр 'set'."
    except Exception as e:
        return f"Помилка при визначенні мови{str(e)}"
def CodeLang(lang : str) -> str:
    lang = lang.lower()
    langcode = {
        "english":"en",
        "ukrainian":"uk",
        "efrikaans": "af",
        "emharic": "am",
        "erabic": "ar",
        "ermenian": "hy"
        #etc
    }
    code_detect = {v:k for k,v in langcode.items()}
    if lang in langcode:
        return langcode[lang]
    elif lang in code_detect:
        return code_detect[lang]
    else:
        return None



