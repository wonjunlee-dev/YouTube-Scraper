from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
import pytz

Base = declarative_base()

def utc_now():
    return datetime.now(pytz.utc)

class YoutubeVideo(Base):
    __tablename__ = 'youtube_videos'

    id = Column(Integer, primary_key=True)
    hashtag = Column(String)
    title = Column(String)
    url = Column(String)
    channel = Column(String)
    views = Column(Integer, nullable=True)
    scraped_at = Column(DateTime(timezone = True), default = utc_now)
