from flask import Flask
from flask import render_template
import contentscrape

app = Flask(__name__,
            template_folder="templates")

GaillardEvent = contentscrape.Gaillard()
HTDTEvent = contentscrape.HomeTeamDowntown()
HTWAEvent = contentscrape.HomeTeamWA()
MHEvent = contentscrape.MusicHall()
MFEvent = contentscrape.MusicFarm()
PHEvent = contentscrape.PourHouse()
TREvent = contentscrape.TinRoof()
WSEvent = contentscrape.WoolfeStreet()


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html', GaillardEventName=GaillardEvent, HomeTeamDTEventName=HTDTEvent,
                           HomeTeamWAEventName=HTWAEvent, MusicHallEventName=MHEvent, MusicFarmEventName=MFEvent,
                           PourHouseEventName=PHEvent, TinRoofEventName=TREvent, WoolfeStreetEventName=WSEvent)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')
