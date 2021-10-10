#### Задача 0 (http://www.pythonchallenge.com/pc/def/0.html):
print(2**38)
# ------- Ответ: equality


#### Задача 1 (http://www.pythonchallenge.com/pc/def/map.html):
## Мое решение:
'''
my_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet_1 = "abcdefghijklmnopqrstuvwxyz .'()"
alphabet_2 = "cdefghijklmnopqrstuvwxyzab .'()"

new_string = ''
for i in range(len(my_string)):
    new_string += alphabet_2[(alphabet_1.index(my_string[i]))]

print(new_string)
'''

'Альтернативное решение (после того, как расшифровал текст)'
'''
intab = "abcdefghijklmnopqrstuvwxyz .'()" 
outtab = "cdefghijklmnopqrstuvwxyzab .'()" 

trantab = str.maketrans(intab, outtab) 
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print (str.translate(trantab))
'''

#### Задача 2 (http://www.pythonchallenge.com/pc/def/ocr.html):

from level2 import my_string

my_list = []
for char in my_string:
    if char not in my_list:
        my_list.append(char)
        
print(my_list)

#------- Ответ: equality


### Задача 3 (http://www.pythonchallenge.com/pc/def/equality.html):
from level3 import my_string


