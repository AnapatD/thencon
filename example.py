# -*- coding: utf-8 -*-

from thencon import translate

entext = ("l;ylfu") #Typing Thai with English keyboard
thtext = ("็ำสสน") #Typing English with Thai keyboard

converted_th = translate(1, entext) #Convert English to thai
converted_en = translate(2, thtext) #Convert Thai to English

print("The Thai text is: " + converted_th)
print("The English text is: " + converted_en)