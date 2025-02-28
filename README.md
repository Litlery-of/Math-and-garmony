# 19.10.24 -- T == Templates
## Как поменять удалённый репозиторий, если на новом что-то есть
1. Скачать себе код (`git clone <ссылка>`);
2. Поменять удалённый репозиторий (`git remote set-url origin <ссылка>`);
3. Узнать, что там на удалённом репозитории (`git fetch`);
4. Сделать merge нашей main-ветки и удалённой main-ветки (`git merge --allow-unrelated-histories origin/main`);
5. Разрешить конфликты (поправить красный файлы);
6. Сделать commit (`git add <файлы, где были проблемы>; git commit -m "<Тут текст>"`).
## Прикольные приёмы с шаблонами
- Можно просто подставлять значения -- `{{ тут ваше значение }}`;
- Можно использовать УО:
  ```html
  {% if условие %}
    <p>Первая ветка УО</p>
  {% elif условие %}
    <p>Вторая ветка УО</p>
  {% else %}
    <p>Третья ветка УО</p>
  {% endif %}
  ```
- Можно перебирать значения:
  ```html
  <ul>
    {% for переменная in набор данных %}
      <li>Тут что-то</li>
    {% endfor %}
  </ul>
  ```
- Можно использовать функции -- `{% lorem 3 p random %}`;
- Можно наследоваться:
  > Родитель
  ```html
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{{ page_title }}</title>
    </head>
    <body>
        <header>
        {% block header %}

        {% endblock %}
        </header>
        <main>
        {% block main %}

        {% endblock %}
        </main>
        <footer>
        {% block footer %}

        {% endblock %}
        </footer>
    </body>
    </html>
  ```
  > Дочерний шаблон
  ```html
    {% extends 'base/base.html' %}

    {% block main %}

    {% endblock %}
  ```
- В шаблоны можно импортировать другие шаблоны -- `{% include "путь до шаблона" %}`;
- Функция `render` (не только в Django, вообще как явление) может возвращать не только один файл!