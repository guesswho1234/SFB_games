from otree.api import *
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


class Instructions(Page):
    def vars_for_template(self):
        return {
            "languages": languages
        }


class Decision(Page):
    form_model = 'player'
    form_fields = ['pd_decision']

    def vars_for_template(self):
        return {
            "languages": languages
        }


class ResultsWaitPage(WaitPage):
    template_name = 'global/elements/wait_template.html'

    title_text = waitTitleTexts
    body_text = waitBodyTexts

    def vars_for_template(self):
        return {
            "languages": languages
        }

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return {
            "languages": languages,
            'my_decision': self.player.pd_decision,
            'opponent_decision': self.player.other_player().pd_decision,
            'same_choice': self.player.pd_decision == self.player.other_player().pd_decision,
        }


page_sequence = [
    InitialWaitPage,
    Instructions,
    Decision,
    ResultsWaitPage,
    Results
]
