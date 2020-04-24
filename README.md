# Проект "Абсолютный курс" 
прогнозирование абсолютных курсов валют 

http://www.abscur.ru


## Библиотека abscur: 
импортируем: 
```
! wget -O abscur.py https://github.com/prog815/abscur_prediction/raw/master/abscur.py 
```

используем: 
```
import sys
if 'abscur' in sys.modules:
    del sys.modules['abscur']
import abscur
```

