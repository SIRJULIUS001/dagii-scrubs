# ClothSite

A simple Django-based clothing website with Home, About, Gallery, and Contact pages.

## Features
- Responsive layout with plain CSS
- Gallery powered by `GalleryImage` model
- Contact form saving to `ContactMessage` model
- Admin management for gallery and contact messages

## Setup
1. Clone repository
2. Install requirements:
   ```bash
   pip install django

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
