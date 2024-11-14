1. Откройте терминал и выполните команду:

git clone https://github.com/erikahutieva/OOP.git

2. Перейдите в папку проекта

cd materials_site
cd school_portal

3. Установите виртуальное окружение
Создайте виртуальное окружение, чтобы изолировать зависимости проекта, далее активируйте виртуальное окружение:

python -m venv venv
Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

4. Запустите сервер разработки

python manage.py runserver
Теперь откройте браузер и перейдите по адресу http://127.0.0.1:8000, чтобы увидеть сайт на Django.