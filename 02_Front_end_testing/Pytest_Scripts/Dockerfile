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

# Add Google Chrome repository and install stable version
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

# Download and install chromedriver
RUN CHROMEDRIVER_URL="https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chromedriver-linux64.zip" \
    && wget -q $CHROMEDRIVER_URL -O /tmp/chromedriver-linux64.zip \
    && unzip /tmp/chromedriver-linux64.zip -d /usr/local/bin \
    && rm /tmp/chromedriver-linux64.zip

# Set working directory to /Portfolio_front_end
WORKDIR /Portfolio_front_end

# Add Allure Reports directory to the working directory
VOLUME /AllureReports/allure-results

# Copy requirements.txt file to the working directory
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Set the default command to run pytest in headless mode with the tests directory
CMD ["pytest", "--headless", "--alluredir=./AllureReports/allure-results", "tests"]


# For watch allure reports use commands:
# docker cp $(docker ps -a -q | head -1):/Portfolio_front_end/AllureReports/allure-results .
# allure serve AllureReports/allure-results
