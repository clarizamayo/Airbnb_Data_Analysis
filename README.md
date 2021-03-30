<div align="center"><img src="./img/head.jpg"></div>

## Contents

- [Acknowledgement](#acknowledgement)
- [Introduction](#introduction)
- [Technology Used](#technology-used)
- [Data Cleaning](#data-cleaning)
- [Hypothesis](#hypothesis)
- [Conclusion](#conclusion)
- [Summary](#summary)

# AIRBNB DATASET ANALYSIS
## Our Study
**The [current](https://www.kaggle.com/ivanovskia1/nyc-airbnb-rental-data-october-2017) NYC AirBnb Rental data October 2017 contains information about airbnb listings. It has it's location by latitute and longitude as well as the neighborhood,borough. It also has its price per night, amount of bedrooms, bathrooms ect.**

The aim of our study is to explore the data and look for factors that might have contributed to Airbnb sucess. Futhermore, find out if we can find any patterns and predict the location and price of a listing. 

<br>

## Technology Stack
In this analysis, we used python as the primary programming language because of its rich palette of tools that make data analysis a cinch. Some of the packages we used are
| Library | Description |
| --- | --- |
| [Matplotlib](https://matplotlib.org/) | Matplotlib is an extremely versatile library of tools for generating interactive plots that are easy to interpret and customise. |
| [Numpy](https://github.com/numpy/numpy) | Numpy is a popular library used for array manipulation and vector operations. It is used extensively across python projects that require scientific computing. |
| [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) | Pamdas is another library for data science that is just as popular as numpy. It provides easy to use data structures and functions to manipulate structured data. |
| [Seaborn](https://seaborn.pydata.org/) | Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. |
| [Sqlite3](https://www.sqlite.org/index.html) | Sqlite3 is a C library that provides a lightweight disk-based database that allows accessing the database using a nonstandard variant of the SQL query language. |
| [Folium](https://python-visualization.github.io/folium/) | Folium makes it easy to visualize data that’s been manipulated in Python on an interactive leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing rich vector/raster/HTML visualizations as markers on the map. |

These tools are well documented and come with several examples that make it easy to start using them. You can check out the linked documentation pages for more information.

## Data Cleaning

The most important step to take before we get started geenrating any kind of information from all these data sources, it is first important to clean our data and make sure that the datasets are compatible with each other. Since most of the data is divided on a host id basis, we must make sure that all the rows have values and cantain the same formatting.

### What should we look into / errors?
- some rows have bathrooms of value 0 (min bathrooms)
- some rows have bedrooms of value 0 (min bedrooms)
- some rows have beds of value 0 (min beds)
- some rows have square feet of value 0 (min square_feet)
- some rows have price of value 0 (min price)
- some rows have price of 10000 dollars per night (max price)
- there is a minimum nights reqirement stay of 1250 days (max minimum_nights)
- 0 days availability for 30 days (min availability_30) - this one may be a legit requirement
- look into maximum_nights column format

# Hypothesis
#### What do we understand from this? 

## Linear Regression
#### Hypothesis 

The following features are the best predictors for ***price*** of airbnb listings:

- Boroughs
- Accommodates
- Bathrooms
- Bedrooms 
- Beds 
- Number of guest included (in price)

## Multinomial Logistic Regression
#### Hyppothesis  

The following features are the best predictors for ***location*** of airbnb listings:

- Accommodates
- Bathrooms
- Bedrooms 
- Beds 
- Number of guest included (in price)
- Minimun nights

## About us

| Preview                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [<img src="./img/clariza.jpg" width="250" />](https://i.imgur.com/0OoLaa5.png)                                                                                                                                                | Clariza is an Ambitious data science fellow committed to academic excellence. Prepared to implement diverse skill sets, technical proficiencies and new perspectives to leadership personnel. Adaptable and driven with strong work ethic and ability to thrive in team-based or individually motivated settings. At her core, she is a problem solver and experimenter who’s passionate about using sociological and data driven approaches to tackling projects and building meaningful products that help people live better lives. She has worked in Medical billing, consumer and customer service and is now looking to pivot her career path towards Data Science.                                                                                    |
| [<img src="./img/stani.jpg" width="250" />](https://i.imgur.com/0OoLaa5.png)                                                                                                                                                | Stanislava is a life-long learner with a background in Marketing and a passion for Cybersecurity & Data. Team-focused, resourceful, and detail-oriented with a successful record of over 7 years of client-facing experience. Seeking to effectively bridge the gap between Engineering and Business Teams, along with the capability of rendering excellent technical and communications skills.
                                                                                         |
| [<img src="./img/janet.jpg" width="250" />](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/DataScienceEightSteps_Full.png)                    | Placeholder              |