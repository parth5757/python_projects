import requests
from bs4 import BeautifulSoup

def get_job_listings(location, query):
    base_url = "https://in.indeed.com/"
    url = f"{base_url}/jobs?q={query}&l={location}&jt=internship"
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_elements = soup.find_all('div', class_='jobsearch-SerpJobCard')

    job_listings = []
    for job_element in job_elements:
        title = job_element.find('h2', class_='jobTitle').find('span').text.strip()
        print(title)
        company = job_element.find('span', class_='css-92r8pb').text.strip()
        print(company)
        location = job_element.find('div', class_='css-1p0sjhy').text.strip()
        print(location)
        link = base_url + job_element.find('a')['href']
        print(link)
        job_listings.append({'title': title, 'company': company, 'location': location, 'link': link})
        print(job_listings)
    return job_listings

def print_job_listings(job_listings):
    print(job_listings)
    print("print list calling")
    for i, job in enumerate(job_listings, start=1):
        print("printing started")
        print(f"Job {i}:")
        print(f"Title: {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Link: {job['link']}")
        print()

def main():
    location = input("Enter location: ")
    query = input("Enter query (e.g., Python intern developer): ")
    job_listings = get_job_listings(location, query)
    print_job_listings(job_listings)

if __name__ == "__main__":
    main()