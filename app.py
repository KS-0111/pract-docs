import feedparser
import os
from flask import Flask, render_template

app = Flask(__name__)
FEED_URL = "https://hnrss.org/frontpage"

@app.route("/")
def fetch_feed():
    # Added agent to prevent 403 Forbidden errors
    feed = feedparser.parse(FEED_URL, agent='Mozilla/5.0')
    print(f"CRON CHECK: Fetched {len(feed.entries)} stories.")
    return render_template("index.html", entries=feed.entries[:10])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
