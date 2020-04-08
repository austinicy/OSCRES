
# Developer Guide
1. install mysql 
2. run the `database_script.sql` 
3. install django and sql driver:
    conda install django
    conda install mysqlclient
4. instal pyknow:
    clone the repo from "https://github.com/buguroo/pyknow.git"
    go to the project directory and run `pip install .`

5. create database tables by running `table_setup.sh` bash

6. debugging:
    `python3 manage.py runserver 0.0.0.0:8000`
    or add debug configuration for your preferred IDE

7. access the site by "http://localhost:8000/hello"