create-venv:
	python3 -m venv .venv

install-deps:
	.venv/bin/pip install -r requirements.txt

activate-venv:
	. .venv/bin/activate

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

setup-django-project:
	make create-venv
	make activate-venv
	make create-requirements
	make create-mypy-ini
	make install-deps

start:
	python manage.py runserver

clean:
	rm -f mypy.ini
	rm -f requirements.txt
	rm -rf .venv
	rm -rf .mypy_cache

app:
	@read -p "Enter the name of the app: " appname; \
	if python manage.py startapp "$$appname"; then \
		echo "App '$$appname' created successfully!"; \
	else \
		echo "Failed to create app '$$appname'."; \
	fi


