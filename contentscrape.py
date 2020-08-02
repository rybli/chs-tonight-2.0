from bs4 import BeautifulSoup as bs
import requests
from datetime import date
import re

# XPATH Libraries
import requests
from urllib.request import urlopen
from lxml import etree
from lxml import html


#  List of URLs for venues
venues = {
    "Gaillard": "https://gaillardcenter.org/buy-tickets",
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





# Pull initial web page and return for use in site specific functions.
def siteScrape(url):
    """

    :param url: [String] Input of website URL.
    :return: [String] Output of website HTML to be parsed.
    """
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"}
    req = requests.get(url, headers=headers)
    tree = html.fromstring(req.content.decode(encoding="utf-8", errors="ignore"))
    return tree # Return tree for xpath parsing.


def Gaillard():
    """

    :return: [String] Output of a single string for either event name or 'No Events'
    """
    # Request site once and store page in variable for local parsing/scraping
    gaillard = siteScrape((venues.get("Gaillard")))
    month = gaillard.xpath('//span[@class="performance-item__date-month"]//text()')
    day = gaillard.xpath('//span[@class="performance-item__date-day"]//text()')
    event = gaillard.xpath('//div[@class="performance-item__title"]//text()')

    for event_month, event_day, event_name in zip(month, day, event):
        print(event_month, event_day, event_name)
        if (event_month, event_day) == date.today().strftime("%b %d").replace(" 0", " "): # compare event date to today's date formatted
            return event_name


Gaillard()


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
# def HomeTeamDowntown():
#     """
#
#     :return: [String] Output of a single string for either event name or 'No Events'
#     """
#     webpage = bs(siteScrape(venues.get("Home Team Downtown")), 'html.parser')
#     eventInfo = webpage.find('div', {"class": "timeline wow fadeIn"})
#     for event in eventInfo.findAll('div', {"class": "row event location-downtown-charleston"}): # Finding all DT events.
#         eventDate = (event.find('div', {"class": "month"}).text, event.find('div', {"class": "year"}).text) # Year is actually the day of month.
#         if eventDate == date.today().strftime("%b  %d").lstrip("0").replace(" 0", " "): # Format today function to match site date for comparison.
#             HTDTeventName = event.attrs.get("data-name")
#             return HTDTeventName
#         else:
#             HTDTeventName = "No Events"
#             return HTDTeventName
#
#
# HomeTeamDowntown()

# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
# def HomeTeamWA():
#     """
#
#     :return: [String] Output of a single string for either event name or 'No Events'
#     """
#     webpage = bs(siteScrape(venues.get("Home Team West Ashley")), 'html.parser')
#     eventInfo = webpage.find('div', {"class": "timeline wow fadeIn"})
#     for event in eventInfo.findAll('div', {"class": "row event location-west-ashley"}): # Finding all WA events.
#         eventDate = (event.find('div', {"class": "month"}).text,
#                      event.find('div', {"class": "year"}).text)  # Year is actually the day of month.
#         if eventDate == date.today().strftime("%b  %d").lstrip("0").replace(" 0", " "):  # Format today function to match site date for comparison.
#             HTWAeventName = event.attrs.get("data-name")
#             return HTWAeventName
#         else:
#             HTWAeventName = "No Events"
#             return HTWAeventName
#
# HomeTeamWA()

def MusicFarm():
    """

    :return: [String] Out of a single string for either event name of 'No Events'
    Have access to event time as well for future use.
    """
    # date = siteScrape(venues.get("Music Farm")).xpath('//div[@class="mb-0 eventMonth fontMontserratBold singleEventDate font-weight-bold text-uppercase font0by875"]//text()')
    # event =
    # time = site
    # print(event_date)
#     def MusicFarm():
#         webpage = bs(siteScrape(venues.get("Music Farm")), "html.parser")
#         eventInfo = webpage.find('div', {"class": "rhino-widget-list"})
#         for eventDate, eventName, eventTime in zip(eventInfo.findAll('div', {"class": "eventDateList"}),
#                                                    eventInfo.findAll('div', {"class": "col-12 px-0 eventTitleDiv"}),
#                                                    eventInfo.findAll('div', {
#                                                        "class": "d-block eventsColor eventDoorStartDate"})):
#             if eventDate.text.strip() == date.today().strftime("%b %d"):
#                 MFeventName = eventName.text
#                 return MFeventName
#             else:
#                 MFeventName = "No Events"
#                 return MFeventName
#
# MusicFarm()
#
# def MusicHall():
#     webpage = bs(siteScrape(venues.get("Music Hall")), "html.parser")
#     eventInfo = webpage.find('div', {"class": "tribe-events-loop"})
#     for event in eventInfo.findAll('article', {"class": "cmh-event-wrapper"}):
#         eventDate = re.findall('\d+', event.find('time', {"class": "dates"}).text.replace('.', ' '))
#         if (eventDate[0], eventDate[1]) == date.today().strftime("%m %d").lstrip("0").replace(" 0", " "):
#             eventName = event.find('h2').text
#             return eventName
#
# MusicHall()

# # TODO Need to get start time of event
# # TODO Need to get event sub title
# def PourHouse():
#     webpage = bs(siteScrape(venues.get("Pour House")), "html.parser")
#     eventInfo = webpage.find('main', {"class": "site-main"})
#     for event in eventInfo.findAll('header', {"class": "show-header"}):
#         # print(event.find('table', {"class": "show-details"}))
#         event_date = re.sub(r'(?<=[0-9])(?:st|nd|rd|th)', '', event.find('p', {"class": "show-day"}).text.replace(',', '')) # Remove ordinal indicators and strip commas for date comparison
#         if event_date == date.today().strftime("%A %B %d %Y"): # Compare to formatted current date.
#             eventName = event.find('h3').text # Return the name of event
#             return eventName
#
# PourHouse()

# def RoyalAmerican():
#     pass

# def Sparrow():
#     pass

# def Theatre99():
#     pass

# def TinRoof():
#     pass

# def WindJammer():
#     pass

# def WoolfeStreet():
#     pass