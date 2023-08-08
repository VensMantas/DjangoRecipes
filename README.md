# Django Recipes App

This is a simple web application built with Django that allows users to create and share recipes. 
Make sure you have Docker and Docker Compose installed on your system before running the application.

# Installation

1. Clone the repository:

git clone https://github.com/VensMantas/DjangoRecipes.git
cd DjangoRecipes

2. Build the Docker image:

docker-compose build

3. Run the Docker containers:

3.1. Firstly, run: <br>
docker-compose up db

Once it's created <br>
(last message "django_mysql  | 2023-08-08T01:03:32.522674Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.1.0'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL."), <br>
<br>
Press Ctrl+C to stop the container.<br>

3.2. Then, run these commands one by one:
docker-compose up db -d<br>
docker-compose up web -d<br>

3.3. Once both processes are running, migrate the database:<br>
docker-compose exec web python manage.py migrate

4. The application should be accessible at http://localhost:8000/ (same as http://127.0.0.1:8000/)

# Testing

1. To run the tests, use the following command:

docker-compose run web python manage.py test

# Database

The application uses MySQL as the database. Configuration accessible via 'docker-compose.yml'.
###### Default:
1. name: 'recipes',
2. user: 'root',
3. password: '';
