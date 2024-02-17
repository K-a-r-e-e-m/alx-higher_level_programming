# Object-relational mapping
In thi project we will link two amazing worlds: Databases and Python!

In the first part, we will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, we will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).


## Learning Objectives
-  `python` `OOP` `SQL` `MySQL` `ORM` `SQLAlchemy`
- [x] How to connect to a MySQL database from a Python script
- [x] How to `SELECT` rows in a MySQL table from a Python script
- [x] How to `INSERT` rows in a MySQL table from a Python script
- [x] What ORM means
- [x] How to map a Python Class to a MySQL table
- [x] How to create a Python Virtual Environment

## Working on Virtual Environment
#### Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```shell
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install MySQLdb module version 2.0.x
```shell
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

## Install SQLAlchemy module version 1.4.x
```shell
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```
