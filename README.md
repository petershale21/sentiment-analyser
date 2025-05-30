# Sentiment Analyzer API

A simple Dockerized sentiment analyser using Flask and TextBlob.

## How to Use

1. Build the Docker image:
   ```bash
   docker build -t sentiment-analyser .

2. Run the container
   ```bash
   docker run -p 5000:5000 sentiment-analyser

3. Access the API
   curl http://localhost:5000/analyse/I%20love%20this%20product
