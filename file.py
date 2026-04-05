import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

api_key=os.getenv("api_key")


url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"TIME_SERIES_DAILY","symbol":"MSFT","outputsize":"compact","datatype":"json"}

headers = {
	"x-rapidapi-key": "29d04bb977msh6e6ccf157115028p116a36jsndf3231f7d1da",
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code==200:
    data=response.json()
else:
    print(response.status_code)

df=pd.DataFrame(data)
print(df)
