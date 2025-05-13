from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_youtube_by_hashtag(hashtag):
    query = f"%23{hashtag}"
    url = f"https://www.youtube.com/results?search_query={query}&sp=CAMSBAgEEAE%253D"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options = options)
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    results = []
    for video in soup.select("ytd-video-renderer"):
        title_tag = video.select_one("#video-title")
        channel_tag = video.select_one("ytd-channel-name")
        if title_tag and channel_tag:
            title = title_tag.get("title")
            link = "https://www.youtube.com" + title_tag.get("href")
            channel = channel_tag.text.strip()
            results.append({
                "title": title,
                "url": link,
                "channel": channel,
                "hashtag": hashtag,
            })

            if len(results) >= 10:
                break
        
    return results
