Итоговый проект (пример) курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy API: flask 
Данные: с kaggle - https://www.kaggle.com/benroshan/factors-affecting-campus-placement

Задача: предсказать по характеристикам студента возможность его устройства на работу. Бинарная классификация.

Используемые признаки:

'ssc_p' - Secondary Education percentage- 10th Grade (float)
'hsc_p' - Higher Secondary Education percentage- 12th Grade (float)
'degree_p'- Degree Percentage (float)



Модель: LinearRegression
Клонируем репозиторий и создаем образ

$ git clone https://github.com/tabaccopie/ml_bs_course_prj.git
$ cd ml_bs_course_prj.git
$ docker build -t <user>/gb_ilyak_ml_prj .

Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)

$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/models 
<user>/gb_ilyak_ml_prj

Переходим на localhost:8181
