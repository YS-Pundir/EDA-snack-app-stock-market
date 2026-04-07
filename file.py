import requests
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px 

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
print("<>"*60)
print("Original data : ")
print(df)

df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')

#  Clean the column names (removing "1. ", "2. ", etc.)
# Instead of '1. open', it becomes just 'open'
df.columns = [c.split('. ')[1] for c in df.columns]

#  Convert all columns to numeric (they come as strings from the API)
df = df.apply(pd.to_numeric)

#  Convert the index to actual Datetime objects
df.index = pd.to_datetime(df.index)
print("-"*60)
print("Data After cleaning : ")
print(df)
# 2. INspecting the data quality , looking for  missing data or incorrect datatypes
print("-"*50)
print("Sumamry of data structure : ")
print()
print()
print(df.info())
print("Summary of the null values in DF : ")
print(df.isnull().sum())

# 3. inspecting the distribution in the data 
fig1=px.histogram(
    df,
    x="volume",
    title="Distribution of volume"
)
fig1.show()

fig2=px.histogram(
    df,
    x="open",
    title="Distribution of open data"
)
fig2.show()

# 4. inspecting the outliers

fig3=px.box(
    df,
    y="volume",
    title="Outliers of volume in data"
)
fig3.show()
fig4=px.box(
    df,
    y="open",
    title="Outliers of open data"
)
fig4.show()

# 5. inspecting the coorelation bitween the variables in df
corr=df.corr(numeric_only=True)
fig5=px.imshow(
    corr,
    text_auto=True,
    title="Corelation heat map"
)
fig5.show()
