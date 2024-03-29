from datetime import datetime, timedelta, date
import requests
from lxml import html
import re

#  List of Venues and URLs for about page
venuesAbout = {
    "Gaillard": "https://gaillardcenter.org/buy-tickets",
    "Home Team Downtown": "https://hometeambbq.com/happenings/",
    "Home Team West Ashley": "https://hometeambbq.com/happenings/",
    "Music Farm Charleston": "https://music-farm.com/events/?tribe_bar_rhp_venue=3902",
    "Music Hall": "https://www.charlestonmusichall.com/shows/",
    "Pour House": "https://charlestonpourhouse.com/",
    "Royal American": "https://www.theroyalamerican.com/schedule",
    "Sparrow": "https://www.facebook.com/pg/thesparrowparkcircle/events/",
    "Theatre 99": "https://theatre99.com/schedule/action~posterboard/",
    "Tin Roof": "http://charlestontinroof.com/#schedule",
    "Wind Jammer": "https://the-windjammer.com/events/",
    "Woolfe Street": "https://woolfestreetplayhouse.com/shows/"
}

#  List of URLs for venues scraping
venues = {
    "Gaillard": "https://gaillardcenter.org/buy-tickets",
    "Home Team Downtown": "https://hometeambbq.com/happenings/",
    "Home Team West Ashley": "https://hometeambbq.com/happenings/",
    "Music Farm Charleston": "https://music-farm.com/events/?tribe_bar_rhp_venue=3902",
    "Music Hall": "https://www.charlestonmusichall.com/shows/",
    "Pour House": "https://charlestonpourhouse.com/",
    "Royal American": "https://www.theroyalamerican.com/schedule",
    "Sparrow": "https://www.facebook.com/thesparrowparkcircle/events",
    "Theatre 99": "https://theatre99.com/schedule/action~posterboard/",
    "Tin Roof": "https://tockify.com/api/ngevent?max=12&calname=tinroofschedule",
    "Wind Jammer": "https://the-windjammer.com/events/",
    "Woolfe Street": "https://woolfestreetplayhouse.com/shows/"
}


dt = datetime.strptime(date.today().strftime('%d/%b/%Y'), '%d/%b/%Y')
start = dt - timedelta(days=dt.weekday())
end = start + timedelta(days=6)


def daterange(date1, date2):
    """

    :return [List] List of dates from this Monday to Sunday.
    """
    for n in range(int((date2 - date1).days)+1):
        yield date1 + timedelta(n)


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
    gaillard_week = [dt.strftime("%b %d").replace(" 0", " ") for dt in daterange(start, end)]
    event_today = []
    event_week = []
    # Request site once and store page in variable for local parsing/scraping
    gaillard = siteScrape((venues.get("Gaillard")))
    month = gaillard.xpath('//span[@class="performance-item__date-month"]//text()')
    day = gaillard.xpath('//span[@class="performance-item__date-day"]//text()')
    event = gaillard.xpath('//div[@class="performance-item__title"]//text()')
    time = gaillard.xpath('//div[@class="text-accent performance-item__time"]//text()')

    for event_month, event_day, event_name, event_time in zip(month, day, event, time):
        if (event_month + ' ' + event_day) == date.today().strftime("%b %d").replace(" 0", " "):
            event_today.append(event_name + ' - ' + event_time)
        if (event_month + ' ' + event_day) in gaillard_week:
            event_week.append((event_name + ' - ' + event_time))

    print("Gaillard: ", event_today, event_week)
    return event_today, event_week


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
def HomeTeamDowntown():
    # hometeamdt_week = [dt.strftime("%b %d").replace(" 0", " ") for dt in daterange(start, end)]
    event_today = []
    event_week = []
    return event_today, event_week
    # # Request site once and store page in variable for local parsing/scraping
    # hometeamdt = siteScrape((venues.get("Home Team Downtown")))
    # month = hometeamdt.xpath('//span[@class="performance-item__date-month"]//text()')
    # day = hometeamdt.xpath('//span[@class="performance-item__date-day"]//text()')
    # event = hometeamdt.xpath('//div[@class="performance-item__title"]//text()')
    # time = hometeamdt.xpath('//div[@class="text-accent performance-item__time"]//text()')
    #
    # for event_month, event_day, event_name, event_time in zip(month, day, event, time):
    #     if (event_month + ' ' + event_day) == date.today().strftime("%b %d").replace(" 0", " "):
    #         event_today.append(event_name + ' - ' + event_time)
    #     if (event_month + ' ' + event_day) in hometeamdt_week:
    #         event_week.append((event_name + ' - ' + event_time))
    #
    # print("Home Team Downtown: ", event_today, event_week)
    # return event_today, event_week


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
def HomeTeamWA():
    # hometeamwa_week = [dt.strftime("%b %d").replace(" 0", " ") for dt in daterange(start, end)]
    event_today = []
    event_week = []
    return event_today, event_week
    # # Request site once and store page in variable for local parsing/scraping
    # hometeamdt = siteScrape((venues.get("Home Team West Ashley")))
    # month = hometeamdt.xpath('//span[@class="performance-item__date-month"]//text()')
    # day = hometeamdt.xpath('//span[@class="performance-item__date-day"]//text()')
    # event = hometeamdt.xpath('//div[@class="performance-item__title"]//text()')
    # time = hometeamdt.xpath('//div[@class="text-accent performance-item__time"]//text()')
    #
    # for event_month, event_day, event_name, event_time in zip(month, day, event, time):
    #     if (event_month + ' ' + event_day) == date.today().strftime("%b %d").replace(" 0", " "):
    #         event_today.append(event_name + ' - ' + event_time)
    #     if (event_month + ' ' + event_day) in hometeamwa_week:
    #         event_week.append((event_name + ' - ' + event_time))
    #
    # print("Home Team Downtown: ", event_today, event_week)
    # return event_today, event_week


