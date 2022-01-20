
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="#">
    <img src="/static/beeyimobile.jpeg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AGRIC PRICES FLARE</h3>

  <p align="center">
    Agric Products Prices Repository
    <br />
    <a href="https://github.com/Kisekka-Alexander/Prices-Flare/issues">Report Bug</a>
    ·
    <a href="https://github.com/Kisekka-Alexander/Prices-Flare/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Software Requirements](#software-requirements)
  * [Project Installation](#project-installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [License](#license)



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

  Our Human Resource Management Information System is an online and fully integrated HR system with a comprehensive suite of modules such as ***leave module***, ***performance module***, ***recruitment module***, ***time module***, ***payroll module***, ***training module*** and ***expense module*** for effective Human Resources Management. Its design is based on the common processes and best practices of the Human Resources functions.

<p>
    With a dynamic on-demand reporting tool, the system enables an HR department to respond faster to HR business needs. Our HRMS suites (HRMIS, TaMIS) includes online (web-based) capabilities, provides powerful easy-to-use features, fitting diverse personnel and payroll requirements in line with the objectives of any organisation.
</p>

### Built With

* [Python 3.8+](https://www.python.org/)
* [JQuery 3.4.1](https://www.jquery.com/)
* 



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Software Requirements

For this application to run successfully, you will need to have the following software.
   * [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
   * [Wampsever](https://www.wampserver.com/en/download-wampserver-64bits/)

### Project Installation
 
 After successful installation and setup of the above software requirements, follow these steps to install the project using the terminal.
1. Clone the repository to a destination directory of your choice
    ```sh
    $ git clone https://github.com/aldookware/hrm-flare.git
    ```
2. Once the project has been cloned, specifically for windows you have to convert `.sh` file in the project to dos - with a tool called dos2unix.exe <br />
    - Download dos2unix for this [link](https://netactuate.dl.sourceforge.net/project/dos2unix/dos2unix/6.0.2/dos2unix-6.0.2-win64.zip)
    - locate the path of the `dos2unix.exe`.
    - run it against the `entry-point.sh`
      ```sh
      $ c:\Users\dos2unix-folder\dos2unix.exe <path-project>\entry-point.sh
      ```
3. Once step 3 is successful, run the commands below 
    ```sh 
    $ docker-compose up -d --build
    ```
    - In another terminal while still within the root folder of the prokect
      ```sh
      $ docker-compose logs -f  # this will show you in real time what is happing to the project
      ```
    - Create migrations and migrate
      ```sh 
      $ docker-compose exec web python manage.py makemigrations
      $ docker-compose exec web python manage.py migrate
      ```
    - Create super user account
      ```sh
      $ docker-compose exec web python manage.py createsuperuser --email <your-email> --username <your-username>
      ```
4. In a browser of your choice go to `http:localhost:8010` 