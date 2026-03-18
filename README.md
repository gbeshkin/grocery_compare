# Grocery Basket Compare MVP

Первая версия web-сервиса для сравнения продуктовой корзины между **Rimi** и **Selver**.

Сейчас проект работает в режиме **demo catalog**: интерфейс, API и логика сравнения уже готовы, а следующим шагом можно подключить live-поиск по магазинам.

## Что уже умеет

- принимать корзину через web-форму
- сравнивать товары между Rimi и Selver
- считать итог по каждому магазину
- считать смешанную корзину
- выбирать лучший итог
- делать базовый fuzzy matching для RU / EN / ET названий

## Стек

- Python
- FastAPI
- Jinja2
- HTML / CSS / Vanilla JS

## Структура проекта

```text
app/
  main.py
  routes.py
  services/
    catalogs.py
    compare.py
    matcher.py
    stores.py
  static/
    styles.css
  templates/
    index.html
requirements.txt
.gitignore
.env.example
Makefile
README.md
```

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/<your-username>/grocery_compare_mvp.git
cd grocery_compare_mvp
```

### 2. Создать виртуальное окружение

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустить локально

```bash
uvicorn app.main:app --reload
```

Открыть в браузере:

```text
http://127.0.0.1:8000
```

## Как пользоваться

Вставь товары по одному на строку, например:

```text
молоко
яйца
хлеб
бананы
куриное филе
```

Сервис покажет:

- найденный товар в Rimi
- найденный товар в Selver
- лучший вариант по позиции
- общую сумму корзины по каждому магазину
- минимальную смешанную корзину

## Текущие ограничения

- пока нет реального API-поиска по магазинам
- не учитывается количество товара
- не учитывается точный вес / объём
- нет ссылок на карточки товаров
- нет истории корзин

## Что подключать следующим шагом

### Rimi

Нужен live-адаптер, который:

- принимает поисковый запрос
- отправляет запрос в источник Rimi
- получает список товаров
- нормализует ответ в единый формат

Пример нормализованного товара:

```python
{
    "name": "Piim 2.5% 1L",
    "price": 1.29,
    "unit": "1 l",
    "aliases": ["piim", "milk", "молоко"]
}
```

### Selver

Аналогичный live-адаптер с тем же форматом ответа.

## Roadmap

1. Подключить live-поиск для Rimi
2. Подключить live-поиск для Selver
3. Добавить количество товаров: `молоко 2`, `бананы 1 кг`
4. Добавить ссылки на найденные позиции
5. Добавить сохранение истории корзин
6. Подготовить деплой на Railway / Render

## Подготовка к GitHub

### Инициализация репозитория

```bash
git init
git add .
git commit -m "Initial commit: grocery basket compare MVP"
```

### Подключение удалённого репозитория

```bash
git remote add origin https://github.com/<your-username>/grocery_compare_mvp.git
git branch -M main
git push -u origin main
```

## Идеи для следующих веток

- `feature/rimi-live-search`
- `feature/selver-live-search`
- `feature/quantity-parser`
- `feature/history-storage`
- `feature/deploy-railway`

## Лицензия

Пока не добавлял лицензию специально. Если хочешь открытый репозиторий, следующим шагом лучше выбрать MIT.
