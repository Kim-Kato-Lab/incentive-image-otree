from otree.api import *
import random

author = 'Hiroki Kato'
doc = """
This is a donation experiment taking monetary incentive (rebate) and image concern
into account.
"""

# FUNCTION and CLASS
class C(BaseConstants):
    NAME_IN_URL = 'claim'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

def create_input_field(label):
    return models.StringField(
        label = label,
        blank = True,
        initial = ''
    )

class Player(BasePlayer):
    input1 = create_input_field('第1ラウンドの寄付')
    input2 = create_input_field('第2ラウンドの寄付')
    input3 = create_input_field('第3ラウンドの寄付')
    input4 = create_input_field('第4ラウンドの寄付')
    input5 = create_input_field('第5ラウンドの寄付')
    input6 = create_input_field('第6ラウンドの寄付')
    input7 = create_input_field('第7ラウンドの寄付')
    input8 = create_input_field('第8ラウンドの寄付')
    input9 = create_input_field('第9ラウンドの寄付')
    input10 = create_input_field('第10ラウンドの寄付')
    input11 = create_input_field('第11ラウンドの寄付')
    correct1 = models.BooleanField(initial = False)
    correct2 = models.BooleanField(initial = False)
    correct3 = models.BooleanField(initial = False)
    correct4 = models.BooleanField(initial = False)
    correct5 = models.BooleanField(initial = False)
    correct6 = models.BooleanField(initial = False)
    correct7 = models.BooleanField(initial = False)
    correct8 = models.BooleanField(initial = False)
    correct9 = models.BooleanField(initial = False)
    correct10 = models.BooleanField(initial = False)
    correct11 = models.BooleanField(initial = False)

def set_payoff(group: Group):
    for player in group.get_players():
        # calculate payoff
        participant = player.participant
        endowment = participant.endowment
        donate = participant.donate
        rebate = participant.rebate

        payoff_wo_rebate = []
        payoff_w_rebate = []
        for i in range(len(endowment)):
            hold = endowment[i] - donate[i]
            payback = int(round(rebate[i] * donate[i], 0))
            payoff_wo_rebate.append(hold)
            payoff_w_rebate.append(hold + payback)
        
        # set payoff_list
        if player.session.config['opt_in']:
            payoff_list_input = []
            for i in range(len(endowment)):
                if getattr(player, 'correct' + str(i + 1)):
                    payoff_list_input.append(payoff_w_rebate[i])
                else:
                    payoff_list_input.append(payoff_wo_rebate[i])
            
            participant.payoff_list = payoff_list_input
        else:
            participant.payoff_list = payoff_w_rebate
        
        # calculate realized payoff
        pickup = random.sample(participant.payoff_list, 2)
        participant.payoff = sum(pickup)

# PAGES
class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(opt_in = player.session.config['opt_in'])

class Claim(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['opt_in']

    @staticmethod
    def get_form_fields(player: Player):
        participant = player.participant
        donate = participant.donate
        nonzero_donate = [x > 0 for x in donate]
        idx = [i for i, x in enumerate(nonzero_donate) if x]
        form = []
        for x in idx:
            form.append('input' + str(x + 1))
        
        return form
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # check correct ID
        participant = player.participant
        receipt = participant.receipt

        partial_report = False

        for i in range(len(receipt)):
            input_field = 'input' + str(i + 1)
            input_id = getattr(player, input_field)
            correct_id = receipt[i]
            if input_id == correct_id:
                correct_field = 'correct' + str(i + 1)
                setattr(player, correct_field, True)
            
            if not partial_report:
                if input_id == '' and correct_id != '':
                    partial_report = True
        
        participant.partial_report = partial_report

class Wait(WaitPage):
    after_all_players_arrive = set_payoff


page_sequence = [
    Introduction,
    Claim,
    Wait
]