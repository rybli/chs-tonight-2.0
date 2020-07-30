from bs4 import BeautifulSoup as bs
import requests
from datetime import date
import re

def MusicFarm():
    webpage = bs(open("PourHouse.html", "r"), "html.parser")
    # print(webpage)
    eventInfo = webpage.find('main', {"class": "site-main"})
    print(eventInfo)
    # eventInfo = webpage.find('div', {"class": "rhino-widget-list"})
    # for eventDate, eventName, eventTime in zip(eventInfo.findAll('div', {"class": "eventDateList"}),
    #                                            eventInfo.findAll('div', {"class": "col-12 px-0 eventTitleDiv"}),
    #                                            eventInfo.findAll('div', {"class": "d-block eventsColor eventDoorStartDate"})):
    #     if eventDate.text.strip() == date.today().strftime("%b %d"):
    #         MFeventName = eventName.text
    #         return  MFeventName
    #     else:
    #         MFeventName = "No Events"
    #         return MFeventName

MusicFarm()