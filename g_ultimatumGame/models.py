from otree.api import *
from config import *
import markupsafe

author = 'Felix Holzmeister and Sebastian Bachler'

doc = """
Ultimatum game: 

One player makes an offer while the other can either accepts or rejects the offer.
"""


class Constants(BaseConstants):
    name_in_url = 'g_ultimatumGame'
    players_per_group = 2
    num_rounds = 1

    ug_endowment = 10
    ug_outside = 0
    ug_increment = 1

    ug_choices = currency_range(0, ug_endowment, ug_increment)

    ug_choicesTexts = dict(en=[" for player B, ", " for me"],
                           de=[" für Spieler B, ", " für mich"])

    ug_choicesLang = []
    for i in range(len(ug_choices)):
        choice = []

        for key, value in ug_choicesTexts.items():
            choice.append(getLangElement(key, str(ug_choices[i]) + value[0] + str(int(ug_endowment) - ug_choices[i]) + value[1]))

        ug_choicesLang.append([i, markupsafe.Markup(wrapContent(''.join(choice)))])


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        return customGroupByArrival(waiting_players, Constants, colorLabels)

    def vars_for_admin_report(self):
        return customAdminReportRedirect(configHomePage)


class Group(BaseGroup):
    ug_offer = models.IntegerField(widget=widgets.RadioSelect,
                                   label="",
                                   choices=Constants.ug_choicesLang,
                                   initial=None)
    ug_accept = models.BooleanField()

    def set_payoffs(self):
        p1, p2 = self.get_players()

        if self.ug_accept:
            p1.payoff = Constants.ug_endowment - self.ug_offer
            p2.payoff = self.ug_offer
        else:
            p1.payoff = Constants.ug_outside
            p2.payoff = Constants.ug_outside


class Player(BasePlayer):
    pass
