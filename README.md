# 🧠 Tetrika Junior Test Project

📂 Репозиторий с решениями заданий от Tetrika (Junior Backend Developer). Проект выполнен с соблюдением принципов чистой архитектуры и Domain-Driven Design.

---

## 📁 Содержание

* `task1/` — @strict — проверка типов аргументов функции ([task1.md](task1/task1.md))
* `task2/` — парсинг Википедии: подсчёт животных по буквам ([task2.md](task2/task2.md))
* `task3/` — вычисление общего времени пересечения интервалов ([task3.md](task3/task3.md))

---

## ✉️ Общие требования

* Использовать Python версии 3.9 или выше
* Для задания 2 можно использовать библиотеки; задания 1 и 3 реализовать средствами стандартной библиотеки
* Решения должны находиться в `solution.py` или модуле `solution` в соответствующей папке
* К каждой задаче должны быть написаны тесты
* Ссылку на репозиторий и резюме отправлять: [https://t.me/arheugene](https://t.me/arheugene)

---

## 🛠 Makefile (универсальный для всех задач)

```makefile
# Task 1
test1:
	python -m unittest task1/tests.py

# Task 2
run2:
	python -m task2.solution.main

debug2:
	python -m task2.solution.main --debug

refresh2:
	python -m task2.solution.main --refresh

test2:
	python -m unittest discover -s task2/tests

# Task 3
test3:
	python -m unittest task3/tests.py

# Общие команды
test: test1 test2 test3
install:
	pip install -r requirements.txt
```

---

## 📌 Task 1: @strict — проверка типов аргументов

Универсальный декоратор `@strict`, который проверяет соответствие аргументов типам, указанным в аннотациях. При несоответствии вызывается `TypeError`.

```bash
make test1
```

---

## 📌 Task 2: Животные по алфавиту

Сбор животных с русской Википедии: [Категория:Животные по алфавиту](https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту)

📄 Результат сохраняется в `beasts.csv` в формате:

```
А,642
Б,412
...
```

### Запуск

```bash
make install     # установить зависимости
make run2        # обычный режим
make debug2      # с логированием
make refresh2    # пересбор ссылок
```

### Тесты

```bash
make test2
```

### 🧠 Комментарии

* Архитектура: DDD (domain, infrastructure, application)
* Кэш ссылок хранится в `task2/pages.json`
* `--debug` для включения логирования
* Сбор ссылок — синхронный, парсинг — асинхронный

---

## 📌 Task 3: Пересечение интервалов (appearance)

Функция `appearance` возвращает общее время, в течение которого ученик и преподаватель одновременно находились на уроке.

```bash
make test3
```

---

## 📦 Установка зависимостей

```bash
poetry install

pip install -r requirements.txt
```

---

## 🧾 Структура проекта

```
task1/
├── solution.py
├── tests.py

task2/
├── solution/
│   ├── main.py
│   ├── core/
│   ├── domen/
│   ├── infrastructure/
│   └── application/
├── tests/

task3/
├── solution.py
├── tests.py
```
