import numpy as np
import pandas as pd
import re

import django.db as db

from mysite.crimesapp.models import Crime

def delete_data():
    Crime.objects.all().delete()

def load_data(file_name):
    return pd.read_csv(file_name)

data = load_data('./SPD_Reports.csv')
delete_data()

def ingest_data(data):
    i = 0
    # print("num of rows in data: " + data.)
    for idx, values in data.iterrows():
        val = values.values
        if type(val[3]) != str or type(val[2]) != str:
            continue
        if type(val[4]) != str:
            val[4] = None
        m = re.search('(?<=T).*?(?=:)', val[3])
        time = int(m.group(0))
        crime = Crime(offense_type=val[0], offense_description=val[1], report_date=val[2], \
            offense_start_date=val[3], offense_end_date=val[4], block=val[5], district=val[6], \
            beat=val[7], census_tract=val[8], longitude=float(val[9]), latitude=float(val[10]))
        crime.save()

        # i += 1
        # if i % 1000 == 0:
        #     db.session.commit()
        #     db.session.close()
        #     p = i / 700000.
        #     # print str(p) + '%'


ingest_data(data)
