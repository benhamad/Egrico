#Egrico

This application help agriculturists to find and rent equipment from other
agriculturists. To minimize the needed costs to enter the market

# Description

There are three parts of the application:
* Mobile app: in Ionic
* BackEnd Restful API: In Flask
* Image Server: in apache


## Mobile app

The mobile application was developed with Ionic you can clone it with: 
```
git clone https://github.com/Fzwael/TuniHack.git
```
you have to follow this command to get it to work

```
cd TuniHack
npm install 
bower install

```


## Flask Restful API

The application is developed with python 2.7 You need to install the following
packages using `pip install`

`Flask` 
`Flask-SQLAlchemy`
`Flask-api`

By default the server will be binded to `127.0.0.1:5000'
you need to remove that line and uncommnet the line above 

```
    #app.run('0.0.0.0', '80')
    app.run('127.0.0.1', '5000')
```

**Beware** you need root rights to bind the script to port `80` 

# Image server

the images are hosted in he `/images` folder 

# SMS Gateway

We used (Tritux)[http://tritux.com] for sending SMS for users You need to check
the doc at titrux for more information how to use the API


#TODO 

* Implements the upload image functionality in the mobile APP
* Use more sophisticated algorithms to match the user with potential renting
  offers
