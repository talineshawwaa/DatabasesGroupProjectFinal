# DatabasesGroupProjectFinal -- Sneakers

## 💡 Aim of our Project SNEAKERS DATABASE
In this project, we will be creating a Django web application that interacts with both MySQL and MongoDB databases. Our project involves setting up Django models, integrating with MySQL to retrieve relational data, connecting to MongoDB for NoSQL data, and implementing a web scraping component to populate our database with external data. Our database will consist of a multitude of sneakers, of various attributes (colour, model, prices, etc...), which will then be suggested to users, based on their inputted preferences within our web app. We also had the option of creating a simple UI.

## 🎛️ Database Components:

- Model name
- Shoe size 
- Style
- Color
- Price (constant, in €)

## 🛠️ System requirements:

### Python 3.8

It is highly recommended to create a new directory environment based on Python 3.8. (Example of environment name: shoes)

### TablePlus & SQL (ALL THE different databases we have like how we created wisam, everylittle thing) 

### Python Packages to Install (on activated conda environment) -- Prior Installations (*pip3 depending on your environment)

pip install Django

pip install mySQL

pip installmySQLclient

pip install MongoDB driver for Django (djongo)

pip install djongo

pip install beautifulsoup4

pip install selenium

pip install flask

pip install flask-cors



## ⏱️ Timeline

1. Django Web Application: Where you create the project, configure the settings & create the Django models (w/foreign keys for relational data)
2. MySQL Database Integration: Where MySQL database is setup & connected with Django. Also where Django models -> MySQL tables (+ relationships)
3. MongoDB Database Integration: Where MongoDB-D (i.e. djongo) is installed & connected to MongoDB. Also where MongoDB models represent collections in DB
4. Web Scraping Component: Where you select source for data (verify if responsible choice!) & scrape accurate, needed data (+ storage)
5. Simple User Interface: Where you add Django templates to show your data
6. Documentation: Where you explain the project/requirements, & the scope of each Django model


## 🏃‍♀️ How to run the code
When running the code, make sure you have all the python packages installed and ready before running, the packages are all mentioned above in the "Python Packages to Install" section. It is also important to make sure that you are running the code on python3! Changing the file path is also cruical, to the name of the desktop you are using with your specified username and password. Once all is done, a JSON file should be correctly produced with all the sneakers. 



## 🚀 Migration & Dependencies

python manage.py migrate

## ⛓️ Web Scraping

To retrieve sufficient, relevant and updated data, we opted with the site Nike.es. It provides a variety of sneakers and complete information pertaining to each. To complete the webscraping, we used BeautifulSoup & Selenium for both dynamic and non-dynamic data.

## 📬 Acknowledgement & Sources
[Nike España](https://nike.es) provided a reliable data source for our web scraping component

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) made web scraping easier with Python, BeautifulSoup is used for non-dynamic data

[Selenium](https://selenium-python.readthedocs.io/) used for dynamic data, such as sneaker sizes

## ✅ Potential Final Result

After completing the previous steps, you are able to see your result within Compass. This is our result below!

![Image 3-12-23 at 19 30](https://github.com/talineshawwaa/DatabasesGroupProjectFinal/assets/132683425/186a4b26-e90f-44b0-b9aa-fa921436574d)

## 🔔 Potential Final Result -- UI

This is our attempt at creating the user interface, with a simple design. We created an html, css and js file which worked together to create this component.

![image](https://github.com/talineshawwaa/DatabasesGroupProjectFinal/assets/132683425/96f287bb-194f-4f1a-aa56-b1a332419c00)




