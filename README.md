### Итоговый проект (пример) курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy API: flask 

Данные: с kaggle - https://www.kaggle.com/benroshan/factors-affecting-campus-placement

Задача: предсказать по характеристикам студента возможность его устройства на работу. Бинарная классификация.

Используемые признаки:

  * 'ssc_p' - Secondary Education percentage- 10th Grade (float)
  
  * 'hsc_p' - Higher Secondary Education percentage- 12th Grade (float)
  
  * 'degree_p'- Degree Percentage (float)


Модель: LinearRegression

Клонируем репозиторий и создаем образ

```
$ git clone https://github.com/tabaccopie/ml_bs_course_prj.git

$ cd ml_bs_course_prj

$ docker build -t ilyak_ds_app .
```

Запускаем контейнер

```
$ docker run -d -p 8180:8180 -p 8181:8181 ilyak_ds_app
```

Переходим на http://localhost:8181

