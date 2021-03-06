# MovieBluff-Restful
Implementation of [MovieBluff](https://github.com/AnishReddyRavula/MovieBluff) to Restful API

## This Restful API is an endpoint server

This server takes a request in JSON format with movie name, movie rating, watched status and watched date as attributes and saves it in database.

### CRUD operations

Create, Read, Update, Delete operations can be performed by sending GET, POST, PUT and Delete requests\n
Or by starting the server opening the link in browser we can handle all the operations( djangorestframework will handle rendering )

* movie name (max 256 charachters)
* movie rating (WORSE = 1, BAD = 2, AVERAGE = 3, GOOD = 4, EXCELLENT = 5)
* movie watched status (True or False)
* movie watched date (if included then included date else current date)

## Requirements

Install python 3.5 and then install packages with commans ```pip install -r requirements.txt```

* Python=3.5 or above
* certifi==2016.2.28
* Django==2.0.2
* djangorestframework==3.7.7
* pytz==2018.3
* wincertstore==0.2

## Starting the server

*  Clone the repository
*  Install python and other requirements
*  run ```python manage.py makemigrations``` and ```python manage.py migrate``` in project directory to start the database with the model configuration
*  start the server with ```python manage.py runserver``` command to start the server
*  open the link address in browser to start using the API

## Authors

* **Anish Reddy Ravula** - *Initial work* - [AnishReddyRavula](https://github.com/AnishReddyRavula)

## Acknowledgments

* [Django documentation](https://docs.djangoproject.com/en/2.0/)
* [Django Rest Framework](http://www.django-rest-framework.org/)