from pprint import pprint
import requests

BASE_URL = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

session = requests.Session()
session.headers.update(
    {
        'token': TOKEN, 
        'UserAgent': "cja-tech.com,jstrickler@gmail.com", 
        'Accept': "*/*"
    }
)

response = session.get(
    BASE_URL,
    params={
        'datasetid': 'PRECIP_HLY',
#        'stationid': 'COOP:010957',
        'zipid': 'ZIP:27705',
        'startdate': '2000-01-01',
        'enddate': '2000-03-31',
        'limit': 500,  # get up to 500 rows of data
    },
    timeout=10,
)

data = response.json()
# print('-' * 60)
# pprint(data)
# print('-' * 60)

results = data.get('results')
if results:
    for row in results:
        if row['value'] != 99999:
            print(f"{row['date']} {row['station']:20s} {row['value']:3d}")
