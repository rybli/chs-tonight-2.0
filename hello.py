from flask import Flask
from flask import render_template
import contentscrape
from contentscrape import dt, start, end
from datetime import datetime, timedelta, date
# Scheduling libraries
# import time
# import atexit
# from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__,
            template_folder="templates",
            static_folder="static")

events = {
        "Gaillard": contentscrape.Gaillard(),
        "Home Team Downtown": contentscrape.HomeTeamDowntown(),
        "Home Team West Ashley": contentscrape.HomeTeamWA(),
        "Music Farm Charleston": contentscrape.MusicFarm(),
        "Music Hall": contentscrape.MusicHall(),
        "Pour House": contentscrape.PourHouse(),
        "Royal American": contentscrape.RoyalAmerican(),
        "Sparrow": contentscrape.Sparrow(),
        "Theatre 99": contentscrape.Theatre99(),
        "Tin Roof": contentscrape.TinRoof(),
        "Wind Jammer": contentscrape.WindJammer(),
        "Woolfe Street": contentscrape.WoolfeStreet()
    }


# def create_events():
#     events = {
#         "Gaillard": contentscrape.Gaillard(),
#         "Home Team Downtown": contentscrape.HomeTeamDowntown(),
#         "Home Team West Ashley": contentscrape.HomeTeamWA(),
#         "Music Farm Charleston": contentscrape.MusicFarm(),
#         "Music Hall": contentscrape.MusicHall(),
#         "Pour House": contentscrape.PourHouse(),
#         "Royal American": contentscrape.RoyalAmerican(),
#         "Sparrow": contentscrape.Sparrow(),
#         "Theatre 99": contentscrape.Theatre99(),
#         "Tin Roof": contentscrape.TinRoof(),
#         "Wind Jammer": contentscrape.WindJammer(),
#         "Woolfe Street": contentscrape.WoolfeStreet()
#     }
#     return events
#
#
# scheduler = BackgroundScheduler()
# scheduler.add_job(func=create_events, trigger='interval', seconds=30)
# scheduler.start()


# Get today's date
date_today = date.today().strftime("%A, %B %#d, %Y")
# Get list of days of the week
dates = [dt.strftime("%A, %B %#d, %Y") for dt in contentscrape.daterange(start, end)]


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def hello_world():
    return render_template('home.html', date_today=date_today,
                           date_week=dates[0] + " - " + dates[-1],
                           results=events)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', venues=contentscrape.venuesAbout)


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['TESTING'] = True

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)