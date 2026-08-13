import pandas as pd
from numpy.ma.core import count
import random
import secrets
def read_excel(path):
    global random_csv
    global a
    global b

    ranom_csv = pd.read_csv(path)
    b=ranom_csv.to_dict(orient='records')

def make_random():
    a=0+secrets.randbelow(count(b)+1)
    global random_name
    for index,name_random in enumerate(b):
        if a==index:
            random_name=name_random
    return random_name
