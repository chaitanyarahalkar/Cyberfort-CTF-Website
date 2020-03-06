![Cyberfort CTF](logo.png)


CyberFort CTF is a free online platform to test and advance skills in Penetration Testing and Cybersecurity. This repository hosts the codebase for [cyberfort.rocks](https://cyberfort.rocks). 

The project can be hosted as it is or can be extended as per requirements.


### Running the Project


#### Running Locally 
CyberFort CTF is designed using the [Django framework](https://djangoproject.com). Building the project requires PIP and Python 3. It is recommended to install all the Python dependencies in a [virtual environment](https://pypi.org/project/virtualenv/). 

To get started, create a virtual environment - 

```bash

cyberfort@rocks:$ git clone https://github.com/chaitanyarahalkar/Cyberfort-CTF-Website
cyberfort@rocks:$ cd Cyberfort-CTF-Website
cyberfort@rocks:$ virtualenv venv
cyberfort@rocks:$ source venv/bin/activate 
cyberfort@rocks:$ pip install -r requirements.txt

```

Migrate the Django SQLite database before running the server. 

```bash

cyberfort@rocks:$ python manage.py migrate 
cyberfort@rocks:$ python manage.py runserver

```

Create a super user to upload CTF challenges - 

```bash

cyberfort@rocks:$ python manage.py createsuperuser

```
The administration page is located by default at [localhost:8000/admin](http://localhost:8000/admin). New challenges can be added here. Challenge-related files will persist in the Uploads folder. Settings for the website can be configured using the ```CTFFinal/settings.py``` file.


#### Hosted Deployment 
One-click deploy on [Heroku](https://heroku.com)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Authors

 **Chaitanya Rahalkar**

* Twitter: [@chairahalkar](https://twitter.com/chairahalkar)
* Github: [@chaitanyarahalkar](https://github.com/chaitanyarahalkar)

 **Anushka Virgaonkar**

* Github: [@anushkavirgaonkar](https://github.com/anushkavirgaonkar)

 **Harsh Saglani**

* Github: [@ashawe](https://github.com/ashawe)

#### Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/chaitanyarahalkar/Cyberfort-CTF-Website/issues).

#### Show your support

Give a ⭐️ if this project helped you!

#### License

Copyright © 2019 [Chaitanya Rahalkar](https://github.com/chaitanyarahalkar).<br />
This project is [MIT](https://github.com/chaitanyarahalkar/Cyberfort-CTF-Website/blob/master/LICENSE) licensed.







