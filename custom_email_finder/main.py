import requests
from dns.resolver import Resolver
import tldextract
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import re
import time
import signal

class TimeoutError(Exception): pass

def timeout_handler(signum, frame):
    raise TimeoutError()

signal.signal(signal.SIGALRM, timeout_handler)

def extract_domain(email):
    return tldextract.extract(email).registered_domain

def check_mx_record(domain):
    resolver = Resolver()
    try:
        answers = resolver.resolve(domain, 'MX')
        mx_records = [rdata.exchange.to_text() for rdata in answers]
        return True, mx_records
    except Exception:
        return False, []

def validate_email(email):
    domain = extract_domain(email)
    mx_valid, _ = check_mx_record(domain)
    
    return {
        'email': email,
        'domain': domain,
        'mx_valid': mx_valid
    }

def find_emails_from_website(url, timeout=10):
    try:
        signal.alarm(timeout)
        response = requests.get(url, timeout=timeout)
        signal.alarm(0)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        emails = []
        for element in soup.find_all(['a', 'span']):
            text = element.get_text()
            email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
            if email_match:
                emails.append(email_match.group())
        
        return list(set(emails))  # Remove duplicates
    except TimeoutError:
        print(f"Timeout occurred while fetching {url}")
    except Exception as e:
        print(f"Error fetching emails from {url}: {str(e)}")
    finally:
        signal.alarm(0)
    return []

def find_emails_from_domain(domain, timeout=30):
    base_url = f"https://{domain}"
    
    try:
        signal.alarm(timeout)
        response = requests.get(base_url, timeout=timeout)
        signal.alarm(0)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/'):
                links.append(f"{base_url}{href}")
            elif href.startswith('http') and domain in href:
                links.append(href)
        
        unique_links = list(set(links))
        
        emails = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(find_emails_from_website, link, timeout=10) for link in unique_links[:50]]  # Limit to 50 links
            
            for future in as_completed(futures):
                try:
                    page_emails = future.result(timeout=15)
                    emails.extend(page_emails)
                except Exception as exc:
                    print(f"Error processing future: {exc}")
        
        return list(set(emails))  # Remove duplicates
    except TimeoutError:
        print(f"Timeout occurred while fetching emails from {domain}")
    except Exception as e:
        print(f"Error fetching emails from domain {domain}: {str(e)}")
    finally:
        signal.alarm(0)
    return []

def main():
    domains_to_check = ["swansoftweb.com"]  # List of domains to check
    
    for domain in domains_to_check:
        print(f"\nChecking domain: {domain}")
        
        start_time = time.time()
        emails = find_emails_from_domain(domain, timeout=60)
        elapsed_time = time.time() - start_time
        
        print(f"Fetched emails from {domain} in {elapsed_time:.2f} seconds")
        
        valid_emails = []
        with ThreadPoolExecutor(max_workers=10) as validation_executor:
            futures = [validation_executor.submit(validate_email, email) for email in emails]
            
            for future in as_completed(futures):
                try:
                    result = future.result(timeout=10)
                    if result['mx_valid']:
                        valid_emails.append(result['email'])
                except Exception as exc:
                    print(f"Error validating email: {exc}")
        
        print(f"Found {len(valid_emails)} valid email addresses:")
        for email in valid_emails[:10]:  # Show first 10 valid emails
            print(email)

if __name__ == "__main__":
    main()
