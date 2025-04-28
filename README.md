# CS325_Project1
Utilizes BeautifulSoup4 to scrape news headlines from the business sections of pre-determined sites. Then uses a locally run LLM to evaluate the scraped news headlines as either "positive," "negative," or "neutral." Finally, outputs this sentiment analysis to a text file.

## Installation
Run the following commands on Linux/WSL
1. Installs Ollama API / terminal CLI
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. Verify Ollama CLI installation
```bash
ollama --version
```
3. Installs llama3.2 (3 billion parameter) local LLM (Meta)
```bash
ollama pull llama3.2:3b
```
4. Installs Gemma2 (2 billion parameter) local LLM (Google)
```bash
ollama pull gemma2:2b
```
--Note that all other installation requirements to run are listed in requirements.yaml

## Usage
Ensure that input_urls.txt contains links to the Chicago Tribune business section and the US News business section. Then run the following command from cloned directory:
```bash
python interface.py
```
Choose which news site you would like to scrape the headlines from. Then choose which LLM you want to run. The choosen LLM will take some time to respond, and then responses should be stored in 'responses.txt,' along with timestamps.

## Other notes
-If the curl command does not work for you, install curl using:
```bash
sudo apt install curl
```
Then verify installation using:
```bash
curl --version
```

-webscraper.py would need to be augmented to scrape URLs other than those provided.

-the '#' character at the top of text files keeps the line from being read as a prompt by the AI (do not remove!)

-scraped_headlines.txt can be viewed to ensure correct headline scraping. The file is overwritten with new headlines each time 'interface.py' is run.

## Docker container version (ADVANCED USERS!)
Container uses Debian Bullseye-slim OS, and already has both LLMs installed on it.
```bash
docker pull maxlayn1/headline_sentiment_app
```