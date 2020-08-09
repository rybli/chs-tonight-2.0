from datetime import date
from datetime import datetime
import requests
from lxml import html
import json
import re


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
    tree = html.fromstring(req.content)
    return tree  # Return tree for xpath parsing.


def Gaillard():
    """

    :return: [String] Output of a single string for either event name or 'No Events'
    """
    # Request site once and store page in variable for local parsing/scraping
    gaillard = siteScrape((venues.get("Gaillard")))
    month = gaillard.xpath('//span[@class="performance-item__date-month"]//text()')
    day = gaillard.xpath('//span[@class="performance-item__date-day"]//text()')
    event = gaillard.xpath('//div[@class="performance-item__title"]//text()')
    time = gaillard.xpath('//div[@class="text-accent performance-item__time"]//text()')

    for event_month, event_day, event_name, event_time in zip(month, day, event, time):
        print(event_month, event_day, event_name)
        if (event_month, event_day) == date.today().strftime("%b %d").replace(" 0", " "): # compare event date to today's date formatted
            return event_name


# Gaillard()


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


def MusicHall():
    """

    :return: [String] Event name
    """
    musichall = siteScrape(venues.get("Music Hall"))
    edate = musichall.xpath('//time[@class="dates"]')
    event = musichall.xpath('//section[@class="cmh-event-content"]/a/h2//text()')
    time = musichall.xpath('//section[@class="cmh-event-content"]/p//text()')

    for event_date, event_name, event_time in zip(edate, event, time):
        # Compare scraped date (e.g. SUN8.16) to today's date.
        # Format today to match scraped date. Windows localized with # to get rid of zero padding.
        if (event_date.text_content()) == date.today().strftime("%a%#m.%#d").upper():
            return event_name

# MusicHall()


# TODO Need to get start time of event
# TODO Need to get event sub title
def PourHouse():
    pourhouse = siteScrape(venues.get("Pour House"))
    date = pourhouse.xpath('//p[@class="show-day"]//text()')
    event = pourhouse.xpath('//header[@class="show-header"]//h3[1]//text()')
    # Includes cover, doors time, show time, and some genre.
    # cover = pourhouse.xpath('//table[@class="show-details"]//tr[1]//th//following-sibling::td//text()')
    for item in event:
        print(item)

    print(event)

# PourHouse()


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
def RoyalAmerican():
    pass


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
def Sparrow():
    pass

# Sparrow()


def Theatre99():
    """

    :return: [String] Event name
    """
    theatre99 = siteScrape(venues.get("Theatre 99"))
    date_month = theatre99.xpath('//div[@class="ai1ec-month"]//text()')
    date_day = theatre99.xpath('//div[@class="ai1ec-day"]//text()')
    date_weekday = theatre99.xpath('//div[@class="ai1ec-weekday"]//text()')
    event = theatre99.xpath('//div[@class="ai1ec-event-title"]/div/a//text()')
    time = theatre99.xpath('//div[@class="ai1ec-posterboard-time"]//text()')

    # Create combined date for comparison.
    date = []
    for month, day, weekday in zip(date_month, date_day, date_weekday):
        combined_date = month + day + weekday
        date.append(combined_date)

    for d, e, t in zip(date, event, time):
        print(d)
        if d == date.today().strftime("%b%#d%a"):
            return e


# Theatre99()


def TinRoof():
    """

    :return: [String] Event name with formatted start time.
    """
    tinroof = requests.get(venues.get("Tin Roof"))
    tinroof_json = tinroof.json()
    for event in tinroof_json['events']:
        # Compare event time to today. If event today, return event name.
        if datetime.utcfromtimestamp(event['when']['start']['millis']/1000).strftime('%Y-%m-%d') == \
                date.today().strftime('%Y-%m-%d'):
            # Return event name and formatted start time.
            return event['content']['summary']['text'] + " - " + \
                   datetime.utcfromtimestamp(event['when']['start']['millis']/1000).strftime('%#I:%M %p')


# TinRoof()


def WindJammer():
    windjammer = siteScrape(venues.get("Wind Jammer"))
    date_day = windjammer.xpath('//div[@class="event-arc-day"]//text()')
    date_month = windjammer.xpath('//div[@class="event-arc-month"]//text()')
    event = windjammer.xpath('//h2[@class="event-arc-title"]/a//text()')
    time = windjammer.xpath('//p[@class="event-arc-time"]//text()')
    for dm, dd, e, t in zip(date_month, date_day, event, time):
        # Compare event time to today
        if (dm + ' ' + dd) == date.today().strftime('%b %d'):
            return e + ' - ' + t


WindJammer()


# TODO No specific dates for any events right now. Can't create logic for single events.
# TODO Current functionality returns the last event currently due to above issue. Will not use function right now.
def WoolfeStreet():
    woolfestreet = siteScrape(venues.get("Woolfe Street"))
    events = woolfestreet.xpath('//div[@class="top"]/h2/a//text()')
    date = woolfestreet.xpath('//div[@class="lefty"]/h5//text()')
    
    # print(events)
    
    for a, b in zip(events, date):
        return a + " - " + b


# WoolfeStreet()
