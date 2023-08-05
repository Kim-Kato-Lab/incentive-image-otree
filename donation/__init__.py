from otree.api import *
import random

author = 'Hiroki Kato'
doc = """
This is a donation experiment taking monetary incentive (rebate) and image concern
into account.
"""


class C(BaseConstants):
    NAME_IN_URL = 'donation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    HIGH_ROLE = 'High earner'
    LOW_ROLE = 'Low earner'
    ENDOWMENT = [75, 25]
    REBATE = [
        [0.5, 0.15],
        [0.5, 0.25],
        [0.5, 0.5]#,
        # [0.25, 0.5],
        # [0.15, 0.5],
        # [0.25, 0.1],
        # [0.1, 0.25],
        # [0.15, 0.15]
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    list_row = models.IntegerField(initial=0)
    high_income_rebate = models.FloatField(initial=0)
    low_income_rebate = models.FloatField(initial=0)
    reveal = models.BooleanField()


class Player(BasePlayer):
    endowment = models.IntegerField(initial=0)
    donate = models.IntegerField(min=0)
    rebate = models.FloatField(initial=0)
    payoff_wo_rebate = models.IntegerField(initial=0)
    payoff_w_rebate = models.IntegerField(initial=0)
    observable = models.BooleanField()

# FUNCTIONS
def creating_session(subsession: Subsession):
    mat = subsession.get_group_matrix()
    new_mat = []

    for row in mat:
        l = random.sample(row, len(row))
        new_mat.append(l)
    
    subsession.set_group_matrix(new_mat)

    for g in subsession.get_groups():
        g.reveal = subsession.session.config['one_sided_information']


def set_role(group: Group):
    # rebate incentive
    rebate_list = list(range(len(C.REBATE)))
    now_round = group.subsession.round_number
    if now_round == 1:
        pickup = random.sample(rebate_list, 1)[0]
    else:
        past_round = list(range(1, now_round))
        done = [group.in_round(n).list_row for n in past_round]
        for i in done:
            rebate_list.pop(i)
        pickup = random.sample(rebate_list, 1)[0]
    group.list_row = pickup
    group.high_income_rebate = C.REBATE[pickup][0]
    group.low_income_rebate = C.REBATE[pickup][1]

    # income
    high = group.get_player_by_role(C.HIGH_ROLE)
    low = group.get_player_by_role(C.LOW_ROLE)
    high.rebate = group.high_income_rebate
    low.rebate = group.low_income_rebate
    high.endowment = C.ENDOWMENT[0]
    low.endowment = C.ENDOWMENT[1]

    # set one-sided revealed information
    if group.reveal:
        num1 = group.get_player_by_id(1)
        num2 = group.get_player_by_id(2)
        if now_round == 1:
            num1.observable = False
            num2.observable = True
        else:
            num1.observable = num1.in_round(1).observable
            num2.observable = num2.in_round(1).observable


def donate_max(player: Player):
    return player.endowment

def set_payoffs(group: Group):
    players = group.get_players()
    for p in players:
        p.payoff_wo_rebate = p.endowment - p.donate
        p.payoff_w_rebate = p.payoff_wo_rebate + int(round(p.rebate * p.donate, 0))


# PAGES
class WaitStart(WaitPage):
    after_all_players_arrive = set_role

class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        if player.role == C.HIGH_ROLE:
            partner = group.get_player_by_role(C.LOW_ROLE)
        else:
            partner = group.get_player_by_role(C.HIGH_ROLE)
        return dict(
            your_rebate = int(player.rebate * 100),
            partner_coin = partner.endowment,
            partner_rebate = int(partner.rebate * 100)
        ) 


class Donate(Page):
    form_model = 'player'
    form_fields = ['donate']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        if player.role == C.HIGH_ROLE:
            partner = group.get_player_by_role(C.LOW_ROLE)
        else:
            partner = group.get_player_by_role(C.HIGH_ROLE)
        return dict(
            partner_coin = partner.endowment,
            partner_donate = partner.donate
        )

page_sequence = [
    WaitStart,
    Introduction,
    Donate,
    ResultsWaitPage,
    Results
]