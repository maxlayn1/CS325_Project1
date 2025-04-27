FROM debian:bullseye-slim

# Install python, pip, curl
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    vim-tiny \
    gnupg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN chmod +x /usr/local/bin/ollama

WORKDIR /app

COPY . .

# Environment variables to make Ollama bind to the new port (11500)
ENV OLLAMA_HOST=0.0.0.0
ENV OLLAMA_PORT=11500

# Install pip dependencies (pytest, bs4, some other small stuff)
RUN pip install --no-cache-dir -r requirements.txt || true

# Expose the new Ollama port (11500)
EXPOSE 11500

# Start Ollama, pull models, run interface.py, and wait
CMD ["sh", "-c", "ollama serve & sleep 10 && ollama pull llama3.2:3b && ollama pull gemma2:2b && wait"]