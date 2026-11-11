# Personal Task Manager
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)


A simple task manager built with python for learning git & github

## Features

- add multiple tasks
- save tasks
- load saved tasks
- admin mode
- set task priority

## Task priority 
Each task can have one of thes priority levels:
- low
- medium
- high
  
## Requirements
- Python
- python-dotenv

## Project Structure

```task
personal_task_manager_main/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   tasks.py
│
├───images
│       demo.gif
│       sc1.png
```

## Installaion
Install the requires packages:

```bash
python -m pip install -r requirements.txt
```

## Envoiroment Setup
create a `.env` as a template

Use `.env.example` as a template

Add your admin password

```env
admin_pass = your_password_here
```

replace `your_passsword_here` with your own admin password

## Run the Programm
run the main file
```bash
python main.py
```

## Screenshot 
![personal_task_manager_screenshot](images\sc1.png)

## Demo
![personal_task_manager_demo](images\demo.gif)