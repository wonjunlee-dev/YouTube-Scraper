from flask import Flask, request, jsonify, render_template
from db import init_db, get_session
from models import YoutubeVideo
from scraper import scrape_youtube_by_hashtag
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/videos", methods = ["GET"])
def get_videos():
    hashtag = request.args.get('hashtag')
    if not hashtag:
        return jsonify({"error": "Missing hashtag parameter"}), 400
    
    session = get_session()

    latest = session.query(YoutubeVideo)\
        .filter(YoutubeVideo.hashtag == hashtag)\
        .order_by(YoutubeVideo.scraped_at.desc())\
        .first()

    if not latest:
        session.close()
        return jsonify({"error": "No data found. Please POST to /crawl."}), 404

    now = datetime.now(pytz.utc)
    if (now - latest.scraped_at) > timedelta(hours = 5):
        session.close()
        return jsonify({"error": "Data too old. Please POST to /crawl."}), 410

    videos = session.query(YoutubeVideo)\
        .filter(YoutubeVideo.hashtag == hashtag)\
        .order_by(YoutubeVideo.scraped_at.desc())\
        .limit(10).all()
    
    result = []
    for vid in videos:
        result.append({
            "title": vid.title,
            "url": vid.url,
            "channel": vid.channel,
            "scraped_at": vid.scraped_at.isoformat()
        })
    
    session.close()
    return jsonify(result)

@app.route("/crawl", methods = ["POST"])
def crawl_videos():
    hashtag = request.form.get("hashtag")
    if not hashtag:
        return jsonify({"error": "Missing hashtag parameter"}), 400
    
    session = get_session()

    session.query(YoutubeVideo).filter(YoutubeVideo.hashtag == hashtag).delete()
    session.commit()
    
    videos = scrape_youtube_by_hashtag(hashtag)
    for vid in videos:
        video = YoutubeVideo(
            hashtag = vid['hashtag'],
            title = vid['title'],
            url = vid['url'],
            channel = vid['channel']
        )
        session.add(video)
    
    session.commit()
    session.close()
    return jsonify(videos)

load_dotenv()
if __name__ == "__main__":
    init_db()
    app.run(
        debug = True,
        host = "0.0.0.0",
        port = int(os.getenv("PORT", 3000)))
