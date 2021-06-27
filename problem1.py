# Q1 : Scraping and use of Pandas, Numpy

# 1) google search for "yahoo finance apple stock price"

# 2) click on 1st search result

# 3) click on tab "Historical Data"

# 4) click on "download" to download the daily prices in excel format

# 5) Read the data in python

# 6) Compute daily percentage change of "Adj close" to calculate daily returns

# 7) Calculate and plot cumulative returns from simple daily returns computed in Step 6


from selenium import webdriver
import time





driver=webdriver.Chrome()
url='https://in.finance.yahoo.com/quote/AAPL?ltr=1'
driver.get(url)


driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[5]/a').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()


import pandas as pd

df = pd.read_csv ('AAPL.csv')

returns=[0]
cumulative=[0]
for i in range(1,251):
    prev=df.loc[i-1]
    data=df.loc[i]

    prev_close=prev['Adj Close']
    today_close=data['Adj Close']

    change=((today_close-prev_close)/today_close)*100

    data['return']=change
    returns.append(change)
    cumulative.append(cumulative[-1]+returns[-1])

    

df=df.assign(returns=returns)
df=df.assign(cumulative_returns=cumulative)

print(df)

