## Gallery- A Django based personal gallery , 29/11/2021.

This is a simple photo gallery web application that showcases exciting photos to users.
Here,users get to view photos updated by the site admin.
Users can see photos based on the location and time that they were posted . 
Users can also copy the link to a photo to paste . The search function will search photos based on the categorie

## By Ian Ochenge

##  Live Link
https://mypictures321.herokuapp.com/


## Specifications
* User can View different photos from the galllery
* User can Click a single image to expand it and view the details of that photo
* User can Search for images by different categories.
* User can Copy a link to the photo.
* A user can Filter photos based on the location.

## Setup and Installation 
##### Clone the repository: 
 ```bash
 https://github.com/devseme/Gallery.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd gallery pip install -r requirements.txt
```
##### Install and activate Virtual Environment 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install The Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations pics
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```
##### Running the application 
 ```bash
 python manage.py server
```
##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.
  
## Known Bugs
There are no unresolved issues in regards to this code that I know of.

## Prerequisites
To be able to run this web application, you will need to have a web browser, preferably Google Chrome.
Just click on the  deployed(https://mypictures321.herokuapp.com/) link on GitHub and run it.


## Technologies Used

- HTML 
- CSS 
- Bootstrap
- Python
- Heroku

## Contributing

Feel free to raise a issue or make a pull request to fix a bug or add a new feature.(@Devseme),semeochenge@gmail.com

## Support and contact details
If there are any issues on how the code runs, concerns, questions or ideas, kindly reach out to me on my email address; 
semeochenge@gmail.com

## Author
* *Ian Seme* -  [Ian Seme]()
## License
This project is licensed under the MIT License -
MIT License

Copyright (c) 2021 Ian Seme

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Copyright (c) 2021 *Ian Seme*
