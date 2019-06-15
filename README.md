# Photo Gallery
#### A python application based on Django framework, 2019
####  **[Ian Kurao](https://github.com/iankurao)**
## Description
This is a personal gallery application that enables me to post images for other users to see. A user can click on an image to view it's details and search in my application for images based on categories.
## Setup/Installation Requirements
* Python3.6 and above
* Postgresql for databases
* On this repository,, click on the green 'clone or download' button
* navigate to the cloned folder by `cd photo gallery`
* Create a virtual environment 
* Run `source virtual/bin/activate`
* Install Django  using `pip install django=1.11.8`
* create new file `requirements.txt` and run `pip freeze > requirements.txt`
* run `python3.6 manage.py runserver `
* for quick debugging run `python manage.py check` 
## Known Bugs
NO known Bugs.
## Behavior Driven Development

| Behaviour| Input | Output |
| ------------- | ----------------- | ------------------ |
| Display all photos on database  | "https://app-name@heroku.com"   | Loads all photos  |
| Copy shortcut for images | click copy button | Saves link to clipboard |
| Save uploaded images | Upload image | Saves image |
| Update images as admin | update image at localhost/admin | Updates |
| Show image details on modal | Click image | Zooms with deets |
| Search by category| search category 'food'| returns images tagged 'culture' |



## Technologies Used
## main languages used are
* Python
* Bootstrap
* WhiteNoise
* Django
* PostgreSQL Database
* CSS


## Support and contact details
Email:kuraoian@gmail.com


### License
MIT LICENSE [Ian Kurao][2019]
