#!/usr/bin/env python
# coding: utf-8

# In[16]:


def get_base_army_compositions():
    army_compositions = {
        7: {
            'attack': {
                'troops': ['Balloon', 'Hog Rider', 'Wizard', 'Archer'],
                'spells': ['Heal Spell', 'Rage Spell'],
                'siege': None,
                'heroes': ['Barbarian King'],
                'pets': None
            },
            'farming': {
                'troops': ['Barbarian', 'Archer', 'Giant', 'Goblin'],
                'spells': ['Lightning Spell'],
                'siege': None,
                'heroes': ['Barbarian King'],
                'pets': None
            }
        },
        8: {
            'attack': {
                'troops': ['Dragon', 'Balloon', 'Hog Rider', 'Wizard'],
                'spells': ['Heal Spell', 'Rage Spell'],
                'siege': None,
                'heroes': ['Barbarian King'],
                'pets': None
            },
            'farming': {
                'troops': ['Barbarian', 'Archer', 'Giant', 'Goblin'],
                'spells': ['Lightning Spell'],
                'siege': None,
                'heroes': ['Barbarian King'],
                'pets': None
            }
        },
        9: {
            'attack': {
                'troops': ['Hog Rider', 'Valkyrie', 'Wizard', 'Healer'],
                'spells': ['Heal Spell', 'Jump Spell', 'Rage Spell'],
                'siege': None,
                'heroes': ['Barbarian King', 'Archer Queen'],
                'pets': None
            },
            'farming': {
                'troops': ['Barbarian', 'Archer', 'Giant', 'Goblin'],
                'spells': ['Lightning Spell', 'Jump Spell'],
                'siege': None,
                'heroes': ['Barbarian King', 'Archer Queen'],
                'pets': None
            }
        },
        10: {
            'attack': {
                'troops': ['Golem', 'Valkyrie', 'Witch', 'Healer'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Jump Spell'],
                'siege': None,
                'heroes': ['Barbarian King', 'Archer Queen'],
                'pets': None
            },
            'farming': {
                'troops': ['Barbarian', 'Archer', 'Giant', 'Goblin'],
                'spells': ['Lightning Spell', 'Jump Spell'],
                'siege': None,
                'heroes': ['Barbarian King', 'Archer Queen'],
                'pets': None
            }
        },
        11: {
            'attack': {
                'troops': ['P.E.K.K.A', 'Witch', 'Healer', 'Valkyrie'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Jump Spell'],
                'siege': ['Wall Wrecker'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden'],
                'pets': None
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Giant', 'Baby Dragon'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Wall Wrecker'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden'],
                'pets': None
            }
        },
        12: {
            'attack': {
                'troops': ['Electro Dragon', 'P.E.K.K.A', 'Balloon', 'Healer'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Clone Spell'],
                'siege': ['Stone Slammer'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden'],
                'pets': None
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Baby Dragon'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Wall Wrecker'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden'],
                'pets': None
            }
        },
        13: {
            'attack': {
                'troops': ['Yetis', 'Super Wizards', 'Ice Golem'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Invisibility Spell'],
                'siege': ['Log Launcher'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': None
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Super Archer'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Log Launcher'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': None
            }
        },
        14: {
            'attack': {
                'troops': ['Super Bowler', 'Inferno Dragon', 'Electro Titan'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Invisibility Spell'],
                'siege': ['Flame Flinger'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['L.A.S.S.I', 'Electro Owl', 'Mighty Yak', 'Unicorn']
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Super Archer'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Log Launcher'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['L.A.S.S.I', 'Electro Owl', 'Mighty Yak', 'Unicorn']
            }
        },
        15: {
            'attack': {
                'troops': ['Electro Titan', 'Super Bowler', 'Ice Golem'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Recall Spell'],
                'siege': ['Flame Flinger'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['Poison Lizard', 'Frosty', 'Diggy', 'Phoenix']
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Baby Dragon'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Log Launcher'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['Poison Lizard', 'Frosty', 'Diggy', 'Phoenix']
            }},
        16:{
            'attack': {
                'troops': ['Inferno Dragon', 'Super Bowler', 'Electro Titan', 'Ice Golem'],
                'spells': ['Freeze Spell', 'Rage Spell', 'Recall Spell'],
                'siege': ['Flame Flinger'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['Poison Lizard', 'Frosty', 'Diggy', 'Phoenix']
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Baby Dragon'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Log Launcher'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['Poison Lizard', 'Frosty', 'Diggy', 'Phoenix']
            }},
          17:{ 
            'attack': {
                'troops': ['Electro Dragon', 'Super Miner', 'Super Wizard', 'Ice Golem'],
                'spells': ['Clone Spell', 'Rage Spell', 'Invisibility Spell'],
                'siege': ['Battle Blimp'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['Spirit Fox', 'Frosty', 'Diggy', 'Phoenix']
            },
            'farming': {
                'troops': ['Sneaky Goblin', 'Super Archer'],
                'spells': ['Jump Spell', 'Invisibility Spell'],
                'siege': ['Log Launcher'],
                'heroes': ['Barbarian King', 'Archer Queen', 'Grand Warden', 'Royal Champion'],
                'pets': ['Spirit Fox', 'Frosty', 'Diggy', 'Phoenix']
            }
        }
    }
    
    return army_compositions






