# CS325_Project1
Uses a locally run LLM to evaluate news headlines as either "positive," "negative," or "neutral."

## Installation
Run the following commands on Linux/WSL
1. Installs Ollama API / terminal CLI
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. Installs llama3.2 (3 billion parameter) local LLM (Meta)
```bash
ollama pull llama3.2:3b
```
3. Installs Gemma2 (2 billion parameter) local LLM (Google)
```bash
ollama pull gemma2:2b
```
## Usage
Copy and paste your headlines into prompts.txt. Each headline should take up a single line. Then run the following command from cloned directory:
```bash
python interface.py
```
Choose which LLM you want to run and press enter. Your LLM responses should now be stored in responses.txt, along with timestamps.

## Other notes
If the curl command does not work for you, install curl using:
```bash
sudo apt install curl
```
Then verify installation using 
```bash
curl --version
```
Additionally you can verify Ollama CLI installation using:
```bash
ollama --version
```