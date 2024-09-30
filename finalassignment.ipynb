import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings("ignore", category=FutureWarning) # Ignore all warnings

# Q1 -> Use yfinance to Extract Stock Data of Tesla
tesla = yf.Ticker("TSLA")
company1_name=tesla.info['longName']
print("Company Name:" , company1_name)
len_1=len(company1_name)
print("=" * (len_1+14))
tesla_data = tesla.history(period="max") # change the period as 5days, 1 month, etc
tesla_data.reset_index(inplace=True)
df=pd.DataFrame(tesla_data)
df=df.round(2)
print(df.to_string())
# Q1 -> Ends


# Q2 -> Use Webscraping to Extract Tesla Revenue Data
url ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data,"html.parser")
tesla_tables = soup.find_all("table")
data = []
for row in soup.find_all("tbody")[1].find_all("tr"):
       col = row.find_all("td")
       date = col[0].text
       revenue = col[1].text.replace("$", "")
       data.append((date,revenue))
tesla_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace('[,\\$]', "", regex=True)
print(tesla_revenue)
print("=" * 50)
# Q2 -> Ends


# Q3 -> Use yfinance to Extract Stock Data of GameStop Corp. (GME)
gme = yf.Ticker("GME")
company2_name=gme.info['longName']
print("Q3 - > Company Name:" , company2_name)
len_2=len(company2_name)
print("=" * (len_2+20))
gme_data = gme.history(period="max") # change the period as 5days, 1 month, etc
gme_data.reset_index(inplace=True)
df1=pd.DataFrame(gme_data)
df1=df.round(2)
print(df1.to_string())
print("=" * 95)
# Q3 -> Ends


# Q4 -> Use Webscraping to Extract GameStop Corp. Revenue Data
url ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data,"html.parser")
gme_tables = soup.find_all("table")
data = []
for row in soup.find_all("tbody")[1].find_all("tr"):
       col = row.find_all("td")
       date = col[0].text
       revenue = col[1].text.replace("$", "")
       data.append((date,revenue))
gme_revenue = pd.DataFrame(data, columns=["Date", "Revenue"])
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace('[,\\$]', "", regex=True)
print(gme_revenue)
print("=" * 50)
# Q4 -> Ends


# Q5 and Q6 starts
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
                        height=900,
                        title=stock,
                        xaxis_rangeslider_visible=True)
    fig.show()
make_graph(tesla_data,tesla_revenue,'tesla')
make_graph(gme_data,gme_revenue, 'gme')
