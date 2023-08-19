# Brew-Tea-Full Final Project!
![Untitled_Artwork 6](https://user-images.githubusercontent.com/109074529/231804566-2a389d56-46c7-4b31-a678-c8d057143d71.png)
_____________________________________________________________________________________________________________________

# Elevator Pitch!

Our café owners (SuperCafé) want to be able to; <br />
• monitor multiple stores, <br />
• obtain sales data and, <br />
• check their stock levels in real-time. 

**We offer** a backend system that visually displays sales data and more from multiple data sources. 

The system enables the owner to check live data, such as the number of coffees sold and their most loyal customers unlike their current manual ordering system which is time-consuming. 

**With our product**, Super Café can conveniently reorder stock, discover marketing opportunites, and review sales data from the comfort of their own location.

_______________________________________________________________________________________________________________________

# Project Goal

As a team, we aim to create robust data pipelines that convert and load 100 .csv files daily. We seek to enable client-side functionality through interpretation of crucial sales data. 

We will measure our progress through; weekly team retro’s and live data visualisation.

In order to achieve this we will work together using agile methodology. We have created a ways of working agreement which can be viewed [here](https://github.com/generation-de-lon9/brew-tea-full-final-project/blob/main/documentation/ways_of_working.MD).

Our primary focus will be delivering the bedrock technical requirements before adding extra functionality.

We aim to deliver this in 5 weeks.

_______________________________________________________________________________________________________________________

# Team Members

[Charlene](https://github.com/ck1ldn) <br />
[Kahlail](https://github.com/kahlail) <br />
[Minhaz](https://github.com/mu601) <br /> 
[Sajjad](https://github.com/spopal) & <br />
[Zain](https://github.com/Zainkhanshin)

_______________________________________________________________________________________________________________________

# Technology Stack
• Python 3.10  <br />
• Postgres  <br />
• AWS Services including S3, Lambda, Redshift, Quicksight and Cloudwatch  <br />
• Grafana
_______________________________________________________________________________________________________________________

# How to run our code locally

We recommend creating a virtual enviroment, where you can download the dependencies from our [requirements.txt](https://github.com/generation-de-lon9/brew-tea-full-final-project/blob/main/src/requirements.txt) file. <br />

1. From the root (brew-tea-full-final-project), move your terminal into the correct folder
```
cd src
```
<br />

2. Creating a virtual environment on Windows
```
py -m venv .venv
```
<br />
&nbsp; &nbsp; &nbsp; Creating a virtual environment on Mac 

```
python3 -m venv .venv
```
<br />
<br />

3. Activate virtual environment on Windows

```
.venv\Scripts\activate
```

&nbsp; &nbsp; &nbsp; Activate virtual environment on Mac
```
source .venv/bin/activate
```
<br />
<br />

4. Installing dependencies
```
pip install -r requirements.txt
```
<br />

_______________________________________________________________________________________________________________________

# ETL pipline

When csv files are uploaded to the S3 bucket, the lambda is triggered. The lambda goes on to process the files then inserts the data onto the Redshift database. As soon as data in inserted to the database, the Grafana dashboard is updated.

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/bac89ff4-9bc0-4499-8eaf-9cd913c7c0b4)

_______________________________________________________________________________________________________________________

# End Result - Grafana Dashboard

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/557995e8-a0bc-4ae1-89cf-0159c2913850)

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/284562a4-5e7b-49b9-9ebc-11250bdd6633)

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/bd46d06f-1785-4168-9780-0c488b0d22c0)

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/5b7a3119-e085-4f03-83b7-66a753f78729)

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/b9d9eae9-e574-4e01-898f-e46584b3f373)

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/cff6cc53-627b-4c3e-92c7-b6c13f0d647a)

![image](https://github.com/mu601/brew-tea-ful-project/assets/127961097/1a0c63cd-ae55-4c03-bfa4-099f5814bcc3)












