import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92'
    WARNING = '\033[93'
    FAIL = '\033[91'
    ENDC = '\033[0'
    BOLD = '\033[1'
    UNDERLINE = '\033[4'

class Person:
    def __init__(self, hp, mp, attack,df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attack_l = attack - 10
        self.attack_h = attack +10
        self.df = df
        self.magic = magic
        self.actions = ['Attack', 'Magic']

    def generate_damage(self):
        return random.randrange(self.attack_l, self.attack_h)

    def generate_spell_damage(self, i):
        mg_l = self.magic[i]['dmg'] - 5
        mg_h = self.magic[i]['dmg'] + 5
        return random.randrange(mg_l, mg_h)

    def take_damage(self, dmg):
        self.hp -=dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(selfself, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']


    def choose_action(self):
        i = 1
        print('Actions')
        for item in self.actions:
            print (str(i) + ':' + item)
            i = i+1

    def choose_magic(self):
        i = 1
        print('Magic')
        for spell in self.magic:
            print(str(i) + ':' + spell['name'], "(cost", str(spell['mp']) + ')')