Forsage

Django
LiteSQL
GIT
HTML
CSS


Install Python on your device (Python 3.11.1)


To create a virtual environment, navigate to your project directory and execute: python -m venv venv

Activate your venv\Scripts\activate.bat- for Windows; source venv/bin/activate- for Linux and MacOS.

Install packages:

Go to forsage_project app: cd forsage_school

Install requirements.txt:
pip install -r requirements.txt

Create a .env file in the root directory of the project with the following content:

STRIPE_PUBLIC_KEY=your_public_key
STRIPE_SECRET_KEY=your_secret_key

success_url=your_success_url
cancel_url=your_cancel_url

SQL_ENGINE=your_db_engine
SQL_DATABASE=your_db_name
SQL_USER=your_db_user
SQL_PASSWORD=your_db_password
SQL_HOST=your_host
SQL_PORT=your_port
Make migrations python manage.py makemigrations python manage.py migrate
Run server: python manage.py runserver
