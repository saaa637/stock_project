Material Stock Report - Django (skeleton project)
------------------------------------------------

What is included
- Django project 'stockproject'
- App 'inventory' with models: Category, Material, StockEntry
- Basic templates: dashboard, stock entry, report
- Admin registration for models

How to run (on your machine)
1. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate    (Linux/macOS) or venv\Scripts\activate (Windows)

2. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. Create superuser for admin:
   python manage.py createsuperuser

5. Run the development server:
   python manage.py runserver 0.0.0.0:8000

6. Open in browser:
   http://127.0.0.1:8000/   (dashboard)
   http://127.0.0.1:8000/admin/  (admin panel)

Notes:
- Change SECRET_KEY in stockproject/settings.py for production.
- DEBUG=True here for development only.
