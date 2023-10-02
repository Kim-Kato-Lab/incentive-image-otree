from otree.api import *
import random, string

author = 'Hiroki Kato'
doc = """
This is a donation experiment taking monetary incentive (rebate) and image concern
into account.
"""


class C(BaseConstants):
    NAME_IN_URL = 'donation'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 11
    ENDOWMENT = [1500, 500]
    REBATE = [
        [0.6, 0.1],
        [0.5, 0.1],
        [0.4, 0.1],
        [0.4, 0.2],
        [0.3, 0.2],
        [0.3, 0.3],
        [0.2, 0.3],
        [0.2, 0.4],
        [0.1, 0.4],
        [0.1, 0.5],
        [0.1, 0.6]
    ]
    RECEIPT_ID_LEN = [5, 10]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    rebate_list_idx = models.IntegerField(initial=0)
    high_income_rebate = models.FloatField(initial=0)
    low_income_rebate = models.FloatField(initial=0)
    reveal = models.BooleanField()
    opt_in = models.BooleanField()


class Player(BasePlayer):
    endowment = models.IntegerField(initial=0)
    rebate = models.FloatField(initial=0)
    donate = models.IntegerField(min=0)
    observer = models.BooleanField()
    receipt = models.StringField()

# FUNCTIONS
def creating_session(subsession: Subsession):
    subsession.group_randomly(fixed_id_in_group=True)

    for g in subsession.get_groups():
        g.reveal = subsession.session.config['reveal_information']
        g.opt_in = subsession.session.config['opt_in']


def set_role(group: Group):
    # player
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)

    # Role: income
    number = random.random()
    if number < 0.5:
        p1.endowment = C.ENDOWMENT[0] # High income
        p2.endowment = C.ENDOWMENT[1] # Low income
    else:
        p1.endowment = C.ENDOWMENT[1] # Low income
        p2.endowment = C.ENDOWMENT[0] # High income

    # Role: incentive
    idx_list = list(range(len(C.REBATE)))
    now_round = group.subsession.round_number
    if now_round == 1:
        pickup = random.choice(idx_list)
    else:
        past_round = list(range(1, now_round))
        done = [group.in_round(n).rebate_list_idx for n in past_round]
        for i in done:
            idx_list.remove(i)
        pickup = random.choice(idx_list)
    group.rebate_list_idx = pickup

    group.high_income_rebate = C.REBATE[pickup][0]
    group.low_income_rebate = C.REBATE[pickup][1]

    if number < 0.5:
        p1.rebate = group.high_income_rebate
        p2.rebate = group.low_income_rebate
    else:
        p1.rebate = group.low_income_rebate
        p2.rebate = group.high_income_rebate

    # Role: Observer or not (Fixed role)
    if now_round == 1:
        if group.reveal:
            p1.observer = True
            p2.observer = False
        else:
            p1.observer = False
            p2.observer = False
    else:
        p1.observer = p1.in_round(1).observer
        p2.observer = p2.in_round(1).observer


def donate_max(player: Player):
    return player.endowment

# PAGES
class WaitStartApp(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class WaitStartRound(WaitPage):
    after_all_players_arrive = set_role

class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        partner = player.get_others_in_group()[0]
        return dict(
            your_rebate = int(player.rebate * 100),
            partner_coin = partner.endowment,
            partner_rebate = int(partner.rebate * 100)
        )
    
    @staticmethod
    def js_vars(player: Player):
        return dict(
            current = player.round_number,
            max = C.NUM_ROUNDS
        )


class Donate(Page):
    form_model = 'player'
    form_fields = ['donate']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # issue receipt id
        receipt_id = ''
        if player.group.opt_in:
            if player.donate > 0:
                min_len = C.RECEIPT_ID_LEN[0]
                max_len = C.RECEIPT_ID_LEN[1]
                num_list = range(min_len, max_len + 1)
                n = random.choice(num_list)
                receipt_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
                
        player.receipt = receipt_id
        
        # set participant field
        participant = player.participant
        if player.round_number == 1:
            participant.endowment = [player.endowment]
            participant.rebate = [player.rebate]
            participant.donate = [player.donate]
            participant.receipt = [player.receipt]
        else:
            participant.endowment.append(player.endowment)
            participant.rebate.append(player.rebate)
            participant.donate.append(player.donate)
            participant.receipt.append(player.receipt)
    
    @staticmethod
    def js_vars(player: Player):
        return dict(
            current = player.round_number,
            max = C.NUM_ROUNDS,
            rebate_rate = player.rebate,
            endowment = player.endowment
        )

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        partner = player.get_others_in_group()[0]
        return dict(
            opt_in = player.group.opt_in,
            your_rebate = int(player.rebate * 100),
            your_rebate_amount = int(round(player.rebate * player.donate)),
            partner_coin = partner.endowment,
            partner_rebate = int(partner.rebate * 100),
            partner_donate = partner.donate
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            current = player.round_number,
            max = C.NUM_ROUNDS
        )

class Receipt(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.group.opt_in and player.donate > 0
    
    @staticmethod
    def vars_for_template(player: Player):
        return dict(rebate = int(player.rebate * 100))
    
    @staticmethod
    def js_vars(player: Player):
        return dict(
            current = player.round_number,
            max = C.NUM_ROUNDS
        )

class ShuffleWaitPage(WaitPage):
    body_text = """
    他のグループのゲームの終了を待っています。
    しばらくお待ちください。
    """

    wait_for_all_groups = True

page_sequence = [
    WaitStartApp,
    WaitStartRound,
    Introduction,
    Donate,
    ResultsWaitPage,
    Results,
    Receipt,
    ShuffleWaitPage
]