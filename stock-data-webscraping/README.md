# Stock Data Webscraping

## Overview
Investors need to examine trends that dictate whether their share price will rise or fall. Data scicence can be used to visual data relationships that influences shares. In this project, I take on the role of a junior data scientist with the objective of structuring stock and revenue data for Tesla and GameStop to build an investor dashboard.

## Extracting Tesla Stock Data
To extract stock data from Tesla, the **yfinance** library is used where a Ticker object downloads the stock data to the lab notebook. The **history** method with a parameter **period="max"** will show the full stock data period.

<img width="1847" height="755" alt="extract-tesla-stock-data" src="https://github.com/user-attachments/assets/5a280016-d583-4ed2-b358-42a75eec6f6b" />

## Webscraping Tesla Revenue Data
To acquire quarterly revenue data for Tesla, a url provided by IBM was used to access a revenue table. The HTML data was parsed using BeautifulSoup and loaded into a pandas DataFrame using the **read_html** function. Columns were renamed for simplicity to "Date" and "Revenue", and the revenue data was reformatted for graphing purposes. The final DataFrame can be seen here: 
<img width="307" height="277" alt="tesla-revenue" src="https://github.com/user-attachments/assets/fabf0e66-840c-4eb9-bbac-532a07c42dee" />

## Extracting GameStop Stock Data
The **yfinance** library is used once more with a Ticker object to download GameStop stock data. The **history** method is called with a the parameter **period="max"* to acquire the full GameStop stock data. 

<img width="1857" height="747" alt="extract-gme-stock-data" src="https://github.com/user-attachments/assets/de2a5a64-5e0f-4012-bca1-6936869d820e" />

## Webscraping GameStop Revenue Data
To acquire quarterly revenue data for GameStop, the same methodology was used with a different url provided by IBM. The final DataFrame can be seen here:

<img width="298" height="266" alt="gamestop-revenue" src="https://github.com/user-attachments/assets/c1188c43-f4ec-45c5-b05e-663eec7f46c8" />

## Tesla Data Visualizations
The stock and revenue for Tesla were plotted with the aid of a helper function from IBM. The following plots reveal that both the share price and revenue for Tesla have sharply rised over time:

<img width="1108" height="757" alt="tesla-share-revenue-plots" src="https://github.com/user-attachments/assets/4784eefd-e215-4d50-8b66-d5917f6c4806" />

## GameStop Data Visualizations
The stock and revenue for GameStop were plotted with the same helper function from IBM. While the revenue plot showed no significant growth, the share price skyrocketed in recent years:

<img width="897" height="625" alt="gme-share-revenue-plots" src="https://github.com/user-attachments/assets/22d9f724-0977-4479-ade7-de0dd5003e3b" />

## Business Insights
An investor can gather that Tesla should see an increase in share price as there revenue grows. Althouth the share price for GameStop rose dramatically, there is no clear indicator that the share price will maintain its value with its flippant revenue numbers. 

## Getting Started
1. Download Anaconda Navigator and create a virtual environment.
2. Download Visual Studio Code and get the Python and Jupyter Notebook Extensions.
3. Ensure Python 3.12 or higher is installed and the path is in the system path of your environment variables.
4. Install the ipykernel extension to modify notebook cells.
5. Clone the repository to a project folder with:
```
git clone https://github.com/Cameron-Nann-Python/ibm-data-science-projects/tree/main/stock-data-webscraping
```

## Technologies Used
- Anaconda Navigator
- Visual Studio Code
- Python

## Required Libraries
- yfinance
- pandas
- bs4
- nbformat
- matplotlib
- lxml

## Files Included
- `Analyzing Historical Stock-Revenue Data and Building a Dashboard.ipynb`: lab notebook containing full webscraping workflow and visualizations
