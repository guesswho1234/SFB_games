from otree.api import *
from config import *
import markupsafe

author = 'Felix Holzmeister and Sebastian Bachler'

doc = """
Home page:
 
Access games and change participant settings
"""


class Constants(BaseConstants):
    name_in_url = 'i_homePage'
    players_per_group = None
    num_rounds = 1

    colorChoices = [i for i in range(len(colorLabels))]

    colorChoicesLang = []
    for i in range(len(colorLabels)):
        choice = []

        for key, value in colorLabels[i]['name_lang'].items():
            choice.append(getLangElement(key, value))

        colorChoicesLang.append([colorLabels[i]['colorCode'], markupsafe.Markup(wrapContent(''.join(choice), 'div'))])

    initialColorChoice = 0

    # form fields for items
    G = [None] * len(configGames)

    for i, item in enumerate(configGames):
        gameLabels = getLangElements(item['display_names_lang'].items())
        gameLabels = ''.join(gameLabels)
        G[i] = models.BooleanField(widget=widgets.CheckboxInput,
                                   label=gameLabels,
                                   initial=True,
                                   blank=True)


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        from otree.models.session import Session
        from otree.room import ROOM_DICT

        # get latest demo session for home page
        demoSession = getLatestDemoSession(Session, configHomePage)

        # get all sessions that are not demos or archived
        sessions = (
            Session.objects_filter(is_demo=False, archived=False)
            .order_by(Session.id.desc())
            .all()
        )

        # get rooms attributed to sessions
        sessions = [dict(session=s,
                         sessionNumVisited=sum([p.visited for p in s.get_participants()]),
                         sessionNumUnvisited=s.num_participants - sum([p.visited for p in s.get_participants()]),
                         sessionCapacity=round((s.num_participants - sum([p.visited for p in s.get_participants()])) / s.num_participants, 2),
                         room=next((key for key, value in ROOM_DICT.items() if value == s.get_room()), None))
                    for s in sessions]

        # room setup
        homePageSetup = dict(display_name=configHomePage['display_name'], session_config_name=configHomePage['name'], room_name=roomHomePage['name'])
        gameSetup = [dict(display_name=configGames[i]['display_name'], session_config_name=configGames[i]['name'], room_name=roomsGames[i]['name']) for i in range(len(roomsGames))]

        return {
            "minParticipants": minParticipants,
            "maxParticipants": maxParticipants,
            "demoSession": demoSession,
            "redirect": not self.session.is_demo,
            "sessions": sessions,
            "homePageSetup": homePageSetup,
            "gameSetup": gameSetup,
            "homePageUrl": homePageUrl,
            "homePageDisplayUrl": baseUrl + homePageUrl,
            "homePageUrlQr": homePageUrlQr
        }


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    color = models.StringField(widget=widgets.RadioSelect,
                               label="",
                               choices=Constants.colorChoicesLang)

    for i in range(len(configGames)):
        exec("G_%d = Constants.G[i]" % int(i + 1))
        del i

    alwaysIncorrectFormField = models.IntegerField(widget=widgets.RadioSelect,
                                                   label="",
                                                   choices=[-1],
                                                   initial=-1)
