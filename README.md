# **E-commerce web application using Django:**
Ecommerce project made with Django and basic HTML & CSS. I have used both class-based and functional views throughout the project, PostgreSQL for database, Celery for handling emails and Django-Filter for category filtering. API's for admin side are included in the app named api. For payment integration, I have used Paypal's API.

![](snapshots/user_interface/store_.png)

# Features:

### Admin side:

* Add new products.
* Edit details of the existing products.
* Delete existing products.
* View all orders.
* Change order status.
* Filter orders based on their status.
* View the order details.

### User side:

* Registration and authentication.
* Add and remove products to cart.
* Update the quantity of cart.
* Payment can be done with paypal.
* Products can be filtered by category.
* Search filter.
* Confirmation email after order successfully placed.
* View complete order history.
* View order details.
* Update profile details.

# Technology stack:
1. Python 3.6.5
2. Django REST Framework 2.1
3. PostgreSQL 13.1 Database
4. Google Chrome

# Project Structure:
```
.
├── api: API's for the ecommerce project
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py: serializers for the models
│   ├── tests.py
│   ├── urls.py: urls for api app
│   └── views.py: These views are called by API endpoints
├── API.md: API documentation file
├── ecom Ecommerce project base folder
│   ├── celery.py: contains the default code needed for celery
│   ├── __init__.py
│   ├── settings.py: settings file for the project
│   ├── urls.py: base urls for apps of the project
│   └── wsgi.py
├── manage.py
├── README.md: documentation file
├── requirements.txt: requirements needs to be install
├── snapshots: contains the screenshots of project
├── static
│   ├── css
│   │   └── main.css: CSS file for the Ecommerce project
│   ├── images
│   └── js
│       └── cart.js: JS file for updating cart items
└── store
    ├── admin.py
    ├── apps.py
    ├── filters.py: contains the Django filters
    ├── forms.py: contains the Django forms rendered by views
    ├── __init__.py
    ├── models.py: database models for store app
    ├── tasks.py: contain tasks for celery
    ├── templates: HTML templates for Ecommerce website project
    │   └── store
    │       ├── adminpages: HTML pages for admin interface
    │       │   ├── adminaddproduct.html
    │       │   ├── adminallproduct.html
    │       │   ├── adminbase.html
    │       │   ├── admincategory.html
    │       │   ├── adminhome.html
    │       │   ├── adminlogin.html
    │       │   ├── adminmain.html
    │       │   ├── adminorderdetail.html
    │       │   ├── adminorderlist.html
    │       │   ├── adminprofile.html
    │       │   ├── adminstore.html
    │       │   ├── adminwrongpassword.html
    │       │   ├── deleteproduct.html
    │       │   └── editproduct.html
    │       ├── base.html
    │       ├── cart.html
    │       ├── category.html
    │       ├── change_password.html
    │       ├── checkout.html
    │       ├── email_template.html
    │       ├── home.html
    │       ├── login.html
    │       ├── main.html
    │       ├── order_detail.html
    │       ├── order_history.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── password_reset_form.html
    │       ├── profile.html
    │       ├── search.html
    │       ├── signup.html
    │       ├── store.html
    │       ├── success.html
    │       ├── update_user.html
    │       └── wrongpassword.html
    ├── tests.py
    ├── urls.py: url endpoints of store app
    └── views.py: These views are called by store app endpoints
```

# Steps to run the project:
1. First, clone the repository to your local machine:
    ```bash
   git clone https://github.com/saiyadfaizan/ecomm.git
   ```
2. Create super user:
    ```bash
    python manage.py createsuperuser
    ```
    _Note: It will prompt to enter username, email and password one by one. Please remember the username and password, it will be used to login admin area._

3. Install the requirements: 
    ```bash 
    pip install -r requirements/dev.txt
    ```

4. Create the .env file to the root directory of the project. 
    >You can refer this example file:  .env.example

5. Check for the database migrations: 
    ```bash 
    python manage.py makemigrations
    ```
6. Apply the database migrations:
    ```bash 
    python manage.py migrate
    ```
7. Run the developement server: 
    ```bash 
    python manage.py runserver
    ```
8. Open chrome and the site will be available [here](127.0.0.1:8000/)

# Future scope of the project:
1. Integrating new payment gateways.
2. Adding new search and category filters.
3. Implementing and using sessions.
4. Adding suggestions wrt previous purchases.
