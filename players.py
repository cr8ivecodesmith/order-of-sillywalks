from random import random


class BasePlayer():

    default_stats = {
        'name': 'nobody',
        'health': 0,
        'strength': 0,
        'dexterity': 0,
        'agility': 0,
    }

    def __init__(self, stats=default_stats):
        return self.stats

    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr

    def attack_success(self, defender, modifiers):
        chance = False
        if random(1, self.stats['dexterity'] + defender.stats['agility']) <= self.stats['dexterity']:
            chance = True

        return chance

    def defend_success(self, attacker, modifiers):
        chance = False
        if random(1, self.stats['agility'] + attacker.stats['dexterity']) <= self.stats['agility']:
            chance = True

        return chance
