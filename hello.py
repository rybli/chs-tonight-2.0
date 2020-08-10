from flask import Flask
from flask import render_template
import contentscrape
from datetime import date

app = Flask(__name__,
            template_folder="templates",
            static_folder="static")

events = {
    "Gaillard": contentscrape.Gaillard(),
    "Home Team Downtown": contentscrape.HomeTeamDowntown(),
    "Home Team West Ashley": contentscrape.HomeTeamWA(),
    "Music Farm": contentscrape.MusicFarm(),
    "Music Hall": contentscrape.MusicHall(),
    "Pour House": contentscrape.PourHouse(),
    "Royal American": contentscrape.RoyalAmerican(),
    "Sparrow": contentscrape.Sparrow(),
    "Theatre 99": contentscrape.Theatre99(),
    "Tin Roof": contentscrape.TinRoof(),
    "Wind Jammer": contentscrape.WindJammer(),
    "Woolfe Street": contentscrape.WoolfeStreet()
}

date_today = date.today().strftime("%A, %B %#d, %Y")

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html', date_today=date_today, results=events)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TESTING'] = True