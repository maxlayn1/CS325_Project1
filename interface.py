import subprocess                                                                   #allows python to input terminal commands
import time                                                                         #allows for listing time of LLM response in reponses.txt file
import webscraper
from typing import Protocol

class LLM(Protocol):
    def query(self):
        pass
    def respond(self):
        pass
    
class FileHandler(Protocol):
    def read(self):
        pass
    def write(self):
        pass
    
class HeadlineLLM:
    def query(self, prompt_list, LLM_name):
        try:
            response_list = []
            for prompt in prompt_list:
                LLM_PROMPT = 'Read the following news headline and determine if it is positive, negative, or neutral. When responding use only one of these three words, and respond with only one word. Do NOT respond further than the one word:'
                command = "ollama run " + LLM_name + " \"" + LLM_PROMPT + prompt + "\"" + "\n"
                result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True) #runs command in terminal
                response_list.append(result.stdout)                                         #adds response to a list
            return response_list                                                        #returns list of LLM's responses
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"
    def respond (self, clean_response_list):
        file = open('responses.txt', 'a')
        file.write(f'#-------LLM RESPONSE AT {time.strftime("%H:%M:%S")}------\n')
        for response in clean_response_list:
            file.write(f'{response}\n')
    def clean_response(self, unclean_response_list):
        return [response.strip().lower() for response in unclean_response_list]
    def choose_LLM(self):
        LLM = input('Choose an LLM: 1. Gemma2-2b   2. llama3.2\n')
        if LLM == '1':
            print('Using Gemma2-2b')
            return 'gemma2:2b'                                                          #user choose gemma2-2b
        elif LLM == '2':
            print('Using llama3.2')
            return 'llama3.2:3b'                                                        #user choose llama3.2
        else:
            raise SystemExit(1)                                                         #crash program if unexpected input

class HeadlineResponseHandler:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            return lines
    def write(self, clean_response_list):
        file = open('responses.txt', 'a')
        file.write(f'#-------LLM RESPONSE AT {time.strftime("%H:%M:%S")}------\n')
        for response in clean_response_list:
            file.write(f'{response}\n')
    def clean(self, lines):
        lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]  # skip empty lines and lines starting with '#'   
        return lines

def clear_scraped_headlines():
    file = open('scraped_headlines.txt', 'w')
    file.write('#-----THIS FILE SHOULD CONTAIN HEADLINES SCRAPED BY BS4-----\n\n')

def main():           
    clear_scraped_headlines()
    
    url_handler: webscraper.FileHandler = webscraper.URLHeadlineHandler()
    scraper: webscraper.Scraper = webscraper.HeadlineScraper()
    
    urls = url_handler.read()
    clean_urls = url_handler.clean(urls)
    site_to_scrape = scraper.choose_site_to_scrape()
    soup = scraper.connect_to_site(site_to_scrape, clean_urls)
    headlines = scraper.scrape(site_to_scrape, soup)
    url_handler.write(headlines)
    
    local_LLM: LLM = HeadlineLLM()
    headline_handler: FileHandler = HeadlineResponseHandler('scraped_headlines.txt')
    
    prompt_list = headline_handler.read()     
    clean_prompt_list = headline_handler.clean(prompt_list)
    
    LLM_name = local_LLM.choose_LLM()                                                   #user chooses which LLM they want to use
    response_list = local_LLM.query(clean_prompt_list, LLM_name)
    clean_response_list = local_LLM.clean_response(response_list)
    local_LLM.respond(clean_response_list)
    print('LLM RESPONSES STORED')                                                       #indicate to the user that the script is done

main()