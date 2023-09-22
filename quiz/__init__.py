from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'quiz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    ENDOWMENT = [200, 50]
    DONATE = [100, 10]
    REBATE = [0.5, 0.1]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    reveal = models.BooleanField()
    opt_in = models.BooleanField()
    q1 = models.IntegerField(
        label = '''
            あなたは寄付によっていくらの返金をもらえますか？
            整数（半角数字）で解答してください。
        '''
    )
    q2 = models.IntegerField(
        label = '''
            返金を受けた後、最終的にあなたの手元に残るコインはいくらですか？
            整数（半角数字）で解答してください。
        '''
    )
    q3 = models.BooleanField(
        choices = [
            [False, 'いいえ'],
            [True, 'はい']
        ],
        label = '''
            あなたのパートナーであるBさんは、あなたがいくら寄付したことを知っていますか？
        '''
    )
    q4 = models.IntegerField(
        label = '''
            あなたは寄付によっていくらの返金をもらえますか？
            整数（半角数字）で解答してください。
        '''
    )
    q5 = models.IntegerField(
        label = '''
            返金を受けた後、最終的にあなたの手元に残るコインはいくらですか？
            整数（半角数字）で解答してください。
        '''
    )
    q6 = models.BooleanField(
        choices = [
            [False, 'いいえ'],
            [True, 'はい']
        ],
        label = '''
            あなたのパートナーであるAさんは、あなたがいくら寄付したことを知っていますか？
        '''
    )

for k in range(6):
    setattr(
        Player,
        'correct_q' + str(k + 1),
        models.BooleanField()
    )

# FUNCTIONS
def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.reveal = subsession.session.config['reveal_information']
        p.opt_in = subsession.session.config['opt_in']

# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Quiz(Page):
    form_model = 'player'
    form_fields = [
        'q1',
        'q2',
        'q3',
        'q4',
        'q5',
        'q6'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            high_income = C.ENDOWMENT[0],
            low_income = C.ENDOWMENT[1],
            high_income_rebate = C.REBATE[0] * 100,
            low_income_rebate = C.REBATE[1] * 100,
            high_income_donate = C.DONATE[0],
            low_income_donate = C.DONATE[1]
        )
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        low_income_rebate_amount = int(C.DONATE[1] * C.REBATE[1])
        low_income_payoff = int(C.ENDOWMENT[1] - C.DONATE[1] + low_income_rebate_amount)
        low_income_observe = False

        high_income_rebate_amount = int(C.DONATE[0] * C.REBATE[0])
        high_income_payoff = int(C.ENDOWMENT[0] - C.DONATE[0] + high_income_rebate_amount)
        high_income_observe = player.reveal

        player.correct_q1 = player.q1 == high_income_rebate_amount
        player.correct_q2 = player.q2 == high_income_payoff
        player.correct_q3 = player.q3 == high_income_observe
        player.correct_q4 = player.q4 == low_income_rebate_amount
        player.correct_q5 = player.q5 == low_income_payoff
        player.correct_q6 = player.q6 == low_income_observe

class Answer(Page):
    @staticmethod
    def vars_for_template(player: Player):
        low_income_rebate_amount = int(C.DONATE[1] * C.REBATE[1])
        high_income_rebate_amount = int(C.DONATE[0] * C.REBATE[0])

        return dict(
            low_income_rebate_amount = low_income_rebate_amount,
            low_income_payoff = int(C.ENDOWMENT[1] - C.DONATE[1]) + low_income_rebate_amount,
            low_income_observe = 'いいえ',
            high_income_rebate_amount = high_income_rebate_amount,
            high_income_payoff = int(C.ENDOWMENT[0] - C.DONATE[0]) + high_income_rebate_amount,
            high_income_observe = 'はい' if player.reveal else 'いいえ'
        )
    
class Finish(Page):
    @staticmethod
    def is_display(player: Player):
        checker = [
            player.correct_q1,
            player.correct_q2,
            player.correct_q3,
            player.correct_q4,
            player.correct_q5,
            player.correct_q6
        ]

        return all(checker)
    
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]

page_sequence = [
    Introduction,
    Quiz,
    Answer,
    Finish
]