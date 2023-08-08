# Django Money Transfer App

This is a Django web application for managing user accounts and facilitating money transfers between users.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This Django application allows users to create accounts, view user lists, and initiate money transfers between accounts. It uses Django REST framework for API endpoints and provides both function-based and class-based views for various functionalities.

## Features

- Create user accounts with names, IINs (Individual Identification Numbers), and initial balances.
- View a list of users with their details.
- Initiate money transfers between users.
- Basic validation and error handling for account creation and money transfers.
- Responsive and user-friendly front-end templates using Bootstrap.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/EdiPAIN/DRF.git
   ```
2. Create a virtual environment and activate it:
    ```bash
   python3 -m venv venv
   source venv/bin/activate
    ```
3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations to create the database tables:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
6. Access the application in your web browser at http://127.0.0.1:8000/

## Usage
1. Access the User List: http://127.0.0.1:8000/
2. Add a new user: http://127.0.0.1:8000/create/
3. Initiate a money transfer: http://127.0.0.1:8000/transfer/
