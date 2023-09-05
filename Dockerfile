# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Firefox and other required dependencies
RUN apt-get update && apt-get install -y firefox-esr

# Copy the script and requirements file into the container
COPY Groups/Qilin_Blog.py /app/Qilin_Blog.py
COPY Groups/sample2.py /app/sample2.py
COPY requirements.txt /app/requirements.txt

# Install required Python dependencies
RUN pip install -r requirements.txt

# Continue with the rest of your Dockerfile configuration...