def MusicFarm():
    """

    :return: [String] Event name and time (formatted)
    """
    musicfarm_week = [dt.strftime("%b %#d") for dt in daterange(start, end)]
    event_today = []
    event_week = []
    musicfarm = siteScrape(venues.get("Music Farm Charleston"))
    day = musicfarm.xpath('//div[@class="eventDateList"]/div//text()')
    event = musicfarm.xpath('//a[@class="url"]/h2//text()')
    time = musicfarm.xpath('//div[@class="d-block eventsColor eventDoorStartDate"]/span//text()')

    for event_day, event_name, event_time in zip(day, event, time):
        # Getting today event info, and week event info
        if event_day.strip() == date.today().strftime("%b %m"):
            event_today.append(event_day + ' - ' + event_time)
        if event_day.strip() in musicfarm_week:
            event_week.append(event_day + ' - ' + event_time)

    print("Music Farm: ", event_today, event_week)
    return event_today, event_week


def MusicHall():
    """

    :return: [String] Event name
    """
    musichall_week = [dt.strftime("%a%#m.%#d").upper() for dt in daterange(start, end)]
    event_today = []
    event_week = []
    musichall = siteScrape(venues.get("Music Hall"))
    day = musichall.xpath('//time[@class="dates"]')
    event = musichall.xpath('//section[@class="cmh-event-content"]/a/h2//text()')
    time = musichall.xpath('//section[@class="cmh-event-content"]/p//text()')

    for event_date, event_name, event_time in zip(day, event, time):
        # Getting today event info, and week event info
        if (event_date.text_content()) == date.today().strftime("%a%#m.%#d").upper():
            event_today.append(event_name + ' - ' + event_time)
        if (event_date.text_content()) in musichall_week:
            event_week.append(event_name + ' - ' + event_time)

    print("Music Hall: ", event_today, event_week)
    return event_today, event_week


def PourHouse():
    pourhouse_week = [dt.strftime("%A, %B %#d, %Y") for dt in daterange(start, end)]
    event_today = []
    event_week = []
    pourhouse = siteScrape(venues.get("Pour House"))
    day = pourhouse.xpath('//p[@class="show-day"]//text()')
    event = pourhouse.xpath('//header[@class="show-header"]/h3')
    door_times = pourhouse.xpath('//table[@class="show-details"]//th[text() = "Doors:"]//following-sibling::td//text()')
    show_times = pourhouse.xpath('//table[@class="show-details"]//th[text() = "Show:"]//following-sibling::td//text()')
    # TODO Some shows do no have a cover listed
    # cover_cost = pourhouse.xpath('//table[@class="show-details"]//th[text() = "Cover:"]//following-sibling::td')

    for event_day, event_name, door_time, event_show_time in zip(day, event, door_times, show_times):
        # Getting today event info, and week event info
        if re.sub("(?<=[0-9])(?:st|nd|rd|th)", "", event_day) == date.today().strftime("%A, %B %#d, %Y"):
            event_today.append(event_name.text_content() + ' - ' + 'Doors: ' + door_time + ' Show: ' + event_show_time)
        if re.sub("(?<=[0-9])(?:st|nd|rd|th)", "", event_day) in pourhouse_week:
            event_week.append(event_name.text_content() + ' - ' + 'Doors: ' + door_time + ' Show: ' + event_show_time)

    print("Pour House: ", event_today, event_week)
    return event_today, event_week


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
def RoyalAmerican():
    event_today = []
    event_week = []
    return event_today, event_week


