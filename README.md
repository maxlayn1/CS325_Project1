# CS325_Project1
Uses a locally run LLM to evaluate scraped business news headlines as either "positive," "negative," or "neutral."

## Installation (Local LLM Component)
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

## Usage (Local LLM Component)
Copy and paste your headlines into prompts.txt. Each headline should take up a single line. Then run the following command from cloned directory:
```bash
python interface.py
```
Choose which LLM you want to run and press enter. Your LLM responses should now be stored in responses.txt, along with timestamps.

## Usage (Webscrapping Component)
Run the following command to scrape the headlines from the URLS within input_urls.txt:
```bash
python webscraper.py
```
Choose which of the given news sites to scrape the business headlines from. Scraped headlines will be stored within scraped_headlines.txt.

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