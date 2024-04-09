from otree.api import *
from config import *
import markupsafe


author = 'Felix Holzmeister and Sebastian Bachler'

doc = """
Prisoners Dilemma:

Two players are asked separately, whether they want to cooperate or defect. Their choices directly determine 
the payoffs. This is the one-shot version of the game.
"""


class Constants(BaseConstants):
    name_in_url = 'g_prisonersDilemma'
    players_per_group = 2
    num_rounds = 1

    # payoff if one player defects and the other cooperates
    pd_betray_payoff = Currency(10)
    pd_betrayed_payoff = Currency(0)

    # payoff if both players cooperate or both defect
    pd_both_cooperate_payoff = Currency(2)
    pd_both_defect_payoff = Currency(5)


class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        return customGroupByArrival(waiting_players, Constants, colorLabels)

    def vars_for_admin_report(self):
        return customAdminReportRedirect(configHomePage)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    pd_decision = models.StringField()

    def other_player(self):
        return self.get_others_in_group()[0]

    def set_payoff(self):

        payoff_matrix = {
            'Cooperate':
                {
                    'Cooperate': Constants.pd_both_cooperate_payoff,
                    'Defect': Constants.pd_betray_payoff
                },
            'Defect':
                {
                    'Cooperate': Constants.pd_betrayed_payoff,
                    'Defect': Constants.pd_both_defect_payoff
                }
        }

        self.payoff = payoff_matrix[self.pd_decision][self.other_player().pd_decision]