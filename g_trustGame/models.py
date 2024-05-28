from otree.api import *
from config import *
import markupsafe


author = 'Felix Holzmeister and Sebastian Bachler'

doc = """
Trust game: 

One player sends money to another player, which then can decide how much to keep and how much to send back.
"""


class Constants(BaseConstants):
    name_in_url = 'g_trustGame'
    players_per_group = 2
    num_rounds = 1

    tg_endowment = 3
    tg_multiplier = 3

    tg_choicesTexts = dict(en=[" for the other player, ", " for me"],
                           de=[" für den anderen Person, ", " für mich"])

    tg_choicesOffer = currency_range(0, tg_endowment, 1)

    tg_choicesLangOffer = []
    for i in range(len(tg_choicesOffer)):
        choice = []

        for key, value in tg_choicesTexts.items():
            choice.append(
                getLangElement(key, str(tg_choicesOffer[i]) + value[0] + str(int(tg_endowment) - tg_choicesOffer[i]) + value[1]))

        tg_choicesLangOffer.append([i, markupsafe.Markup(wrapContent(''.join(choice)))])


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        return customGroupByArrival(waiting_players, Constants, colorLabels)

    def vars_for_admin_report(self):
        return customAdminReportRedirect(configHomePage)


class Group(BaseGroup):
    tg_offer = models.IntegerField(widget=widgets.RadioSelect,
                                   label="",
                                   choices=Constants.tg_choicesLangOffer,
                                   initial=None)
    tg_return = models.IntegerField(widget=widgets.RadioSelect,
                                   label="",
                                   initial=None)

    def tg_return_choices(self):
        tg_multipliedCoins = self.tg_offer * Constants.tg_multiplier
        tg_choicesReturn = currency_range(0, tg_multipliedCoins, 1)

        tg_choicesLangReturn = []
        for i in range(len(tg_choicesReturn)):
            choice = []

            for key, value in Constants.tg_choicesTexts.items():
                choice.append(
                    getLangElement(key,
                                   str(tg_choicesReturn[i]) + value[0] + str(int(tg_multipliedCoins) - tg_choicesReturn[i]) +
                                   value[1]))

            tg_choicesLangReturn.append([i, markupsafe.Markup(wrapContent(''.join(choice)))])

        return tg_choicesLangReturn

    def set_payoffs(self):
        p1, p2 = self.get_players()

        p1.payoff = Constants.tg_endowment - self.tg_offer + self.tg_return
        p2.payoff = self.tg_offer * Constants.tg_multiplier - self.tg_return


class Player(BasePlayer):
    pass
