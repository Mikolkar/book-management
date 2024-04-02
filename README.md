# Book Management

## Description 
This is a **Python** program built using the **Django** framework. It provides functionalities for managing books, including their borrowers and order history. Developed by **Mikołaj Karapka** for an **Advanced Python Programming** course, the application allows data population through either the **ORM** or an **API**.

## Video Demonstration - TO DO

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
but before you run the server:
    
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
