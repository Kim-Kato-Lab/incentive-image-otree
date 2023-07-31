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
    HIGH_ROLE = 'High earner'
    LOW_ROLE = 'Low earner'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.CurrencyField(initial=cu(0))
    donate = models.CurrencyField(min=0)

# FUNCTIONS
def set_endowment(group: Group):
    high = group.get_player_by_role(C.HIGH_ROLE)
    low = group.get_player_by_role(C.LOW_ROLE)
    high.endowment = 75
    low.endowment = 25

def donate_max(player: Player):
    return player.endowment

def set_payoffs(group: Group):
    players = group.get_players()
    for p in players:
        p.payoff = p.endowment - p.donate


# PAGES
class WaitStart(WaitPage):
    after_all_players_arrive = set_endowment

class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        if player.role == C.HIGH_ROLE:
            partner = group.get_player_by_role(C.LOW_ROLE)
        else:
            partner = group.get_player_by_role(C.HIGH_ROLE)
        return dict(partner_coin = partner.endowment) 


class Donate(Page):
    form_model = 'player'
    form_fields = ['donate']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [
    WaitStart,
    Introduction,
    Donate,
    ResultsWaitPage,
    Results
]