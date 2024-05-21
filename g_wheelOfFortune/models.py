from otree.api import *
from config import *
import markupsafe

author = 'Sebastian Bachler'

doc = """
Wheel of fortune game: 

One player spins the wheel of fortune with a double or nothing payoff.
"""


class Constants(BaseConstants):
    name_in_url = 'g_wheelOfFortune'
    players_per_group = None
    num_rounds = 1

    numColors = 2
    numSegments = 24

    resultValues = [colorLabels[i] for i in range(numColors)]

    resultValuesLang = []
    for i in resultValues:
        choice = []

        for key, value in i['name_lang'].items():
            choice.append(getLangElement(key, value))

        resultValuesLang.append([i['colorCode'], markupsafe.Markup(wrapContent(''.join(choice), 'div'))])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    result = models.StringField(widget=widgets.RadioSelect,
                                label="",
                                choices=Constants.resultValuesLang)

    alwaysIncorrectFormField = models.IntegerField(widget=widgets.RadioSelect,
                                                   label="",
                                                   choices=[-1],
                                                   initial=-1)

    def init_result(self, val):
        self.participant.vars['result'].update({val: [0, 0]})

    def update_result(self, val):
        self.participant.vars['history'].append(val)
        newValue = self.participant.vars['result'][val][0] + 1
        self.participant.vars['result'][val] = [newValue, 0]

        totalFreq = sum([value[0] for value in self.participant.vars['result'].values()])
        for key, value in self.participant.vars['result'].items():
            self.participant.vars['result'][key] = [value[0], (1 - value[0] / totalFreq) * 100]
