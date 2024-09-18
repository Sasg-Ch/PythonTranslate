from TranslatorPackage import module1
text = "Добрий день!"
print(module1.TransLate(text,"auto","en"))

print(module1.LangDetect(text,"lang"))
print(module1.LangDetect(text,"confidence"))
print(module1.LangDetect(text,"all"))
print(module1.LangDetect(text,""))

print(module1.CodeLang("en"))
print(module1.CodeLang("english"))
print(module1.CodeLang("aF"))
print(module1.CodeLang("UKrAinIaN"))