from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    ## Questionnaire items
    STRING_CHOICE = {
        "field": models.StringField,
        "items": {
            "academic_field": {
                "question": 'あなたの学部は以下の三つの領域のうちどれに当てはまりますか。',
                "choice": [
                    ['humanities', '人文科学系（文学・心理学・歴史学など）'],
                    ['social', '社会科学系（法学・政治学・経済学・社会学など）'],
                    ['natural', '自然科学系（物理・工学・数学・医学など）']
                ]
            }
        }
    }
    INT_RANGE = {
        "field": models.IntegerField,
        "items": {
            "age": {
                "question": 'あなたの年齢をお答えください。',
                "min": 0,
                "max": None
            },
            "sibling": {
                "question": 'あなたは兄弟姉妹が何人いますか。人数をお答えください。',
                "min": 0,
                "max": None
            },
            "impression": {
                "question": '''
                    今回の実験で寄付した慈善活動について好意的な印象を持っていますか。
                    「最も好意的である」場合を「10」、「全く好意的とは思わない」場合を「0」として、
                    「0」～「10」の範囲でお答えください。
                ''',
                "min": 0,
                "max": 10
            },
            "other_impression": {
                "question": '''
                    先ほどの質問で5点より高い得点を付けた人は慈善活動に好意的であるとします。
                    今回の実験に参加していただいている人からランダムに10人を選び、
                    そのうち何人が慈善団体に好意的な印象を持っている（5点より高い得点をつけた人）と思いますか。
                    「0」～「10」の範囲でお答えください。
                ''',
                "min": 0,
                "max": 10
            },
            "oblige": {
                "question": '''
                    一般的に、富・権力・名声といった社会的地位が高い人は社会の規範となるようにふるまうべきだと思いますか。
                    「最も強くそのように思う」場合を「10」、「全くそのように考えていない」場合を「0」として、
                    「0」～「10」の範囲でお答えください。
                ''',
                "min": 0,
                "max": 10
            },
            "other_oblige" : {
                "question": '''
                    先ほどの質問で5点より高い得点をつけた人は「社会的地位が高い人は社会の規範となるようにふるまうべき」だと考えているとします。
                    今回の実験に参加していただいている人からランダムに10人を選び、
                    そのうち何人が「社会的地位が高い人は社会の規範となるようにふるまうべき」だと考えている
                    （5点より高い得点をつけた人）と思いますか。
                    「0」～「10」の範囲でお答えください。
                ''',
                "min": 0,
                "max": 10
            }
        }
    }
    LIKERT = {
        "field": models.IntegerField,
        "choice": [
            [5, 'ぴったり当てはまる'],
            [4, 'どちらかというと当てはまる'],
            [3, 'どちらともいえない'],
            [2, 'どちらかというと当てはまらない'],
            [1, '全く当てはまらない']
        ],
        "question": {
            "image": '他人に自分勝手な人間とみられてもよい',
            "horizontal_equity": '学歴や年齢などに関わらず、同じ所得を持っている人は同じ額の税金を支払うべきだと思う',
            "vertical_equity": '高所得者は低所得者よりも高い税金を支払うべきだと思う'
        }
    }
    INT_CHOICE = {
        "field": models.IntegerField,
        "items": {
            "experience": {
                'question': 'あなたはこれまで、なんらかの経済実験に参加したことはありますか。',
                "choice": [
                    [0, 'いいえ'],
                    [1, 'はい']
                ]
            },
            "male": {
                "question": 'あなたの性別をお答えください。',
                "choice": [
                    [0, '女性'],
                    [1, '男性']
                ]
            },
            "foreigner": {
                "question": 'あなたは留学生ですか。',
                "choice": [
                    [1, 'はい'],
                    [0, 'いいえ']
                ]
            },
            "academic_year": {
                "question": 'あなたの学年をお答えください。',
                "choice": [
                    [1, "学部1年"],
                    [2, "学部2年"],
                    [3, "学部3年"],
                    [4, "学部4年"],
                    [5, "博士前期1年"],
                    [6, "博士前期2年"],
                    [7, "博士後期1年"],
                    [8, "博士後期2年"],
                    [9, "博士後期3年"],
                ]
            },
            "economist": {
                "question": '''
                あなたの学部が「社会科学系（法学・政治学・経済学・社会学など）」と回答した方にお尋ねします。
                あなたが所属する学部は経済学部ですか。''',
                "choice": [
                    [0, 'いいえ（経済学部以外）'],
                    [1, 'はい（経済学部）']
                ]
            },
            "past_donation": {
                "question": '''
                あなたは、この1年間に、<b>金銭による寄付</b>を何円くらいしましたか。
                <br>
                ※金銭による寄付とは、あなた自身や家族のためではなく、
                広く公共的・公益的な活動やその活動を行っている団体に対して、
                金銭を自発的に提供する行為のことを言います。''',
                "choice": [
                    [1, '0円'],
                    [2, '1円～500円未満'],
                    [3, '500円～1,000円未満'],
                    [4, '1,000円～3,000円未満'],
                    [5, '3,000円～5,000円未満'],
                    [6, '5,000円～10,000円未満'],
                    [7, '10,000円～25,000円未満'],
                    [8, '25,000円～50,000円未満'],
                    [9, '50,000円以上']
                ]
            },
            "social_class": {
                "question": 'あなたの生活の程度は、世間一般からみて、次のどれに入ると思いますか。',
                "choice": [
                    [1, '上'],
                    [2, '中の上'],
                    [3, '中の中'],
                    [4, '中の下'],
                    [5, '下'],
                    [6, 'わからない']
                ]
            }
        }
    }
    INEQUALITY = {
        "field": models.IntegerField,
        "choice": [
            [0, '配分パターンA'],
            [1, '配分パターンB']
        ],
        "question": {
            "inequality1": '''
            ケース1
            <br>
            配分パターンA：あなたは10,000円、他人は10,000円もらう
            <br>
            配分パターンB：あなたは10,000円、他人は6,000円もらう''',
            "inequality2": '''
            ケース2
            <br>
            配分パターンA：あなたは10,000円、他人は10,000円もらう
            <br>
            配分パターンB：あなたは16,000円、他人は4,000円もらう''',
            "inequality3": '''
            ケース3
            <br>
            配分パターンA：あなたは10,000円、他人は10,000円もらう
            <br>
            配分パターンB：あなたは10,000円、他人は18,000円もらう''',
            "inequality4": '''
            ケース4
            <br>
            配分パターンA：あなたは10,000円、他人は10,000円もらう
            <br>
            配分パターンB：あなたは11,000円、他人は19,000円もらう'''
        }
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    reason_partial_report = models.LongStringField(
        label = '''
            あなたは今回の実験で寄付によるコインの返金を受ける機会がありましたが、
            一部の寄付について返金の申請をしませんでした。
            よろしければ、下記の空欄にその理由を簡単に教えてください。
        ''',
        initial = '',
        blank=True
    )

for k, v in C.STRING_CHOICE["items"].items():
    setattr(
        Player,
        k,
        C.STRING_CHOICE["field"](label = v["question"], choices = v["choice"])
    )

for k, v in C.INT_RANGE["items"].items():
    setattr(
        Player,
        k,
        C.INT_RANGE["field"](label = v["question"], min = v["min"], max = v["max"])
    )

for k, v in C.INT_CHOICE["items"].items():
    setattr(
        Player,
        k,
        C.INT_CHOICE["field"](label = v["question"], choices = v["choice"])
    )

for k, v in C.LIKERT["question"].items():
    setattr(
        Player,
        k,
        C.LIKERT["field"](label = v, choices = C.LIKERT["choice"])
    )

for k, v in C.INEQUALITY["question"].items():
    setattr(
        Player,
        k,
        C.INEQUALITY["field"](label = v, choices = C.INEQUALITY["choice"])
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    template_name = 'survey/SimpleForm.html'
    form_model = 'player'
    form_fields = [
        'male',
        'sibling',
        'foreigner',
        'experience',
        'age',
        'academic_year',
        'academic_field'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.academic_field != "social":
            player.economist = 0
    
    @staticmethod
    def js_vars(player: Player):
        return dict(page = 1)

class Economist(Page):
    template_name = 'survey/SimpleForm.html'
    form_model = 'player'
    form_fields = ['economist']

    @staticmethod
    def is_displayed(player: Player):
        return player.academic_field == "social"
    
    @staticmethod
    def js_vars(player: Player):
        return dict(page = 2)

class Impression(Page):
    template_name = 'survey/SimpleForm.html'
    form_model = 'player'
    form_fields = ['impression', 'other_impression']

    @staticmethod
    def js_vars(player: Player):
        return dict(page = 3)

class Oblige(Page):
    template_name = 'survey/SimpleForm.html'
    form_model = 'player'
    form_fields = ['oblige', 'other_oblige']

    @staticmethod
    def js_vars(player: Player):
        return dict(page = 4)

class Likert(Page):
    form_model = 'player'
    form_fields = C.LIKERT["question"].keys()

    @staticmethod
    def js_vars(player: Player):
        return dict(page = 5)

class SocialClass(Page):
    template_name = 'survey/SimpleForm.html'
    form_model = 'player'
    form_fields = ['social_class']

    @staticmethod
    def js_vars(player: Player):
        return dict(page = 6)

class Donation(Page):
    template_name = 'survey/SimpleForm.html'

    form_model = 'player'
    form_fields = ['past_donation']

    @staticmethod
    def js_vars(player: Player):
        return dict(page = 7)

class Allocation(Page):
    form_model = 'player'
    form_fields = C.INEQUALITY["question"].keys()

    @staticmethod
    def js_vars(player: Player):
        return dict(page = 8)

class PartialReport(Page):
    template_name = 'survey/SimpleForm.html'
    form_model = 'player'
    form_fields = ['reason_partial_report']

    @staticmethod
    def is_displayed(player: Player):
        return player.participant.partial_report
    
    @staticmethod
    def js_vars(player: Player):
        return dict(page = 9)

page_sequence = [
    Demographics,
    Economist,
    Impression,
    Oblige,
    Likert,
    SocialClass,
    Donation,
    Allocation,
    PartialReport
]