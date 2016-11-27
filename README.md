#Egrico

This application help agriculturists to find and rent equipment from other
agriculturists. To minimize the needed costs to enter the market

# Description

There are three parts of the application:
* Mobile app: in Ionic
* BackEnd Restful API: In Flask
* Image Server: in apache


## Mobile app

The mobile app is developed in Ionic you can find it here: 


## Flask Restful API

The application is developed with python 2.7 You need to install the following
packages using `pip install`

`Flask` 
`Flask-SQLAlchemy`
`Flask-api`

# Image server

the images are hosted in he `/images` folder 

# SMS Gateway

We used (Tritux)[http://tritux.com] for sending SMS for users You need to check
the doc at titrux for more information how to use the API


#TODO 

* Implements the upload image functionality in the mobile APP
* Use more sophisticated algorithms to match the user with potential renting
  offers
