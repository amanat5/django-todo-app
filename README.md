# Todo App

This is a simple Todo application built with Django and Tailwind CSS. It allows users to create, update, and delete tasks, as well as mark tasks as completed.

## Features
- User authentication (login/logout)
- Create, edit, and delete tasks
- Mark tasks as completed or pending
- Search tasks by title

## Technologies Used
- **Backend:** Django
- **Frontend:** HTML, CSS (Tailwind CSS)
- **Database:** SQLite (default)

## Setup Instructions

### 1. Clone the repository
Clone this repository to your local machine:

git clone https://github.com/YOUR_USERNAME/todo-app.git 

### 2.Navigate to the project directory:

cd todo-app
Create a virtual environment (optional):

python -m venv venv
Activate the virtual environment:

venv\Scripts\activate

### 3.Install the required packages:

pip install -r requirements.txt

### 4.Setting Up the Database

Run migrations to set up the database:

python manage.py migrate


### 6. Login using these details: 

username: root
password: 123

### Otherwise, Create a new superuser to login:

python manage.py createsuperuser

### 7.Follow the prompts to create a superuser account.

### 8.Running the Application

To start the development server, run:

python manage.py runserver
The app will be available at http://127.0.0.1:8000/