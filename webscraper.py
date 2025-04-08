import bs4
import requests
import time

def main():
    urls = read_url_file()
    headlines = scrape_urls(urls)
    store_scraped_headlines(headlines)
        
    
def read_url_file():
    with open('input_urls.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
    return lines
        
def scrape_urls(urls):
    all_headlines = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    for url in urls:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            #print(soup.prettify())
            headlines = soup.find_all('span', class_ ='dfm-title')  
            all_headlines.extend(headlines)  # Add the headlines to the list                               
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return all_headlines

def store_scraped_headlines(headlines):
    file = open('scraped_headlines.txt', 'a')
    file.write(f'-------HEADLINES SCRAPED AT {time.strftime("%H:%M:%S")}------\n')
    for headline in headlines:
        file.write(f'{headline}\n')
            
main()