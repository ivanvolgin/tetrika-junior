# === Task 1 ===
test1:
	python -m unittest task1/tests.py

# === Task 2 ===
run2:
	python -m task2.solution.main

debug2:
	python -m task2.solution.main --debug

refresh2:
	python -m task2.solution.main --refresh

test2:
	python -m unittest discover -s task2/tests

# === Task 3 ===
test3:
	python -m unittest task3/tests.py

# === Общие команды ===
test: test1 test2 test3

install:
	pip install -r requirements.txt
