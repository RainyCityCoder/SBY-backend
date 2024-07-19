# Scientist Birthdays

This full-stack app was designed to fulfill the following requirements:

1. React front-end, demonstrating proper component use, with no topic/subject requirement.
2. Django back-end with 2 or more endpoints accessed by the front end.
3. Deploy the front end to AWS S3.
4. Deploy the back end to AWS EC2.
5. Website is publicly available.

## Table of Contents

1. [Design](#design)
   1. [Front-End](#front-end)
   2. [Back-end](#back-end)
   3. [Database](#database)
2. [Data API](#data-api)
3. [For Developers](#for-developers)
4. [Tech Stack](#tech-stack)

## Design

### **Front-End:**

A React app with minimal dependencies, leveraging Bootstrap for styling. Two components are used to display API response data, with one component being used to display multiple database records via `.map()`. The site itself automatically calls the API; no user interaction is necessary.

### **Back-End:**

Django API offering the following endpoints:

| Request | Endpoint    | Expected results                                                                     |
| ------- | ----------- | ------------------------------------------------------------------------------------ |
| GET     | /bio/       | Retrieves all biologists and birth years in the corresponding SQLite3 table          |
| GET     | /compsci/   | Retrieves all computer scientists and birth years in the corresponding SQLite3 table |

### **Database:**

The SLQite3 database contains two tables of interest:
1. biologists
2. computerscientists

Each table is composed of 3 fields:

1. id (unique, primary key)
2. name
3. birthyear

## For Developers:

To run this code locally on Linux:

Download the front-end repo [here](https://github.com/RainyCityCoder/SBY-frontend), and the back-end repo [here](https://github.com/RainyCityCoder/SBY-backend).

Once downloaded, in your terminal navigate to `SBY-backend/pythonbackend`, and start the Django API with `python3 manage.py runserver`. Please be aware that the API URL in the two `fetch()` commands in `~/SBY-frontend/src/Components/DataDisplay.jsx` will need to be updated. Next, navigate to `SBY-frontend`, and the React SPA may be initiated locally with `npm run dev`, which will provide a link to the running SPA, and should be `http://localhost:5173/`.

## Tech Stack

- React.js front-end
    * React Bootstrap
- Django back-end (API)
    * djangorestframework
    * django-cors-headers
- SQLite3 database