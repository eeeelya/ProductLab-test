# ProductLab-test
Тестовое задание для компании ProductLab.

### Установка

Установка репозитория на локальную машину:

    git clone git@github.com:eeeelya/ProductLab-test.git

### Часть 1

Решение первой части находится в каталоге *algorithm-task*. Для решения задачи
использовался алгоритм обхода графа в глубину. Для запуска алгоритма необходимо ввести
следующее:
    
    python algorithm-task/task.py

### Часть 2
    
Решение второй части находится в каталоге *wildberries_task*. Для запуска проекта необходимо
выполнить ряд команд:

    cd wildberries_task
    chmod +x entrypoint.sh
    sudo docker-compose up --build

Решение поставленных задач описано в следующих пунктах.

<details>
  <summary>Пункт 1.</summary>
Сперва необходимо было найти HTTP запрос, который в json формате возрашал бы информацию
о товаре. Данный запрос был найден в инспекции страницы, но после проверки на других страницах
стало понятно, что этот запрос отличается для каждого товара с ним могут возникнуть 
проблемы. Решением появилось после 10 минут, проведенных в google. Был найден запрос, который 
одинаков для всех страниц, за исключением артикула.
</details>

<details>
  <summary>Пункт 2.</summary>
Далее требовалось написать API. Для рещения этой задачи использовалась *APIView*
с переопределенным методом *post*, также был реализован сереализатор *InputSerializator*
 для валидорования полученных данных.
</details>


<details>
  <summary>Пункт 3.</summary>
 При помощи *aiohttp* была написана функция, которая получает необходимые данные
 из отправленного запроса. А для ее выполнения была реализована функция 
 *make_request*, которая обеспечивает выполнение асинхронного кода до конца.
</details>

<details>
    <summary>Пункт 4.</summary>
 В результате получилось готовое приложение для получекния данных по артикулам. 
 Приложение имеет обработку ошибок, что обеспечивает стабильную работу.
</details>
