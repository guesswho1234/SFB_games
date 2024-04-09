from otree.api import *
from .models import Constants
from config import *


class HomePage(Page):
    all_fields = list()

    for i in range(len(Constants.G)):
        all_fields.append("G_%d" % int(i + 1))

    all_fields.append("color")
    all_fields.append("alwaysIncorrectFormField")

    form_model = "player"
    form_fields = all_fields

    def vars_for_template(self):
        # set games according to session settings
        games = [dict(cG, player_range=range(cG['min_participants'])) for cG in configGames]

        if 'games' not in self.participant.vars.keys():
            self.participant.vars['games'] = [True for g in games]

        # set games according to participant settings
        gamesExcludedByParticipant = [i for i in range(len(self.participant.vars['games'])) if self.participant.vars['games'][i] is False]
        for i in sorted(gamesExcludedByParticipant, reverse=True):
            del games[i]

        # set participant label (3 parts: <color>_<id>_<nonce>)
        # participant color
        if 'color' not in self.participant.vars.keys():
            self.participant.vars['color'] = Constants.initialColorChoice

        # participant label id
        labelId = self.participant.id_in_session

        # participant nonce
        if 'nonce' not in self.participant.vars.keys():
            self.participant.vars['nonce'] = 0
        else:
            self.participant.vars['nonce'] += 1

        labelNonce = self.participant.vars['nonce']

        # pass data to template
        return {
            "languages": languages,
            "colorCodeSelected": colorLabels[int(self.participant.vars['color'])]['colorCode'],
            "label": dict(labelId=labelId, labelNonce=labelNonce),
            "room_name_prefix": room_name_prefix,
            "games": games,
            "homePageUrl": homePageUrl,
            "homePageDisplayUrl": baseUrl + homePageUrl,
            "homePageUrlQr": homePageUrlQr
        }

    # form check callback exploit to change games and color
    def error_message(self, values):
        self.participant.vars['color'] = [i for i in range(len(colorLabels)) if colorLabels[i]['colorCode'] == values['color']][0]
        self.participant.vars['games'] = [values[field_name] for field_name in values if 'G_' in field_name]

        return dict(alwaysIncorrectFormField="")


page_sequence = [
    HomePage
]
