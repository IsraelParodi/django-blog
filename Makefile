# Variables
VENV_DIR = .venv
PYTHON = python3
PIP = $(VENV_DIR)/bin/pip
ACTIVATE = . $(VENV_DIR)/bin/activate

# Commands
create-venv:
	$(PYTHON) -m venv $(VENV_DIR)

install-deps: create-venv
	$(PIP) install -r requirements.txt

activate-venv:
	$(ACTIVATE)

create-requirements:
	echo "Django" > requirements.txt
	echo "pylint" >> requirements.txt
	echo "mypy" >> requirements.txt
	echo "black" >> requirements.txt
	echo "djlint" >> requirements.txt

create-mypy-ini:
	echo "[mypy]" > mypy.ini
	echo "python_version = 3.12" >> mypy.ini
	echo "warn_redundant_casts = True" >> mypy.ini
	echo "" >> mypy.ini
	echo "[mypy-code.test]" >> mypy.ini
	echo "warn_return_any = False" >> mypy.ini
	echo "ignore_missing_imports = True" >> mypy.ini
	echo "" >> mypy.ini
	echo "[mypy-django.*]" >> mypy.ini
	echo "ignore_missing_imports = True" >> mypy.ini

create-gitignore:
	echo ".venv" > .gitignore
	echo ".mypy_cache" >> .gitignore
	echo ".vscode" >> .gitignore
	echo "db.sqlite3" >> .gitignore
	echo "__pycache__/" >> .gitignore

setup-django-project:
	make create-venv
	make activate-venv
	make create-requirements
	make create-mypy-ini
	make create-gitignore
	make install-deps

start:
	python manage.py runserver

clean:
	rm -f mypy.ini
	rm -f requirements.txt
	rm -rf $(VENV_DIR)
	rm -rf .mypy_cache

app:
	@read -p "Enter the name of the app: " appname; \
	if python manage.py startapp "$$appname"; then \
		echo "App '$$appname' created successfully!"; \
	else \
		echo "Failed to create app '$$appname'."; \
	fi


