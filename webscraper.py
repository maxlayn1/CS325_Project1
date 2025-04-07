import bs4
import requests

def main():
    urls = read_url_file()
    headlines = scrape_urls(urls)
    for headline in headlines:
        print(headline.text)
    
def read_url_file():
    with open('input_urls.txt', 'r') as file:
        lines = file.readlines()
        lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]  # skip empty lines and lines starting with '#'                                                            #excludes comment at the top of prompts.txt from evaluation
        return lines
        
def scrape_urls(urls):
    for url in urls:
        try:
            response = requests.get(url)
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all('h2')                                 
            return headlines
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            
main()