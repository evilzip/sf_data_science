# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#Результат)  
[6. Выводы](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#Выводы)  

### Описание проекта
Угадать загаданное число за минимальное число попыток. 

&uarr;[ К оглавлению](https://github.com/evilzip/sf_data_science/blob/main/project_0/README.md#ВыводыОглавление)

### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**
- Компьтер загадывает целое число от 0 до 100, и нам нужно его угадать. Под "угадать" подразумевается "написать программу, которая угадывает число"

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем** Учимся писать хороший код на python

### Краткая информация о данных
...
### Этапы работы над проектом
* создана функция которая угадывает загаданное число методом перебора случайных чисел
* создана функция, которая угадывает загаданное число методом "деления пополам" диапазона поиска, тем самы на каждой итерции диапазон поиска сокращается в два раза
* создана функция оценки эффективности алгоритмов угадывания по среднему количетсву попыток на 1000 задач поиска
* создан и оформлен README файл для проекта и для репозитория

### Результат
Метогд smart_predict основанный на "методе деления пополам" показал лучший результат: в среднем 6 попыток на 1000 задач поиска

### Выводы
Метод перебора случайных чисел показал самую низкую эффективность. Удалось найти и реализовать более эффективный алгоритм. 

