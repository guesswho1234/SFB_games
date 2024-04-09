from otree.api import *
from config import *
import random

from .bt_config import Constants

author = 'Felix Holzmeister, Armin Pfurtscheller, and Sebastian Bachler'

doc = """
Bomb Risk Elicitation Task (BRET):
 
Similar to Crosetto/Filippin (2013), Journal of Risk and Uncertainty (47): 31-65.
"""


# ******************************************************************************************************************** #
# *** CLASS SUBSESSION *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        return customAdminReportRedirect(configHomePage)


# ******************************************************************************************************************** #
# *** CLASS GROUP *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass


# ******************************************************************************************************************** #
# *** CLASS PLAYER *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):

    # whether bomb is collected or not
    # store as integer because it's easier for interop with JS
    bomb = models.IntegerField()

    # location of bomb
    bomb_row = models.PositiveIntegerField()
    bomb_col = models.PositiveIntegerField()

    # number of collected boxes
    boxes_collected = models.IntegerField()

    # --- set round results and player's payoff
    # ------------------------------------------------------------------------------------------------------------------
    pay_this_round = models.BooleanField()
    round_result = models.CurrencyField()

    def set_payoff(self):

        # determine round_result as (potential) payoff per round
        if self.bomb:
            self.round_result = Currency(0)
        else:
            self.round_result = self.boxes_collected * Constants.box_value

        # set payoffs if <random_payoff = True> to round_result of randomly chosen round
        # randomly determine round to pay on player level
        if self.subsession.round_number == 1:
            self.participant.vars['round_to_pay'] = random.randint(1,Constants.num_rounds)

        if Constants.random_payoff:
            if self.subsession.round_number == self.participant.vars['round_to_pay']:
                self.pay_this_round = True
                self.payoff = self.round_result
            else:
                self.pay_this_round = False
                self.payoff = Currency(0)

        # set payoffs to round_result if <random_payoff = False>
        else:
            self.payoff = self.round_result
