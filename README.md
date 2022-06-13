<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">RENEWABLE ENERGY</br>DEVELOPMENT SCENARIOS</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/AlessandroCogollo/CompEng-Project2022/blob/main/docs/deliverables/documentation.pdf"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AlessandroCogollo/CompEng-Project2022/issues">Report Bug</a>
    ·
    <a href="https://github.com/AlessandroCogollo/CompEng-Project2022/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Features</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()

The proposed project aims to create an <b>interactive web interface</b> which will be integrated in the RSE S.p.A. dissemination platforms, for <b>supporting future renewable energy development scenarios</b>, which constitutes one of the core activities in RSE. The website will support the computation of the photovoltaic capacity distribution and the expected production in Italy at a province scale for the achievement of the European Green Deal goals. Starting from variable input parameters and spatial indicators, the interface should allow the spatial and graphical representation of the intermediate and final outputs.

More can be found [here](https://github.com/AlessandroCogollo/CompEng-Project2022/blob/main/docs/deliverables/Presentation.pptx)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

For this project Python was choosen as the programming language for this project, since it possesses a broad variety of libraries very well suited to develop custom applications in the field of geospatial analysis. More in depth, the libraries and software used were:

* [Flask](https://flask.palletsprojects.com/en/2.1.x/)  is a web framework built with a small core and easy-to-extend philosophy. It's ideal for a small app like this project.
* [Pandas](https://pandas.pydata.org/) and [Psycopg2](https://www.psycopg.org/docs/) are flexible and powerful libraries when it comes to operate with data, which were, in this project in particular, used to interrogate the database. 
* [Bootstrap](https://getbootstrap.com) is powerful, extensible, and feature-packed frontend toolkit used do develop a user interface. There is no need to reinvent the wheel each time!
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This project is meant to be deployed as a web app, thus it requires a webserver to work. For development purposes it can be tested locally.

### Local Deployment
#### Prerequisites
Obviously, you need python3 installed on your computer; to install it, follow this guide 
[getting started with Python3](https://docs.python-guide.org/starting/install3/linux/)
#### Installation

1. First, clone this repository via HTTPS with
    ```sh
   git clone https://github.com/AlessandroCogollo/CompEng-Project2022.git
   ```
2. Navigate to the flaskr module, if you're using bash, type
   ```sh
   cd <your project repository>/project/flaskr
   ```
3. Execute the project
   ```sh
   flask run
   ```
    For development purposes, server can be run under `development` mode. To do that, kill flask process using `CTRL^C`, then type: 
    ```sh
    export FLASK_ENV="development"
    flask run
    ```
4. Go to `http://127.0.0.1:5000/` and check it out!


### Deploying With Heroku 
[Heroku](https://www.heroku.com/) is a service that allows you to deploy this Python web application so that anyone with the link will be able to use it.
Obviously, you need python3 installed on your computer; to install it, follow this guide 

#### Prerequisites

1. First, create an account to Heroku
2. Click the button that says `Create New App`. Give your application a name, and click `Create App`

#### Installation

1. First, add this repository to your github doing a `fork`
2. Choose `GitHub` as deployment method, and connect your account
3. Search for your forked repository and link it to heroku
4. Choose `automatic deployment`
5. Choose the branch to develop (maintained is `main`) and deploy

### Other Hosts
Plenty of hosting solutions are available to run your application. [Here a guide can be found](https://flask.palletsprojects.com/en/2.1.x/deploying/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Features
As required by the project specifications, the developed web app permits to plot and compare map plots based on parameters inputted by the user; output values can be inspected at a province scale thanks to a tooltip that is triggered and shown on mouse over event.  

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alessandro Cogollo - [@linkedin](https://www.linkedin.com/in/alessandrocogollo/?originalSubdomain=it) - alessandro.cogollo@mail.polimi.it


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/AlessandroCogollo/CompEng-Project2022/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alessandrocogollo/?originalSubdomain=it
[product-screenshot]: images/screenshot1.png
