## Проект to-do-list - Веб-сервис менеджера задач

### Возможности проекта:
- CRUD операции для задач.
- Поиск задач по фильтрам
- REST API


<br>

### Технологии
![Python](https://img.shields.io/badge/Python-3.10-%23254F72?style=flat-square&logo=python&logoColor=yellow&labelColor=254f72)
![FastAPI](https://img.shields.io/badge/FastAPI-0.1.0-%23254F72?style=flat-square&logo=python&logoColor=yellow&labelColor=254f22)

### Как запустить проект:

Клонировать репозиторий

```
git clone https://github.com/G-Star29/to-do-list-fastapi.git
```

Установка зависимотсей 

```
pip install -r requirements.txt
```

Запуск сервера:

```
uvicorn app.main:app --host 0.0.0.0 --port 80
```

Запуск тестов:

```
pytest
```
