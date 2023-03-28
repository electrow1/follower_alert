from apscheduler.schedulers.background import BackgroundScheduler
from helpers import get_all_updates
from flask import Flask


app = Flask(__name__)

no_minutes=2
scheduler = BackgroundScheduler()
scheduler.add_job(func=get_all_updates, trigger="interval", seconds=60*no_minutes)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=False)
