from functions import *

# configurations
configGames = [
    dict(
        name='g_trustGame',
        display_name="GAME: Trust Game",
        display_names_lang=dict(en="Trust Game", de="Vertrauensspiel"),
        min_participants=2,
        num_demo_participants=2,
        app_sequence=['g_trustGame'],
        use_browser_bots=False
    ),
    dict(
        name='g_ultimatumGame',
        display_name="GAME: Ultimatum Game",
        display_names_lang=dict(en="Ultimatum Game", de="Ultimatumspiel"),
        min_participants=2,
        num_demo_participants=2,
        app_sequence=['g_ultimatumGame'],
        use_browser_bots=False
    ),
    dict(
        name='g_prisonersDilemma',
        display_name="GAME: Prisoner's Dilemma",
        display_names_lang=dict(en="Prisoner's Dilemma", de="Gefangenendilemma"),
        min_participants=2,
        num_demo_participants=2,
        app_sequence=['g_prisonersDilemma'],
        use_browser_bots=False
    ),
    dict(
        name='g_bombTask',
        display_name="GAME: Bomb Risk Elicitation Task",
        display_names_lang=dict(en="Bomb Game", de="Bomben Spiel"),
        min_participants=1,
        num_demo_participants=1,
        app_sequence=['g_bombTask'],
        use_browser_bots=False
    ),
dict(
        name='g_whellOfFortune',
        display_name="GAME: Wheel Of Fortune",
        display_names_lang=dict(en="Wheel Of Fortune", de="Glücksrad"),
        min_participants=1,
        num_demo_participants=1,
        app_sequence=['g_wheelOfFortune'],
        use_browser_bots=False
    )
]

minParticipants = max([cG['min_participants'] for cG in configGames])
configHomePage = dict(
    name='i_homePage',
    display_name="HOME PAGE",
    min_participants=minParticipants,
    num_demo_participants=2,
    app_sequence=['i_homePage'],
    use_browser_bots=False
)

# rooms
room_name_prefix = "waitingRoom_"

roomsGames = [dict(name=room_name_prefix + cG['name'], display_name="Waiting Room " + cG['display_name']) for cG in configGames]

roomHomePage = dict(
    name='waitingRoom',
    display_name='Waiting Room'
)

# session size (number of plays possible)
maxParticipants = 400

# base url for the whole application
from os import environ
baseUrl = "https://" + environ.get('HEROKU_APP_DEFAULT_DOMAIN_NAME') if environ.get('HEROKU_APP_DEFAULT_DOMAIN_NAME') not in {None, '', '0'} else "http://localhost:8000"

# colors used for participant labels
colorLabels = [
    dict(colorCode="003361", name_lang=dict(en="dark blue", de="dunkelblau")),
    dict(colorCode="F39200", name_lang=dict(en="orange", de="orange")),
    dict(colorCode="0077BB", name_lang=dict(en="blue", de="blau")),
    dict(colorCode="66CCEE", name_lang=dict(en="light blue", de="hellblau")),
    dict(colorCode="225522", name_lang=dict(en="dark green", de="duneklgrün")),
    dict(colorCode="55AA22", name_lang=dict(en="green", de="grün")),
    dict(colorCode="ACD39E", name_lang=dict(en="light green", de="hellgrün")),
    dict(colorCode="DC050C", name_lang=dict(en="red", de="rot")),
    dict(colorCode="EE3377", name_lang=dict(en="magenta", de="magenta")),
    dict(colorCode="FFAABB", name_lang=dict(en="pink", de="pink")),
    dict(colorCode="BBBBBB", name_lang=dict(en="gray", de="grau")),
    dict(colorCode="AA4499", name_lang=dict(en="purple", de="violett")),
    dict(colorCode="CC6677", name_lang=dict(en="rose", de="rosa")),
    dict(colorCode="882255", name_lang=dict(en="wine red", de="weinrot")),
    dict(colorCode="FFDD44", name_lang=dict(en="yellow", de="gelb")),
    dict(colorCode="993404", name_lang=dict(en="brown", de="braun"))
]

# url and qr code for home page
import segno

homePageUrl = "/room/" + roomHomePage['name']
homePageUrlQr = segno.make_qr(baseUrl + homePageUrl).svg_data_uri(scale=10)

# languages
languages = list(set(key.upper() for cG in configGames for key in cG['display_names_lang'].keys()))

# alternative point text
pointsCustomName = dict(en="Coin(s)",
                        de="Taler")

# wait page texts
waitTitleTexts = dict(en="Please wait",
                      de="Bitte warten")
waitTitleTexts = getLangElements(waitTitleTexts.items())

waitBodyTexts = dict(en="Please wait until the other participant is ready.",
                     de="Bitte warten Sie bis der/die andere Teilnehmer/in bereit ist.")
waitBodyTexts = getLangElements(waitBodyTexts.items())
