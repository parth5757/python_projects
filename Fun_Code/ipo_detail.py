import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_ipo_data(year):
    url = f"https://www.chittorgarh.com/report/sme-ipo-list-in-india-bse-sme-nse-e221merge/84/?year={year}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return pd.DataFrame()  # Return empty DataFrame in case of failure

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the correct table based on the class attribute
    table = soup.find('table', {'class': 'table table-bordered table-striped'})
    if not table:
        print("Failed to find the table in the HTML content")
        return pd.DataFrame()  # Return empty DataFrame in case of failure
    
    # Extract headers
    headers = [header.text.strip() for header in table.find_all('th')]
    
    # Extract rows
    rows = []
    for row in table.find_all('tr')[1:]:
        cells = [cell.text.strip() for cell in row.find_all('td')]
        print("hellos")
        if cells:
            rows.append(cells)
            print(rows)
    # Create DataFrame
    df = pd.DataFrame(rows, columns=headers)
    
    # Filter data by year if 'Listing Date' is available
    if 'Listing Date' in df.columns:
        df['Listing Date'] = pd.to_datetime(df['Listing Date'], format='%b %d, %Y', errors='coerce')
        df = df[df['Listing Date'].dt.year == year]
    
    return df

# Use the function to get SME IPO data for 2023
ipo_data = scrape_ipo_data(2023)
print(ipo_data)

# Save to CSV
ipo_data.to_csv('sme_ipo_data_2023.csv', index=False)