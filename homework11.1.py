
# Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
# После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и
# функциями. К каждой библиотеке дана ссылка на документацию ниже.

# requests - запросить данные с сайта и вывести их в консоль.
# pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
# matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
# В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная
# библиотека и как вы расширили возможности Python с её помощью.

import requests  # 'Можно сделать запрос с сайта'

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'

res = []

for i in range(10):
    response = requests.get(THE_URL)   # 'Запрос по URL'
    page_response = response.json()   # 'Перевод в формат Piton'
    res.append(page_response)   # 'Добовляем результат в список res'

print(res)



import matplotlib.pyplot as plt   # 'Для построения графиков'

plt.plot([1, 2, -6, 0, 4])
plt.show()


import PIL
from PIL import Image

SOURCE_DIR = f'./images/'
p1 = Image.open(SOURCE_DIR + 'item-portrait-groot.jpg')
awa = p1.crop((0,0,p1.width,p1.width)).resize((300, 300)).transpose(Image.FLIP_LEFT_RIGHT) # 'Можно обрезать изображение'
awa.save(SOURCE_DIR + 'awa.jpeg')

# print(p1.size)
# print(p1.mode)
# print(p1.format)
# print(p1.info)
p1.show()







