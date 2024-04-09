from os import environ
from config import *
from functions import *

SESSION_CONFIGS = [configHomePage] + configGames

ROOMS = [roomHomePage] + roomsGames

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00
)

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_CUSTOM_NAME = getLangElements(pointsCustomName.items())

DEBUG = False if environ.get('OTREE_PRODUCTION') not in {None, '', '0'} else True

ADMIN_USERNAME = environ.get('OTREE_ADMIN_USERNAME')
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'b%v(6@a_5@q!axsw+s#z!vv=cvbo#ho&(rjt36y45h_907#b+q'

INSTALLED_APPS = ['otree']

with open('_templates/global/elements/init.html', 'r') as file:
    initHtml = file.read() % (configHomePage['name'], minParticipants)

DEMO_PAGE_INTRO_HTML = initHtml
DEMO_PAGE_TITLE = "SFB Games"
