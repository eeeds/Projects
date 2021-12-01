def web_scraping_part():
    """
    In this function we collect data from a web page. Especifically, the web page of the List of largest banks in Wikipedia.
    """
    import requests
    import bs4
    import pandas as pd


    url = ' https://en.wikipedia.org/wiki/List_of_largest_banks'
    r = requests.get(url)
    if r.status_code == 200:
        html_data = r.text
    else:
        print('Error')
    
    #Scraping the data
    soup = bs4.BeautifulSoup(html_data, 'html.parser')
    """
    Load the data from the `By market capitalization` table into a pandas dataframe. 
    The dataframe should have the country `Name` and `Market Cap (US$ Billion)` as column names. 
    Using the empty dataframe `data` and the given loop extract the necessary data from each row and append it to the empty dataframe.
    
    """
    data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

    for row in soup.find_all('tbody')[3].find_all('tr'):
        col = row.find_all('td')
        if len(col) > 0:
            data = data.append({'Name': col[1].text.replace('\n', ''), 'Market Cap (US$ Billion)': col[2].text.replace('\n', '')}, ignore_index=True)
        else:
            continue
    #Saving the file into a json file
    data.to_json('bank_market_cap.json', orient='records')

def data_from_api():
    """
    In this function we collect data from an API. Especifically, the ExchangeRatesAPI.
    
    """
    import requests
    import json 
    import pandas as pd

    #Obtain api_key from a json file
    with open('credentials.json', 'r') as f:
        data = json.load(f)
    api_key = data['key']
    url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key={}".format(api_key)
    # Turn the data into a dataframe
    response = requests.get(url)
    data = response.json()
    df= pd.DataFrame({'Rates': data['rates'].values(), 'Currency': data['rates'].keys()})
    df.set_index('Currency', inplace=True, drop = True)
    df = df.rename_axis(None)
    #Drop na values
    df = df.dropna(axis= 1)
    #Save into a csv file
    df.to_csv('exchange_rates_1.csv')

def log(message):
    """
    This is a logging function.
    
    """
    from datetime import datetime

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

def extract_from_json(file):
    """
    This function allow you to extract data from a json file
    """
    import pandas as pd
    
    df = pd.read_json(file)
    return df


if __name__=='__main__':
    #web_scraping_part()
    #data_from_api()