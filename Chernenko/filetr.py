import re
import os
from TranslatorPackage import module1,module2
def read_config(name_file):
    try:
        with open(name_file,'r') as file:
            lines = file.read().splitlines()
        return {
            'namefile': lines[0],
            'lang' : lines [1],
            'out' : lines [2],
            'max_chars' : int(lines[3]),
            'max_words' : int(lines[4]),
            'max_sentences' : int(lines[5])
        }
    except FileNotFoundError:
        print("File not found")


def read_text_file(name,max_chars,max_words,max_sentences):
    with open(name,'r') as file:
        text = file.read()
        words = text.split()

        selected_words = []

        count_words = 0
        count_char = 0
        count_sentences = 0


        for word in words:
            count_char += len(word)
            count_words += 1
            if count_char >= max_chars or count_words >= max_words or count_sentences >= max_sentences:
                break
            selected_words.append(word)
            if re.search(r'[.!?]', word):
                count_sentences += 1
            if count_sentences >= max_sentences:
                break
    result = ' '.join(selected_words)
    return result,count_char,count_words,count_sentences

def exportFile(namefile,langtext, text, out):
    try:
        if out == "file":
            with open(f"{namefile}_{langtext}", "w", encoding="utf-8") as file:
                file.write(text)
            return "OK"
        elif out == "screen" or out == "":
            return text
    except Exception as e:
        print(f"Error: {e}")

config_info = read_config('configfile.txt')
text_file,count_chars,count_words,count_sentences = read_text_file(config_info['namefile'],config_info['max_chars'],config_info['max_chars'],config_info['max_sentences'])
lang_text = module1.LangDetect(text_file,'lang')
tr_text = module1.Translate(text_file,lang_text,config_info['lang'])
size_file = os.path.getsize(config_info['namefile'])
print(f"Назва файла: {config_info['namefile']}\n"
      f"Розмір файла: {size_file} байт\n"
      f"Кількість символів/слів/речень: {count_chars}/{count_words}/{count_sentences}\n"
      f"Мова тексту: {lang_text}")
print(exportFile(config_info['namefile'],lang_text,tr_text,config_info['out']))