# TODO No events happening at the moment (Aug 2020) So no data to refactor this function with XPATH.
def Sparrow():
    event_today = []
    event_week = []
    return event_today, event_week


def Theatre99():
    """

    :return: [String] Event name
    """
    theatre99_week = [dt.strftime("%b%#d%a") for dt in daterange(start, end)]
    event_today = []
    event_week = []
    theatre99 = siteScrape(venues.get("Theatre 99"))
    date_month = theatre99.xpath('//div[@class="ai1ec-month"]//text()')
    date_day = theatre99.xpath('//div[@class="ai1ec-day"]//text()')
    date_weekday = theatre99.xpath('//div[@class="ai1ec-weekday"]//text()')
    event = theatre99.xpath('//div[@class="ai1ec-event-title"]/div/a//text()')
    time = theatre99.xpath('//div[@class="ai1ec-posterboard-time"]//text()')

    # Create combined date for comparison.
    dates = []
    for event_month, event_day, event_weekday in zip(date_month, date_day, date_weekday):
        combined_date = event_month + event_day + event_weekday
        dates.append(combined_date)

    for d, e, t in zip(dates, event, time):
        # Getting today event info, and week event info
        if d == date.today().strftime("%b%#d%a"):
            event_today.append(e + ' - ' + t)
        if d in theatre99_week:
            event_week.append(e + ' - ' + t)

    print("Theatre 99: ", event_today, event_week)
    return event_today, event_week


def TinRoof():
    """

    :return: [String] Event name with formatted start time.
    """
    tinroof_week = [dt.strftime('%Y-%m-%d') for dt in daterange(start, end)]
    event_today = []
    event_week = []
    tinroof = requests.get(venues.get("Tin Roof"))
    tinroof_json = tinroof.json()
    for event in tinroof_json['events']:
        # Getting today event info, and week event info
        if datetime.utcfromtimestamp(event['when']['start']['millis']/1000).strftime('%Y-%m-%d') == \
                date.today().strftime('%Y-%m-%d'):
            # Return event name and formatted start time.
            event_today.append(event['content']['summary']['text'] + " - " + \
                   datetime.utcfromtimestamp(event['when']['start']['millis']/1000).strftime('%#I:%M %p'))
        if datetime.utcfromtimestamp(event['when']['start']['millis'] / 1000).strftime('%Y-%m-%d') in tinroof_week:
            event_week.append(event['content']['summary']['text'] + " - " + \
                   datetime.utcfromtimestamp(event['when']['start']['millis']/1000).strftime('%#I:%M %p'))

    print("Tin Roof: ", event_today, event_week)
    return event_today, event_week


def WindJammer():
    """

    :return: [String] Event name with formatted time.
    """
    windjammer_week = [dt.strftime('%b %d') for dt in daterange(start, end)]
    event_today = []
    event_week = []
    windjammer = siteScrape(venues.get("Wind Jammer"))
    date_day = windjammer.xpath('//div[@class="event-arc-day"]//text()')
    date_month = windjammer.xpath('//div[@class="event-arc-month"]//text()')
    event = windjammer.xpath('//h2[@class="event-arc-title"]/a//text()')
    time = windjammer.xpath('//p[@class="event-arc-time"]//text()')
    for dm, dd, e, t in zip(date_month, date_day, event, time):
        # Getting today event info, and week event info
        if (dm + ' ' + dd) == date.today().strftime('%b %d'):
            event_today.append(e + ' - ' + t)
        if (dm + ' ' + dd) in windjammer_week:
            event_week.append(e + ' - ' + t)

    print("Wind Jammer: ", event_today, event_week)
    return event_today, event_week


def WoolfeStreet():
    woolfestreet_week = [dt.strftime('%B %#d, %Y') for dt in daterange(start, end)]
    event_today = []
    event_week = []
    woolfestreet = siteScrape(venues.get("Woolfe Street"))
    events = woolfestreet.xpath('//div[@class="top"]/h2/a//text()')
    dates = woolfestreet.xpath('//div[@class="lefty"]/h5//text()')

    for e, d in zip(events, dates):
        if re.sub("(?<=[0-9])(?:st|nd|rd|th)", "", d) == date.today().strftime("%B %#d, %Y"):
            event_today.append(e)
        if re.sub("(?<=[0-9])(?:st|nd|rd|th)", "", d) == woolfestreet_week:
            event_week.append(e)

    print("Woolfe Street: ", event_today, event_week)
    return event_today, event_week
