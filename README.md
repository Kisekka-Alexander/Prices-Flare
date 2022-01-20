
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
* [MySql](https://www.w3schools.com/mySQl/default.asp)




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
    $ git clone https://github.com/Kisekka-Alexander/Prices-Flare.git
    ```
2. Once the project has been cloned, you have to configure the config file in C:\wamp64\apps\phpmyadmin4.9.2 
to connect to the online heroku db by adding the content from the dbconfig file<br />
3. Once step 3 is successful, run the commands below 

    - In the terminal while still within the root folder of the project
      ```sh
      $ env:FLASK_APP="app"
      ```
        ```sh
      $ env:FLASK_ENV="development"
      ```
        ```sh
      $ flask run
      ```
4. In a browser of your choice go to `http:localhost:5000` 