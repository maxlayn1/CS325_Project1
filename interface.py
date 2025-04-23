import subprocess                                                           #allows python to input terminal commands
import time                                                                 #allows for listing time of LLM response in reponses.txt file
import webscraper

def main():           
    #webscraper.main()                                                       #run webscraper.py to scrape headlines
    LLM_name = choose_LLM()                                                 #user chooses which LLM they want to use
    prompt_list = read_prompt_file()     
    clean_response_list = pass_prompt_to_LLM(prompt_list, LLM_name)         #prompt is passed to LLM and result is stored
    store_LLM_response(clean_response_list)                                 #LLM responses stored in responses.txt
    print('LLM RESPONSES STORED')                                           #indicate to the user that the script is done

def choose_LLM():                                                           #ask whether user wants to use Gemma2-2b or llama3.2
    LLM = input('Choose an LLM: 1. Gemma2-2b   2. llama3.2\n')
    if LLM == '1':
        print('Using Gemma2-2b')
        return 'gemma2:2b'                                                  #user choose gemma2-2b
    elif LLM == '2':
        print('Using llama3.2')
        return 'llama3.2:3b'                                                #user choose llama3.2
    else:
        raise SystemExit(1)                                                 #crash program if unexpected input

def read_prompt_file():                                                     #read prompts.txt, returning all the prompts in a list
    with open('scraped_headlines.txt', 'r') as file:
        lines = file.readlines()
        lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]  # skip empty lines and lines starting with '#'   
        return lines

def pass_prompt_to_LLM(prompt_list, LLM_name):                              #ask LLM to interpret prompt thru user's terminal
    try:
        response_list = []
        for prompt in prompt_list:
            LLM_PROMPT = 'Read the following news headline and determine if it is positive, negative, or neutral. When responding use only one of these three words, and respond with only one word. Do NOT respond further than the one word:'
            command = "ollama run " + LLM_name + " \"" + LLM_PROMPT + prompt + "\"" + "\n"
            result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True) #runs command in terminal
            response_list.append(clean_LLM_response(result.stdout))         #adds response to a list after cleaning it
        return response_list                                                #returns list of LLM's responses
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def clean_LLM_response(unclean_response):                                   #clean LLM's response
    return unclean_response.strip().lower()

def store_LLM_response(clean_response_list):                                #store LLM's responses in responses.txt                 
    file = open('responses.txt', 'a')
    file.write(f'#-------LLM RESPONSE AT {time.strftime("%H:%M:%S")}------\n')
    for response in clean_response_list:
        file.write(f'{response}\n')

main()