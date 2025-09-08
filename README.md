# Scientist Birthdays Backend

This full-stack app was originally designed to fulfill the following requirements:

1. React front-end, demonstrating proper component use, with no topic/subject requirement.
2. Django back-end with 2 or more endpoints accessed by the front end.
3. Deploy the front end to AWS S3.
4. Deploy the back end to AWS EC2.
5. Website is publicly available.

As the AWS free account that originally hosted this project has lapsed a new hosting solution needed to be found to keep the app affordable. After some research, Supabase, Render, and XXXX were chosen to host the database, API, and front-end respectively. 

## Table of Contents

1. [Design](#design)
   1. [Front-End](#front-end)
   1. [Back-end](#back-end)
   1. [Database](#database)
1. [Data API](#data-api)
1. [For Developers](#for-developers)
1. [Tech Stack](#tech-stack)
1. [Contributing](#contributing)
1. [Resources](#resources-utilized)

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

The PostgreSQL database contains two tables of interest:
1. biologists
2. computerscientists

Each table is composed of 3 fields:

1. id (unique, primary key)
2. name
3. birthyear

## For Developers:

To run this code locally on Linux:

Download the front-end repo [here](https://github.com/RainyCityCoder/SBY-frontend), and the back-end repo [here](https://github.com/RainyCityCoder/SBY-backend).

Once downloaded, in your terminal navigate to `SBY-backend/pythonbackend`, run `pip install -r requirements.txt`, and start the Django API with `python3 manage.py runserver`. Please be aware that the API URL in the two `fetch()` commands in `~/SBY-frontend/src/Components/DataDisplay.jsx` will need to be updated. Next, navigate to `SBY-frontend`, and the React SPA may be initiated locally with `npm run dev`, which will provide a link to the running SPA, and should be `http://localhost:5173/`.

## Tech Stack

- [React.js front-end](https://github.com/RainyCityCoder/SBY-frontend)
    * Bootstrap
- [Django back-end (API)](https://github.com/RainyCityCoder/SBY-backend)
    * djangorestframework
    * django-cors-headers
- SQLite3/PostgreSQL database

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## Resources utilized

- [foadbotan](https://gist.github.com/foadbotan/ba617102ab15eb648947afbbb88295cb)
- [CBI Analytics](https://www.youtube.com/playlist?list=PLmEKHA8iFrmCAPgSe9ze8RXXdE0M11suR)
- [Supbase docs](https://supabase.com/docs/guides/database/import-data)
- [Render docs](https://render.com/docs/deploy-django#updating-an-existing-django-project)
- ChatGPT