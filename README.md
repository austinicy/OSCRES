
## Developer Guide

 The project was developed using python3, mysql, and Google DialogFlow.   
 Make sure you have python3 and anaconda installed. Then you can follow this guide to install the rest dependencies

# Python library depencencies
1. install python dependencies:  
    `conda install django`  
    `pip install djangorestframework`  
    `conda install mysqlclient`  
    `pip install google-api-core`  
    `pip install dialogflow`  
    `pip install pandas`

2. instal pyknow:  
    clone the pyknow repo:   
        `git clone "https://github.com/buguroo/pyknow.git" pyknow`   
    go to the created project directory `pyknow` and run `pip install .`  

# Project Setup
1. Clone the project repo "https://github.com/NormanLYJ/OSCRES.git"

# Database
1. install mysql  
    make sure use legecy password authentication is used   

2. In `SystemCode/oscres/settings.py`, in the DATABASES section, modify the USER and PASSWORD based on what you have created.  

3. Similarly, in the `2_table_load.py` file, modify the username and password 

3. connect to you mysql database using below command   
    `mysql -u <USERNAME> -h localhost -p`      
    then run the `0_database_creation.sql`    

5. create database tables by executing below bash file
    `1_table_setup.sh`  

6. load data into mysql tables by 
    `python 2_table_load.py`

# Google DialogFlow
1. zip the folder dialogflow_objects and import the zip file into your Google DialogFlow project
2.  generate a json key file in the Google Dialoge page:   
        General --> Service Account    
        Click the 3 dots --> generate key file   
    name file as `project_key.json`, put it into `/SystemCode` folder     

# Run the application
    Run the applicaiton by below command in the proejct root directory
    `python manage.py runserver 0.0.0.0:8000`   
    or add debug configuration for your preferred IDE

