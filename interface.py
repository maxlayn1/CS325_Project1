#idk yet // dont forget to add yaml file too

#read from text file 3 prompts
#pass these 3 prompts to model
#copy answers and store in another txt file

def main(): #call functions from here 
    print('main')
    read_prompt_file()

def choose_LLM(): #ask user whether they want to use Gemma2-2b, or Phi3
    LLM = input('Choose and LLM: 1. Gemma2-2b   2. Phi3')
    if LLM == '1':
        print('Using Gemma2-2b')
    elif LLM == '2':
        print('Using Phi3')
    else:
        print('Error, invalid input')
        exit

def read_prompt_file(): #read text file containing prompts, adding all the lines into a list
    with open('prompts.txt', 'r') as file:
        lines = file.readlines()
        lines = [empty for empty in lines if empty.strip()] #trims empty lines from txt prompt file
    for line in lines:
        print(line)

def pass_prompt_to_LLM(): #ask LLM to interpret prompt sufficiently
    print('passing prompt to LLM')

def read_LLM_response(): #interpret LLM's response
    print('reading response from LLM')

def store_LLM_response(): #store LLM's response in seperate txt file
    print('storing LLM response in txt file')

main()