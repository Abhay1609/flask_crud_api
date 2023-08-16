# Flask CRUD
BY Abhay Pratap

This is a python based application on flask along with the mongoDB as the database, this application contains a dockerfile for the ease of deployment and testing, you can directly you this application via docker image(Steps provided below)

## To setup:

### Using the git repo:
Follow the below steps to setup this application locally on your machine

1. Ensure that git is installed on your computer, clone this repository using
```shell
  git clone https://github.com/Abhay1609/flask_crud
```

2. Make sure that python is installed on you system

3. Go to the root directory and create a virtual environment
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

4. Activate the environment:
```shell
  myenv\Scripts\activate
```
Or if you are using a Linux based machine
```shell
  source flaskenv/bin/activate
```

5. Now instll the required dependencies:
```shell
  pip install flask bcrypt Flask-PyMongo
```

6. All set, now run the application using
```shell
  flask run
```

YOUR APPLICATION WILL RUN ON PORT 5000..

### Using docker image:
1. Make sure docker engine is installed on your system and is running

2. Pull the docker image using 
```shell
  docker pull abhaypratap9848/abhay-flask
```
3. Build docker
```shell
  docker build -t abhaypratap9848/abhay-flask .
```
   
4 At last run the docker image on your system using:
```shell
  docker run -p 5000:5000 abhaypratap9848/abhay-flask
```

YOUR APPLICATION RUNS LOCALLY ON PORT 5000.....

## Project Video:


https://github.com/Abhay1609/flask_crud/assets/113366849/c06fd190-607f-4605-8973-9b8bf1c640e4


## Project ScreenShot:
![new_model](https://github.com/Abhay1609/flask_crud/assets/113366849/214369f7-f445-4d7c-b790-e8d8254ea1d6)
![new_view](https://github.com/Abhay1609/flask_crud/assets/113366849/fdb43f39-e9ec-4f5d-8060-62bff93675ac)
![new_control](https://github.com/Abhay1609/flask_crud/assets/113366849/0e9a03fb-6e2d-4271-9fb6-2279ae1bf395)
![new_docker](https://github.com/Abhay1609/flask_crud/assets/113366849/46a43466-44d4-4432-a2b7-508c9487fb01)
![new_build](https://github.com/Abhay1609/flask_crud/assets/113366849/6a0c3632-66da-4174-bec5-8c07004287b2)
![new_post](https://github.com/Abhay1609/flask_crud/assets/113366849/fd791974-d137-4652-9c9c-4527aed3afcf)
![new_post_db](https://github.com/Abhay1609/flask_crud/assets/113366849/884a6e9a-b834-4cdd-9ab2-b8cc77dcb7fa)
![new_get](https://github.com/Abhay1609/flask_crud/assets/113366849/44774a09-46cb-465e-92b2-2a7156163e1b)
![specific](https://github.com/Abhay1609/flask_crud/assets/113366849/b2e5bb9b-24c3-42fe-954f-1ed90ae9a8f6)
![new_update](https://github.com/Abhay1609/flask_crud/assets/113366849/d276ecc3-6031-4238-926e-007d3bd7ecb2)

![new_update_db](https://github.com/Abhay1609/flask_crud/assets/113366849/8f415a3d-88d6-47d1-a894-7750b8cc5524)
![new_delete](https://github.com/Abhay1609/flask_crud/assets/113366849/0f2bd004-3251-4b7e-833c-d96ee0cb2669)
![new_delete_db](https://github.com/Abhay1609/flask_crud/assets/113366849/da38449c-2aa5-4fbc-92a5-b5128cbb0d65)











## Contacts
* Abhay Pratap - [abhaypratap9848@gmail.com](abhaypratap9848@gmail.com)
* Github - [https://github.com/Abhay1609](https://github.com/Abhay1609)

## Acknowledgments
* [https://www.python.org/](https://www.python.org/)
* [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
* [https://www.tutorialspoint.com/docker/index.htm](https://www.tutorialspoint.com/docker/index.htm)
