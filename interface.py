import subprocess                                                       #allows python to input terminal commands
import time                                                             #for listing time of LLM response in reponses txt file

def main():           
    LLM_name = choose_LLM()
    prompt_list = read_prompt_file()
    clean_response_list = pass_prompt_to_LLM(prompt_list, LLM_name)
    store_LLM_response(clean_response_list)
    print('LLM RESPONSES STORED')

def choose_LLM():                                                       #ask user whether they want to use Gemma2-2b, or Phi3
    LLM = input('Choose an LLM: 1. Gemma2-2b   2. Phi3\n')
    if LLM == '1':
        print('Using Gemma2-2b')
        return 'gemma2:2b'
    elif LLM == '2':
        print('Using Phi3')
        return 'phi3:latest'
    else:
        raise SystemExit(1)                                             #crash program if unexpected input for now

def read_prompt_file():                                                 #read text file containing prompts, returning all the prompts in a list
    with open('prompts.txt', 'r') as file:
        lines = file.readlines()
        lines = [empty for empty in lines if empty.strip()]             #trims empty lines from txt prompt file
    return lines

def pass_prompt_to_LLM(prompt_list, LLM_name):                          #ask LLM to interpret prompt thru user's terminal
    try:
        response_list = []
        for prompt in prompt_list:
            LLM_PROMPT = 'Read the following news headline and determine if it is positive, negative, or neutral. When responding use only these three words, and respond with only one word.'
            command = "ollama run " + LLM_name + " \"" + LLM_PROMPT + prompt + "\"" + "\n"
            result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
            response_list.append(read_LLM_response(result.stdout))      #adds response to a list after cleaning it
        return response_list
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def read_LLM_response(unclean_response):                                #interpret LLM's response
    return unclean_response.strip().lower()

def store_LLM_response(clean_response_list):                                 #store LLM's response in seperate txt file                      
    file = open('responses.txt', 'w')
    file.write(f'-------LLM RESPONSE AT {time.strftime("%H:%M:%S")}------\n')
    for response in clean_response_list:
        file.write(f'{response}\n')

main()