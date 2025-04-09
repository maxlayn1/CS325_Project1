import bs4
import requests
import time

def main():
    urls = read_url_file()
    site_to_scrape = choose_site_to_scrape()
    headlines = scrape_urls(urls, site_to_scrape)
    store_scraped_headlines(headlines)
    
def read_url_file():
    with open('input_urls.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
    return lines
        
def scrape_urls(urls, site_to_scrape):
    all_headlines = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    if (site_to_scrape == '1'):
        try:
            response = requests.get(urls[0], headers=headers)
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find_all('span', class_ = 'dfm-title')  
            all_headlines.extend([headline.text.strip() for headline in headlines[6:]])  # Add the headlines to the list                               
        except Exception as e:
            print(f"Error scraping {urls[0]}: {e}")
        return all_headlines
    elif (site_to_scrape == '2'):
        try:
            response = requests.get(urls[1], headers=headers)
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            
            #print(soup.prettify())
            h3s = soup.find_all('h3', class_='story-headline')
            for h3 in h3s:
                    anchor = h3.find('a')
                    if anchor:
                            all_headlines.append(anchor.text.strip())
        except Exception as e:
            print(f"Error scraping {urls[1]}: {e}")
        return all_headlines
    else:
        print('Invalid site selected')
        exit(1)


def store_scraped_headlines(headlines):
    file = open('scraped_headlines.txt', 'a')
    file.write(f'-------HEADLINES SCRAPED AT {time.strftime("%H:%M:%S")}------\n')
    for headline in headlines:
        file.write(f'{headline}\n')
        
def choose_site_to_scrape():
    website_to_scrape = input('Choose a website to scrape: 1. Chicago Tribune   2. U.S. News\n')
    return website_to_scrape
            
main()