# UnityReach
UnityReach is a comprehensive CRM project designed to assist businesses in managing their customer relationships efficiently. Its features, including the ability to add, delete, and update customer details, make it a valuable tool for maintaining accurate customer data and improving customer engagement. The system's user-friendly interface and reporting capabilities contribute to its effectiveness in enhancing overall customer relationship management.

## Acknowledgements

 - [Screenshots](#screenshots)

 - [Features](#features)
   
 - [Getting_started](#getting_started)
   
- [Usage](#usage)

## Screenshots
  
![project 1](https://github.com/Mehaboob98/CRM/assets/134997058/6191272e-8852-44d6-ae14-91af70144f84)
![project 2](https://github.com/Mehaboob98/CRM/assets/134997058/e5d4b63f-9150-406e-a684-8bbff96e2f47)
![project 3](https://github.com/Mehaboob98/CRM/assets/134997058/c99c2c82-263c-4169-84f3-3f94b438ae3c)
![project 4](https://github.com/Mehaboob98/CRM/assets/134997058/eb95fc8e-3a8c-434d-92a0-d5579a2dec50)
![project 5](https://github.com/Mehaboob98/CRM/assets/134997058/852cdb6b-93bc-4af2-9089-501f3151df86)
![project 6](https://github.com/Mehaboob98/CRM/assets/134997058/6fa5692a-8cd5-4ba1-a1e6-c20ed47ff3dd)

## Features

- User registration and authentication system.
- Add details of customers with infromations like address,mail,phone etc
- Option for deleting and Updating
- Cross platform


## Getting Started

To Clone the project:

```bash
  git@github.com:Mehaboob98/CRM.git
```
Make database migrations:

```bash
  python manage.py makemigrations
  python manage.py migrate
```
Create a superuser for admin access:

```bash
  python manage.py createsuperuser
```
Start the development server:

```bash
  python manage.py runserver
```

- Access the website in your web browser at http://127.0.0.1:8000/.
- To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in using the superuser credentials.

## Usage
- After setting up and running the project, users can register, log in, and start using the CRM website.
- Users can create new customer derails
- Users can View customer details,edit,delete and add new ones
