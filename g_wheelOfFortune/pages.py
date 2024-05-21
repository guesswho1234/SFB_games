from otree.api import *
from .models import Constants
from config import *


class WheelOfFortune(Page):
    form_model = "player"
    form_fields = ["result", "alwaysIncorrectFormField"]

    def vars_for_template(self):
        colors = [v["colorCode"] for v in Constants.resultValues]

        if 'result' not in self.participant.vars.keys():
            self.participant.vars['result'] = {}
            self.participant.vars['history'] = []

            for color in colors:
                self.player.init_result(color)

        # pass data to template
        return {
            "languages": languages,
            "hasParticipantLabel": self.participant.label is not None,
            "colors": colors,
            "numSegments": Constants.numSegments,
            "result": self.participant.vars['result'],
            "history": self.participant.vars['history']
        }

    # form check callback exploit to change games and color
    def error_message(self, values):
        self.player.update_result(values["result"])
        return dict(alwaysIncorrectFormField="")


page_sequence = [
    WheelOfFortune
]
