# Django Recipes App

This is a simple web application built with Django that allows users to create and share recipes. 
Make sure you have Docker and Docker Compose installed on your system before running the application.

###### Installation

1. Clone the repository:

git clone https://github.com/VensMantas/DjangoRecipes.git
cd django-recipes-app

2. Build the Docker image:

docker-compose build

3. Run the Docker containers:

docker-compose up

4. The application should be accessible at http://localhost:8000/.

###### Testing

1. To run the tests, use the following command:

docker-compose run web python manage.py test

###### Database

The application uses MySQL as the database. Configuration accessible via 'docker-compose.yml'.
# Default:
1. name: 'recipes',
2. user: 'root',
3. password: '';
