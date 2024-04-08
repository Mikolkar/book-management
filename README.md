# Book Management

## Description 
This is a **Python** program developed using the **Django** and **Django REST framework**. It provides functionalities for managing books, including their borrowers and order history. Developed by **Mikołaj Karapka** for an **Advanced Python Programming** course. The program uses **Django ORM** for data management, which allows data to be saved either **directly** to the database or through an **REST API**.

## Video Demonstration


https://github.com/Mikolkar/book-management/assets/118861101/2cd200c1-189d-4bd5-8941-2eb859936060


## Features
- Graphical Visualization
- Editing Databases using ORM
- Connecting to Server via API
- Poetry Scripts
- Data Validation
- Remove Data From Database

## Installation

```
poetry install
```

## Run
To run the server, type:

```shell
poetry run runserver
```

## Usage
### There are two ways to use commands.
1.  Type: ```poetry run <command> <args>```
   
2.  Type once: ``` poetry shell```
    and then you can use the commands without ```poetry run```.

#### For example: 
1. ```shell
    poetry run add book "title" "author" "year"
    ```
    
2. ```shell
    poetry shell
    add book "title" "author" "year"
    ```
### Info
To view a list of available commands and their usage, type:
```shell
poetry run info
```
### API
To use the API, add --api at the end of the command 
but before you need to run the server first.
    
#### For example:
```shell
poetry run runserver
poetry run add book "title" "author" "year" --api
```

### Example data
You can also quick add to database some example data. To launch it, simply type:
```shell
poetry run example_data
```
