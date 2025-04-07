import bs4
import requests

def main():
    urls = read_url_file()
    
def read_url_file():
    with open('input_urls.txt', 'r') as file:
        lines = file.readlines()
        lines = [empty for empty in lines if empty.strip()]                 #trims empty lines from prompts.txt
        lines.pop()                                                         #excludes comment at the top of prompts.txt from evaluation
        return lines
        
def scrape_urls(urls):
    for url in urls:
        try:
            response = requests.get(url)
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all('h2')                                 
            for headline in headlines:
                print(headline.text)
        except Exception as e:
            print(f"Error scraping {url}: {e}")