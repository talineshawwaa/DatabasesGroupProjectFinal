# DatabasesGroupProjectFinal -- Sneakers

## Aim of our Project SNEAKERS DATABASE
In this project, we will be creating a Django web application that interacts with both MySQL and MongoDB databases. Our project involves setting up Django models, integrating with MySQL to retrieve relational data, connecting to MongoDB for NoSQL data, and implementing a web scraping component to populate our database with external data. Our database will consist of a multitude of sneakers, of various attributes (colour, model, prices, etc...), which will then be suggested to users, based on their inputted preferences within our web app. We also had the option of creating a simple UI.

## Database Components:

- Brand/Model name
- Shoe size (male vs female)
- Style
- Color(s)
- Price (constant, in €)

## System requirements:

### Python 3.8

It is highly recommended to create a new directory environment based on Python 3.8. (Example of environment name: shoes)

### TablePlus & SQL (ALL THE different databases we have like how we created wisam, everylittle thing) 

### Python Packages to Install (on activated conda environment) -- Prior Installations

pip install Django

pip install mySQL

pip installmySQLclient

pip install MongoDB driver for Django (djongo)

pip install djongo

pip install beautifulsoup4

## Timeline

1. Django Web Application: Where you create the project, configure the settings & create the Django models (w/foreign keys for relational data)
2. MySQL Database Integration: Where MySQL database is setup & connected with Django. Also where Django models -> MySQL tables (+ relationships)
3. MongoDB Database Integration: Where MongoDB-D (i.e. djongo) is installed & connected to MongoDB. Also where MongoDB models represent collections in DB
4. Web Scraping Component: Where you select source for data (verify if responsible choice!) & scrape accurate, needed data (+ storage)
5. Simple User Interface: Where you add Django templates to show your data
6. Documentation: Where you explain the project/requirements, & the scope of each Django model







## How to run the code

## Migration & Dependencies

python manage.py migrate

## Web Scraping

To retrieve sufficient, relevant and updated data, we opted with the site Nike.es. It provides a variety of sneakers and complete information pertaining to each. To complete the webscraping, we used BeautifulSoup.

## Acknowledgement & Sources
[Nike España](https://nike.es) provided a reliable data source for our web scraping component
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) made web scraping easier with Python


