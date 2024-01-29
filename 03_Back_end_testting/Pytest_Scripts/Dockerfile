# Use python 3.11 slim base image
FROM python:3.11-slim

# Set labels for the GitHub Actions workflow
LABEL "com.github.actions.name"="Portfolio"
LABEL "creator"="Andrew Usachev"

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory to /Portfolio_front_end
WORKDIR /Portfolio_API

# Add Allure Reports directory to the working directory
VOLUME /AllureReports/allure-results

# Copy requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Set the default command to run pytest with the tests directory
CMD pytest -s -v --alluredir=./AllureReports/allure-results tests/


# For watch allure reports use commands:
# docker cp $(docker ps -a -q | head -1):/Portfolio_API/AllureReports/allure-results .
# allure serve AllureReports/allure-results