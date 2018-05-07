It is a Django application over Python3 to provide Graphical User Interface (GUI) to the project Asynchronous_Web_Server in my repository. This django application connects with the other project through HTTP which allows both the services to run isolately even in different machines. <br />

To runserver server use the following procedure to run Django server. This server would need you to also run Asynchronous_Web_Server along with this application to run the test complete functionality. Details for initializing Asynchronous_Web_Server are provided in its repository.<br />

clone this directory using the following command:

```
$ git clone https://github.com/hassaanuah/Django_Application.git

```
Enter the directory and run the installation file. remember to use "take5" as password where it is inquired except the sudo password.
```
$ cd Django_Application/
Django_Application$ sudo bash install.sh
(Remember to use take5 as password)
```

Now to RUN the Django Server follow the following commands:
```
Django_Application/src$ cd src/django_GUI/
Django_Application/src/django_GUI$ python3 manage.py runserver 0:8000
```

Note:
If some locale error occurs while installing django, execute the following commands:
Install all locales when given the option

```
$ export LANGUAGE=en_US.UTF-8
$ export LANG=en_US.UTF-8
$ export LC_ALL=en_US.UTF-8
$ locale-gen en_US.UTF-8
$ sudo dpkg-reconfigure locales
```
