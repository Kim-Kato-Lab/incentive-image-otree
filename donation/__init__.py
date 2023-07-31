from otree.api import *


author = 'Hiroki Kato'
doc = """
This is a donation experiment taking monetary incentive (rebate) and image concern
into account.
"""


class C(BaseConstants):
    NAME_IN_URL = 'donation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2
    ENDOWMENT = cu(70)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donate = models.CurrencyField(min=0, max=C.ENDOWMENT)


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    for p in players:
        p.payoff = C.ENDOWMENT - p.donate


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Donate(Page):
    form_model = 'player'
    form_fields = ['donate']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Donate,
    ResultsWaitPage,
    Results
]
