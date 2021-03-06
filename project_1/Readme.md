# Проект 1. Анализ вакансий на hh.ru

***Содержание***
- [Введение](#Intro)
- [Анализ и обработка данных](#Analysis)
    - [Базовый анализ структуры данных](#BaseAnalysis)
    - [Преобразование данных](#Processing)
    - [Разведывательный анализ (EDA)](#EDA)
    - [Очистка данных](#Cleaning)
- [Критерии оценивания](#Criteria)
- [Результат и выводы](#Results)



# Введение <a name="Intro"></a>
Используя методы обработки и анализа данных средствами *python* и библиотек *numpy*, *pandas*, *matplotlib*, *seaborn* и *plotly*, решить часть бизнес-задачи по прогнозированию ЗП соискателей на сайте hh.ru, так как часть соискателей не указывают желаемую заработную плату, когда составляют свое резюме.

Настоящий проект является подготовкой данных к прогнозированию.


# Анализ и обработка данных <a name="Analysis"></a>
В подготовленном [датасете](https://drive.google.com/file/d/1Kb78mAWYKcYlellTGhIjPI-bCcKbGuTn/view?usp=sharing) данные представлены в сыром виде, информация в столбцах ненормализована и непригодна для анализа и тем более для построения каких-то предсказательных моделей. Прежде чем приступать к цели самой задачи, данные необходимо базово проанализировать и обработать.


## Базовый анализ структуры данных <a name="BaseAnalysis"></a>
В изначальном виде данные имеют такие признаки:
- **Пол, возраст**
    - Пример данных: "Мужчина , 39 лет , родился 27 ноября 1979"
    - Заметим, что в одном поле содержится пол, возраст и дата рождения соискателя. Очевидно, что эти данные нужно нормализовать 
- **ЗП**
    - Пример данных: "29000 руб."
    - Помимо интересующего нас числа, в этом поле содержится указание валюты, которая не обязательно является рублем. При обработке данных это нужно будет учесть
- **Город, переезд, командировки**
    - Пример данных: "Москва , готов к переезду , готов к командировкам"
    - В данном поле содержится город, готовность соискателя к переезду и командировкам. Эти данные так же нужно будет нормализовать
- **Занятость**
    - Пример данных: "частичная занятость, проектная работа, волонтёрство"
    - В этом поле содержатся категории занятости, в которых заинтересован соискатель. Здесь может быть указано несколько признаков, поэтому все их нужно будет разнести в разные поля
- **График**
    - Пример данных: "сменный график, гибкий график"
    - В этом поле так же содержатся несколько разных признаков, показывающие интересующие соискателя варианты графиков работы. Данный признак мы так же нормализуем по разным полям
- **Опыт работы**
    - Данные в этом поле имеют структуру "Опыт работы: **N** лет **M** месяцев, периоды работы в различных компаниях…"
    - Из этого поля важно извлечь опыт работы соискателя, который представлен в виде "годы" + "месяцы", с необязательным наличием каждой составляющей. Эту информацию нужно будет привести к одному виду
- **Образование и ВУЗ**
    - Пример данных: "Высшее образование 2016 Московский авиационный институт (Национальный исследовательский университет)"
    - Из этого признака необходимо извлечь уровень образования соискателя. Другую информацию учитывать не будем
- **Обновление резюме**. Здесь содержатся данные формата "дата+время" и это поле мы будем использовать в дальнейшем
- Поля **Ищет работу на должность:**, **Последнее/нынешнее место работы**, **Последняя/нынешняя должность**, **Авто** в данном проекте рассматривать не будем


## Преобразование данных <a name="Processing"></a>
Из предыдущего раздела видно, что данные очень сырые: признаки представлены в неудобном для анализа и очистки формате.

Например, столбец «Пол/возраст» содержит информацию и о поле, и о возрасте, и о дате рождения. Желаемая заработная плата представлена в виде текста с указанием валюты, в которой она исчисляется, и так дале

Все это не позволяет визуально оценить зависимости в данных: построить графики распределения и зависимостей, нельзя нормально заполнить пропуски или найти аномалии в данных.

В проекте обработаны следующие поля:
- **"Образование и ВУЗ"**. Из этого признака выделен уровень образования (высшее, неоконченное высшее, среднее специальное и среднее) в новое поле *"Образование"*
- **"Пол и возраст"**. Из этого признака выделен пол соискателя и возраст. Соответствующие данные вынесены в новые поля *"Пол"* и *"Возраст"*
- **"Опыт работы"**. Из этого признака выделен опыт работы соискателя и приведен к числу месяцев (новое поле *"Опыт работы (месяц)*)
- **"Город, переезд, командировки"**. Из этого признака выделен город соискателя, и его готовность к переезду и командировкам. Соответствующие данные вынесены в новые поля *"Город"*, *"Готовность к переезду"* и *"Готовность к командировкам"*, при этом:
    - В поле **Город** выделили только города Москва, Санкт-Петербург, и ввели категории "город-миллионник" и "другие"
    - В полях **Готовность к командировкам** и **Готовность к переездам** стоят значения *True* и *False*
- **Занятость** разбили на поля *"Полная занятость"*, *"Частичная занятость"*, *"Проектная работа"*, *"Стажировка"* и *"Волонтерство"* с проставленными в соответствии с предпочтениями соискателей *True* и *False*
- **График** разбили на поля *"Полный день"*, *"Сменный график"*, *"Гибкий график"*, *"Удаленная работа"* и *"Вахтовый метод"* с проставленными в соответствии с предпочтениями соискателей *True* и *False*
- **ЗП**. Из этого признака была извлечена интересующая соискателя зарплата и, в соответствии с [таблицей курсов валют](https://lms.skillfactory.ru/assets/courseware/v1/15abf80f45a2f3e93c3274101b451c67/asset-v1:SkillFactory+DSPR-2.0+14JULY2021+type@asset+block/ExchangeRates.zip), эти зарплаты приведены к рублю


## Разведывательный анализ (EDA) <a name="EDA"></a>
Теперь данные готовы к первичному анализу зависимостей (*EDA - exploratory data analysis*). Он предназначен для выявления связей между признаками, выявления закономерностей, определения распределений признаков, поиска аномалий и других дефектов данных.

В проекте построено много графиков, таких, как:
- Гистограмма и коробчатая диаграмма распределения возрастов соискателей
- Графики зависимостей медианной ожидаемой ЗП соискателей в зависимости от разных признаков
- Тепловая карта зависимости медианной ожидаемой ЗП соискателей от возраста и образования, и т.д.

К каждому графику приведены описание и выводы.


## Очистка данных <a name="Cleaning"></a>
Проведя разведывательный анализ данных, выявились несостыковки и аномалии:
- Пропуски в данных
- Гигантские размеры ожидаемых заработных плат
- Наличие людей "преклонного возраста"
- Опыт работы, превышающий возраст

Все это говорит о том, что данные подлежат очистке. В проекте данные очищены от аномалий, указанных выше.


## Критерии оценивания <a name="Criteria"></a>
Данный обучающий проект оценивается по следующим критериям:
- Код решения загружен на Github и оформлен файл Readme.md
- Решение оформляется только в *Jupyter Notebook*
- Решение оформляется в соответствии с ноутбуков-шаблоном
- Каждое задание выполняется в отдельной ячейке, выделенной под задание
- Код для каждого задания оформляется в одной-двух *Jupyter*-ячейках
- Решение должно использовать только пройденный материал: переменные, основные структуры данных (списки, словари, множества), циклы, функции, библиотеки numpy, pandas, matplotlib, seaborn, plotly
- Код должен быть читаемым и понятным: имена переменных и функций отражают их сущность, важно избегать многострочных конструкций и условий
- Код должен быть написан в соответствии с [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Графики оформляются в соответствии с теми правилами, которые были приведены в [модуле по визуализации данных](https://lms.skillfactory.ru/courses/course-v1:SkillFactory+DSPR-2.0+14JULY2021/jump_to_id/1fa00a018157484a9bae5d4557ef3e7c)
- Графики должны содержать название, отражающее их суть, и подписи осей
- Выводы к графикам оформляются в формате *Markdown* под самим графиком в отдельной ячейке. Выводы должны быть представлены в виде небольших связанных предложений на русском языке.


## Результаты и выводы <a name="Results"></a>
В настоящем проекте был обработан, проанализирован и очищен датасет с резюме соискателей с сайта hh.ru:
- Выполнен первичный анализ данных
- Выполнена обработка, преобразование и нормализация данных
- Выполнен разведывательный анализ данных (в том числе построены различные графики с выводами)
- Выполнена очистка данных от пропусков и аномалий