from otree.api import *
from .models import Constants
from config import *


class InitialWaitPage(WaitPage):
    template_name = 'global/elements/wait_template.html'

    group_by_arrival_time = True

    title_text = waitTitleTexts
    body_text = waitBodyTexts

    def vars_for_template(self):
        return {
            "languages": languages
        }


class Offer(Page):
    form_model = 'group'
    form_fields = ['ug_offer']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        return {
            "languages": languages
        }


class WaitForProposer(WaitPage):
    template_name = 'global/elements/wait_template.html'

    title_text = waitTitleTexts
    body_text = waitBodyTexts

    def vars_for_template(self):
        return {
            "languages": languages
        }


class Accept(Page):
    form_model = 'group'
    form_fields = ['ug_accept']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {
            "languages": languages
        }


class ResultsWaitPage(WaitPage):
    template_name = 'global/elements/wait_template.html'

    title_text = waitTitleTexts
    body_text = waitBodyTexts

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    def vars_for_template(self):
        return {
            "languages": languages
        }


class Results(Page):
    def vars_for_template(self):
        return {
            "languages": languages
        }


page_sequence = [
    InitialWaitPage,
    Offer,
    WaitForProposer,
    Accept,
    ResultsWaitPage,
    Results
]
