# Plik Dockerfile dla aplikacji serwera HTTP

# Dockerfile for HTTP server application

# Base image - Python 3.10
FROM python:3.10

# Add metadata
LABEL author="Ivan Zachatka"

# Set environment variable
ENV PORT=8000

# Copy application code to the image
COPY server.py /app/server.py

# Set working directory
WORKDIR /app

# Run the server
CMD python server.py

# Specify the listening port
EXPOSE $PORT


