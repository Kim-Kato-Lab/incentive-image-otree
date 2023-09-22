from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0,
    doc=""
)

PARTICIPANT_FIELDS = [
    'endowment',
    'rebate',
    'donate',
    'receipt',
    'payoff_list',
    'partial_report'
]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True
POINTS_CUSTOM_NAME = 'コイン'

SESSION_CONFIGS = [
    dict(
        name='donation',
        display_name="Donation experiment: Incentive and Image",
        app_sequence=[
            'quiz',
            'donation',
            'claim',
            'survey',
            'payment_info',
        ],
        num_demo_participants=4,
        reveal_information = True,
        opt_in = True
    )
]

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Economic Experiments developed by Hiroki Kato.
Source code can be found at <a href='https://github.com/KatoPachi'>Github</a>
"""

SECRET_KEY = environ.get('OTREE_SECRET_KEY')