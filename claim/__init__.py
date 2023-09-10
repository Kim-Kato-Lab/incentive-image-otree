from otree.api import *

author = 'Hiroki Kato'
doc = """
This is a donation experiment taking monetary incentive (rebate) and image concern
into account.
"""


class C(BaseConstants):
    NAME_IN_URL = 'claim'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# FUNCTIONS
def creating_session(subsession: Subsession):
    pass


# PAGES
class Introduction(Page):
    pass

class Claim(Page):
    pass

page_sequence = [
    Introduction,
    Claim
]