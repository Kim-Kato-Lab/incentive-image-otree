from otree.api import *

author = 'Hiroki Kato'
doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class Payment(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return dict(
            participation_fee = player.session.config['participation_fee'],
            realized_payoff = participant.payoff,
            p4p = participant.payoff.to_real_world_currency(player.session),
            get_money = participant.payoff_plus_participation_fee()
        )


page_sequence = [Payment]
