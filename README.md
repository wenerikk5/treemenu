# treemenu

Меню строится на основе алгоритма, где помимо родителя у каждого элемента имеются дополнительные поля: левые и правые ключи, а также уровень вложенности. Все дополнительные поля рассчитываются автоматически, для этого необходимо после добавления или изменения элемента в админ панели MenuItems нажать на кнопку "Update keys".

## Установка

```bash
# В папке директории проекта создать виртуальное окружение:
python -m venv venv
# Активировать виртуальное окружение (linux/mac):
source venv/bin/activate
# Установить зависимости (django и django-debug-toolbar):
pip install -r requirements.txt
# Выполнить миграции:
python manage.py migrate
# Загрузить тестовое меню:
python manage.py load_preview

# Для доступа в админ-панель необходимо создать суперпользователя:
python manage.py createsuperuser
```

## Применение
Template tag вставляется на необходимую страницу командой:
```bash
{% draw_menu "menu_name" %}
```

## Превью
<img src="https://github.com/wenerikk5/treemenu/blob/eb57ce8936ed0c3b0c915398028dc899b4345a70/info/preview.png" alt="img" width="600" height='300'>
