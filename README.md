# Django-Core

A complete, multi-language core project built using Django REST Framework. This modular project includes apps for e-commerce, blogging, courses, ticketing, and more, with features like JWT authentication, Celery integration, and localization.

## Features

- Modular Django apps (accounts, products, orders, blog, etc.)
- RESTful API with Django REST Framework
- JWT authentication
- Celery for background tasks
- Multi-language support (i18n)
- Admin panel for content management
- Static files and media handling

## Installation

1. **Clone the Repo**
    ```sh
    git clone https://github.com/HamidRezaSaad/Django-Core.git
    ```

2. **Install Requirements**
    ```sh
    pip install -r requirements.txt
    ```

3. **Migrate Database**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Collect Static Files**
    ```sh
    python manage.py collectstatic
    ```

5. **Start Server**
    ```sh
    python manage.py runserver
    ```

6. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Admin Panel Usage

1. **Create a Superuser**
    ```sh
    python manage.py createsuperuser
    ```

2. **Run the Server**
    ```sh
    python manage.py runserver
    ```

3. Log in at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your superuser credentials.

---

MIT License © 2023 HamidReza Sadeghzadeh