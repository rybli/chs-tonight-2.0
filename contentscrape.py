from bs4 import BeautifulSoup as bs
import requests
from datetime import date
import re


#  List of URLs for venues
venues = {
    "Gaillard": "https://gaillardcenter.org/buy-tickets/",
    "Home Team Downtown": "https://hometeambbq.com/happenings/",
    "Home Team West Ashley": "https://hometeambbq.com/happenings/",
    "Music Farm": "https://music-farm.com/events/?tribe_bar_rhp_venue=3902",
    "Music Hall": "https://www.charlestonmusichall.com/shows/",
    "Pour House": "https://charlestonpourhouse.com/",
    "Royal American": "https://www.theroyalamerican.com/schedule",
    "Sparrow": "https://www.facebook.com/pg/thesparrowparkcircle/events/",
    "Theatre 99": "https://theatre99.com/schedule/action~posterboard/",
    "Tin Roof": "https://tockify.com/api/ngevent?max=12&calname=tinroofschedule",
    "Wind Jammer": "https://the-windjammer.com/events/",
    "Woolfe Street": "https://woolfestreetplayhouse.com/shows/"
}

#  Pull initial webpage and return for use in site specific functions.
def siteScrape(url):
    """

    :param url: [String] Input of website URL.
    :return: [String] Output of website HTML to be parsed.
    """
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    return str(soup)


def Gaillard():
    """

    :return: [String] Output of a single string for either event name or 'No Events'
    """
    webpage = bs(siteScrape(venues.get("Gaillard")), 'html.parser')
    eventInfo = webpage.findAll('div', {"class": "col-sm-6 bbi-event-info"})
    for event in eventInfo: # Loop through all events
        eventDate = event.find('h5').text # Pull date
        # Check if an event is happening today. If event today, set event variables.
        if eventDate == date.today().strftime("%b  %d").lstrip("0").replace(" 0", " "): # Format today function to match site date for comparison.
            GaillardEventName = event.find('h3').text
            return GaillardEventName
        else:
            GaillardEventName = "No Events"
            return GaillardEventName


Gaillard()

def HomeTeamDowntown():
    """

    :return: [String] Output of a single string for either event name or 'No Events'
    """
    webpage = bs(siteScrape(venues.get("Home Team Downtown")), 'html.parser')
    eventInfo = webpage.find('div', {"class": "timeline wow fadeIn"})
    for event in eventInfo.findAll('div', {"class": "row event location-downtown-charleston"}): # Finding all DT events.
        eventDate = (event.find('div', {"class": "month"}).text, event.find('div', {"class": "year"}).text) # Year is actually the day of month.
        if eventDate == date.today().strftime("%b  %d").lstrip("0").replace(" 0", " "): # Format today function to match site date for comparison.
            HTDTeventName = event.attrs.get("data-name")
            return HTDTeventName
        else:
            HTDTeventName = "No Events"
            return HTDTeventName


HomeTeamDowntown()

def HomeTeamWA():
    """

    :return: [String] Output of a single string for either event name or 'No Events'
    """
    webpage = bs(siteScrape(venues.get("Home Team West Ashley")), 'html.parser')
    eventInfo = webpage.find('div', {"class": "timeline wow fadeIn"})
    for event in eventInfo.findAll('div', {"class": "row event location-west-ashley"}): # Finding all WA events.
        eventDate = (event.find('div', {"class": "month"}).text,
                     event.find('div', {"class": "year"}).text)  # Year is actually the day of month.
        if eventDate == date.today().strftime("%b  %d").lstrip("0").replace(" 0", " "):  # Format today function to match site date for comparison.
            HTWAeventName = event.attrs.get("data-name")
            return HTWAeventName
        else:
            HTWAeventName = "No Events"
            return HTWAeventName

HomeTeamWA()

def MusicFarm():
    """

    :return: [String] Out of a single string for either event name of 'No Events'
    Have access to event time as well for future use.
    """
    def MusicFarm():
        webpage = bs(open("MusicFarm.html", "r"), "html.parser")
        eventInfo = webpage.find('div', {"class": "rhino-widget-list"})
        for eventDate, eventName, eventTime in zip(eventInfo.findAll('div', {"class": "eventDateList"}),
                                                   eventInfo.findAll('div', {"class": "col-12 px-0 eventTitleDiv"}),
                                                   eventInfo.findAll('div', {
                                                       "class": "d-block eventsColor eventDoorStartDate"})):
            if eventDate.text.strip() == date.today().strftime("%b %d"):
                MFeventName = eventName.text
                return MFeventName
            else:
                MFeventName = "No Events"
                return MFeventName

MusicFarm()

def MusicHall():
    webpage = bs(siteScrape(venues.get("Music Hall")), "html.parser")
    eventInfo = webpage.find('div', {"class": "tribe-events-loop"})
    for event in eventInfo.findAll('article', {"class": "cmh-event-wrapper"}):
        eventDate = re.findall('\d+', event.find('time', {"class": "dates"}).text.replace('.', ' '))
        if (eventDate[0], eventDate[1]) == date.today().strftime("%m %d").lstrip("0").replace(" 0", " "):
            eventName = event.find('h2').text
            return eventName

MusicHall()

def PourHouse():
    pass

def RoyalAmerican():
    pass

def Sparrow():
    pass

def Theatre99():
    pass

def TinRoof():
    pass

def WindJammer():
    pass

def WoolfeStreet():
    pass