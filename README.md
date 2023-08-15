#Flask CRUD
BY Abhay Pratap

This is a python based application on flask along with the mongoDB as the database, this application contains a dockerfile for the ease of deployment and testing, you can directly you this application via docker image(Steps provided below)

##To setup:

###Using the git repo:
Follow the below steps to setup this application locally on your machine

* 1. Ensure that git is installed on your computer, clone this repository using
```shell
  git clone https://github.com/Abhay1609/flask_crud
```

* 2. Make sure that python is installed on you system
* 3. Go to the root directory and create a virtual environment
```shell
  pip install virtualenvwrapper-win
```
```shell
  python -m venv <name of virtual env>
```

Or if you are using a Linux based machine use
```shell
  apt-get install python3-venv
```

```shell
  mk dir djangoenv
```

```shell
  python3 -m venv flaskenv
```

* 4. Activate the environment:
```shell
  myenv\Scripts\activate
```
Or if you are using a Linux based machine
```shell
  source flaskenv/bin/activate
```

* 5. Now instll the required dependencies:
```shell
  pip install flask bcrypt Flask-PyMongo
```

* 6. All set, now run the application using
```shell
  flask run
```

YOUR APPLICATION WILL RUN ON PORT 5000..

###Using docker image:
* 1. Make sure docker engine is installed on your system and is running

* 2. Pull the docker image using 
```shell
  docker pull abhaypratap9848/abhay-flask
```

* 3 At last run the docker image on your system using:
```shell
  docker run -p 5000:5000 abhaypratap9848/abhay-flask
```

YOUR APPLICATION RUNS LOCALLY ON PORT 5000

##Project ScreenShot:
![post](https://github.com/Abhay1609/flask_crud/assets/113366849/6764e0a9-226f-42e3-877e-ef2327a93808)
![docker](https://github.com/Abhay1609/flask_crud/assets/113366849/053efa69-dd9f-47aa-9d96-775339e8c86b)
![code](https://github.com/Abhay1609/flask_crud/assets/113366849/9fcc1276-b8e1-4e67-bc45-88fcb346298f)
![delete](https://github.com/Abhay1609/flask_crud/assets/113366849/a6646e82-8395-4b78-83dd-fc3d8fffd18c)
![update](https://github.com/Abhay1609/flask_crud/assets/113366849/58fd3199-bba7-4a5b-84ed-020626822254)
![specific](https://github.com/Abhay1609/flask_crud/assets/113366849/dbf402aa-fcab-487e-9cb0-1657525b98f9)
![get user](https://github.com/Abhay1609/flask_crud/assets/113366849/a1fa6a7c-76c5-499a-b47f-c6876a16795f)

##Contacts
Abhay Pratap - [abhaypratap9848@gmail.com](abhaypratap9848@gmail.com)
Github - [https://github.com/Abhay1609](https://github.com/Abhay1609)

##Acknowledgments
* [https://www.python.org/](https://www.python.org/)
* [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
* [https://www.tutorialspoint.com/docker/index.htm](https://www.tutorialspoint.com/docker/index.htm)
