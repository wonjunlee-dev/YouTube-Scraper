# YouTube-Scraper

A Flask web application that scrapes and displays top 10 YouTube videos for a given hashtag using Selenium, and BeautifulSoup.

[🔗 Live Demo](https://youtube-scraper-production.up.railway.app)

📸 Preview
<p float="left">
  <img src="https://github.com/user-attachments/assets/012cc74c-0e93-4079-a8b3-0f82f3b54ade" width="45%" />
  <img src="https://github.com/user-attachments/assets/829f23a9-030e-4669-8d3c-ca10c1bb5d84" width="45%" />
</p>


## 🔍 Target & Purpose

- **Target**: YouTube search results page for a given hashtag

- **Purpose**: To help users quickly discover trending or timely YouTube videos related to a specific hashtag.


## 🚀 Features

- User inputs a hashtag to search relevant YouTube videos
- Top 10 videos sorted by upload date and view count
- Uses **Selenium** and **BeautifulSoup** to handle JavaScript-rendered pages
- Stores video metadata (title, channel, etc.) in **PostgreSQL** via SQLAlchemy
- **Automatically checks data freshness** - serves cached data if under 5 hours old, otherwise re-crawls
- User-friendly UI built with **HTML**, **CSS**, and **JavaScript**


## 🛠 Tech Stack

- **Backend**: Flask, Selenium, BeautifulSoup
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL, SQLAlchemy
- **Deployment**: Docker, Railway
- **Version Control**: GitHub


## 💻 How to Run Locally
1. Clone the repository

    Clone the project source code to your local environment.
   ```bash
    git clone <Your Repository URL>
    cd <Your Repository Directory>
   ```

2. Install Python dependencies

    All dependencies listed in the `requirements.txt` file will be automatically installed.
   ```bash
    pip install -r requirements.txt
    ```

3. Install ChromeDriver

    - Download the ChromeDriver that matches your version of the Chrome browser from the [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) page.
    - After downloading, add the ChromeDriver executable to your system's PATH.

4. Run the Flask app

    Once the application starts, open your browser and go to the URL printed in the console to verify it is working.
   ```bash
    python app.py
    ```
