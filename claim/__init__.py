from otree.api import *

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

# PAGES
class Introduction(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(opt_in = player.session.config['opt_in_rebate'])

class Claim(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['opt_in_rebate']

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
    


page_sequence = [
    Introduction,
    Claim
]