# seattle crime django backend
**NOTE** we are using **Django 3.0**, which supports **Python 3.6** and later 
1. install dependencies using `pip3 install -r requirements.txt`
2. run `python3 manage.py makemigrations` to create migrations for database
3. run `python3 manage.py migrate` to apply those changes to the database
4. create a django admin user with `python3 manage.py createsuperuser`
5. download `SPD_Reports.csv` from [this kaggle dataset](https://www.kaggle.com/sam/seattle-crime?fbclid=IwAR2KUlA-2XJsWgiN26r5sU4nykT6SX3Avgq40xjIK26NqcZh86p-sJ_9mZM#SPD_Reports.csv) and place it in the root directory
6. run `python3 manage.py shell` to get into the interactive django shell
7. run `exec(open('ingest.py').read())` to ingest the `SPD_Reports.csv` into the  sqlite3 database
8. start the server using `python3 manage.py runserver`
9. open `http://127.0.0.1:8000/admin/` in your browser and log in with your superuser credentials
10. verify that `Crimes` table exists under `crimesapp` in the gui


