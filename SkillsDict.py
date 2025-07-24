skills = {
    'Bloodline': {
        'Human': {
            'Unburdened': {'Max':1,'Cost':3,'cat':'Bloodline','subcat':'Human'},
            'Good Enough': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Human'},
            'Pillar of the Community': {'Max':1,'Cost':2,'cat':'Bloodline','subcat':'Human'},
            'Force of Will': {'Max':None,'Cost':4,'cat':'Bloodline','subcat':'Human'},
            'Pursuit of Knowledge': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Human'}
        },
        'Effendal': {
            'Effendal Senses': {'Max':1,'Cost':2,'cat':'Bloodline','subcat':'Effendal'},
            'Effendal Agility': {'Max':1,'Cost':5,'cat':'Bloodline','subcat':'Effendal'},
            'Patience': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Effendal'},
            'Weapon Master': {'Max':1,'Cost':6,'cat':'Bloodline','subcat':'Effendal'},
            'Scion of the Land': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Effendal'}
        },
        'Fae Blooded': {
            'Slippery': {'Max':1,'Cost':7,'cat':'Bloodline','subcat':'Fae Blooded'},
            'Magic-Resistant': {'Max':None,'Cost':5,'cat':'Bloodline','subcat':'Fae Blooded'},
            'Charmed Misstep': {'Max':None,'Cost':3,'cat':'Bloodline','subcat':'Fae Blooded'},
            'Glamour': {'Max':1,'Cost':7,'cat':'Bloodline','subcat':'Fae Blooded'},
            'Dominating Gesture': {'Max':None,'Cost':8,'cat':'Bloodline','subcat':'Fae Blooded'}
        },
        'Celestial Blooded': {
            'Rallying Cry': {'Max':None,'Cost':3,'cat':'Bloodline','subcat':'Celestial Blooded'},
            'Healing Touch': {'Max':None,'Cost':6,'cat':'Bloodline','subcat':'Celestial Blooded'},
            'Resurrection': {'Max':None,'Cost':10,'cat':'Bloodline','subcat':'Celestial Blooded'},
            'Rise Towards the Light': {'Max':None,'Cost':5,'cat':'Bloodline','subcat':'Celestial Blooded'},
            'Supernatural Strength': {'Max':1,'Cost':10,'cat':'Bloodline','subcat':'Celestial Blooded'}
        },
        'Demon Blooded': {
            'Draining Touch': {'Max':None,'Cost':5,'cat':'Bloodline','subcat':'Demon Blooded'},
            'Abhorrent Sign': {'Max':None,'Cost':3,'cat':'Bloodline','subcat':'Demon Blooded'},
            'Capitvating Gaze': {'Max':None,'Cost':8,'cat':'Bloodline','subcat':'Demon Blooded'},
            'Sink Into Darkness': {'Max':None,'Cost':5,'cat':'Bloodline','subcat':'Demon Blooded'},
            'Supernatural Strength': {'Max':1,'Cost':10,'cat':'Bloodline','subcat':'Demon Blooded'}
        },
        'Dragon Blooded': {
            'Natural Armor': {'Max':1,'Cost':7,'cat':'Bloodline','subcat':'Dragon Blooded'},
            'Iron Stomach': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Dragon Blooded'},
            'Draconic Roar': {'Max':None,'Cost':4,'cat':'Bloodline','subcat':'Dragon Blooded'},
            'Bones of the Earth': {'Max':None,'Cost':8,'cat':'Bloodline','subcat':'Dragon Blooded'},
            'Supernatural Strength': {'Max':1,'Cost':10,'cat':'Bloodline','subcat':'Dragon Blooded'}
        },
        'Newborn Dream': {
            'Grasp of the Waking': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Newborn Dream'},
            'Method in Madness': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Newborn Dream'},
            'Drawn to the Muse': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Newborn Dream'},
            'Infinite Possibility': {'Max':1,'Cost':4,'cat':'Bloodline','subcat':'Newborn Dream'},
            'Slumber Sight': {'Max':None,'Cost':8,'cat':'Bloodline','subcat':'Newborn Dream'}
        }
    },
    'background': {
        'features': {
            'Magical Aptitude': {'Max':1,'Cost':4,'Reliant':['Mana Focus','Weapon Casting','Armored Casting'],'cat':'background','subcat':'features'},
            'Prophetic Dreamer': {'Max':1,'Cost':4,'cat':'background','subcat':'features'},
            'Nobility': {'Max':1,'Cost':6,'cat':'background','subcat':'features'},
            'Military Experience': {'Max':1,'Cost':4,'cat':'background','subcat':'features'},
            'Bardic Knowledge': {'Max':1,'Cost':4,'cat':'background','subcat':'features'},
            'Extra Native Lore': {'Max':1,'Cost':4,'cat':'background','subcat':'features'}
        },
        'flaws': {
            'Sovereign Zeal': {'Max':1,'Cost':-2,'cat':'background','subcat':'flaws'},
            'Religous Zeal': {'Max':1,'Cost':-2,'Prereq':{'Skill':'Religion','Check': lambda x: x != '','Desc':'special'},'cat':'background','subcat':'flaws'},
            'Corrupted': {'Max':None,'Cost':-6,'cat':'background','subcat':'flaws'},
            'Frail': {'Max':4,'Cost':-3,'cat':'background','subcat':'flaws'},
            'Illiterate': {'Max':1,'Cost':-4,'cat':'background','subcat':'flaws'},
            'Oatbound': {'Max':1,'Cost':-6,'cat':'background','subcat':'flaws'}
        },
        'memory flaws': {
            'Clouded Memory': {'Max':1,'Cost':-2,'cat':'background','subcat':'memory flaws'},
            'Fractued Memory': {'Max':1,'Cost':-4,'cat':'background','subcat':'memory flaws'},
            'Fading Memory': {'Max':1,'Cost':-4,'cat':'background','subcat':'memory flaws'}
        }
    },
    'basic': {
        'basic': {
            'Toughness': {'Max':5,'Cost':3,'Cells':{'Skill':'a17','Cost':'b17'},'cat':'basic','subcat':'basic'},
            'Mana Focus': {'Max':None,'Cost':1,'Cells':{'Skill':'a18','Cost':'b18'},'Prereq':{'Skill':'Magical Aptitude','Check':lambda x, y:(x in y),'Desc':'all'},'Reliant':['Internal Reserves'],'cat':'basic','subcat':'basic'},
            'Parry': {'Max':None,'Cost':4,'Cells':{'Skill':'a19','Cost':'b19'},'Reliant':['Tactical Lunge','Defensive Instruction'],'cat':'basic','subcat':'basic'},
            'Dodge': {'Max':None,'Cost':6,'Cells':{'Skill':'a20','Cost':'b20'},'Reliant':['Evasive Instruction','Dance Lesson'],'cat':'basic','subcat':'basic'},
            'Willpower': {'Max':None,'Cost':6,'Cells':{'Skill':'a21','Cost':'b21'},'Reliant':['Serenade'],'cat':'basic','subcat':'basic'}
        }
    }, 
    'General Skills':{
        'Weapon Proficiencies':{
            'Short Weapons':{
                'Max':1,
                'Cost':1,
                'Reliant':['One-Handed Weapons','Hidden Weapon'],
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            },
            'One-Handed Weapons':{
                'Max':1,
                'Cost':2,
                'Prereq':{
                    'Skill':('Short Weapons',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'Reliant':['Two-Handed Weapons'],
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            },
            'Two-Handed Weapons':{
                'Max':1,
                'Cost':3,
                'Prereq':{
                    'Skill':('One-Handed Weapons',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'Reliant':['Oversized Weapon Use','Break Shield'],
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            },
            'Oversized Weapon Use':{
                'Max':1,
                'Cost':2,
                'Prereq':{
                    'Skill':('Two-Handed Weapons',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            },
            'Thrown Weapons':{
                'Max':1,
                'Cost':2,
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            },
            'Bow and Arrow':{
                'Max':1,
                'Cost':3,
                'Reliant':['Precision'],
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            },
            'Two-Weapon Fighting':{
                'Max':1,
                'Cost':6,
                'cat':'General Skills',
                'subcat':'Weapon Proficiencies'
            }
        },  
        'Armor Proficiencies':{
            'Armor Training: Light':{
                'Max':1,
                'Cost':2,
                'Reliant':['Armor Training: Heavy'],
                'cat':'General Skills',
                'subcat':'Armor Proficiencies'
            },
            'Armor Training: Heavy':{
                'Max':1,
                'Cost':2,
                'Prereq':{
                    'Skill':('Armor Training: Light',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Armor Proficiencies'
            },
            'Shield Use':{
                'Max':1,
                'Cost':6,
                'cat':'General Skills',
                'subcat':'Armor Proficiencies'
            },
            'Helmet Mastery':{
                'Max':1,
                'Cost':6,
                'cat':'General Skills',
                'subcat':'Armor Proficiencies'
            }
        },
        'General Combat Skills':{
            'Guardian':{
                'Max':1,
                'Cost':4,
                'Prereq':{
                    'Skill':('Parry',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'General Combat Skills'
            },
            'Stamina Training':{
                'Max':1,
                'Cost':2,
                'Reliant':['Great Stamina'],
                'cat':'General Skills',
                'subcat':'General Combat Skills'
            },
            'Great Stamina':{
                'Max':1,
                'Cost':4,
                'Prereq':{
                    'Skill':('Stamina Training',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'General Combat Skills'
            },
            'Great Strike':{
                'Max':None,
                'Cost':3,
                'Reliant':['Tactial Lunge','Offensive Instruction','Blade Dance','Elemental Flourish'],
                'cat':'General Skills',
                'subcat':'General Combat Skills'
            },
            'Tactical Lunge':{
                'Max':1,
                'Cost':8,
                'Prereq':{
                    'Skill':('Great Strike','Parry',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'General Combat Skills'
            },
            'Stun':{
                'Max':None,
                'Cost':3,
                'Reliant':['Shin Kick','Sand in Your Eyes'],
                'cat':'General Skills',
                'subcat':'General Combat Skills'
            }
        },
        'Archery':{
            'Precision':{
                'Max':1,
                'Cost':7,
                'Prereq':{
                    'Skill':('Bow and Arrow',),
                    'Check': lambda x,y:any(i in y for i in x),
                    'Desc':'all'
                },
                'Reliant':['Master Precision','Disarming Shot','Pinning Shot','Repelling Shot'],
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'Master Precision':{
                'Max':1,
                'Cost':7,
                'Prereq':{
                    'Skill':('Precision',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'Reliant':['One Shot, One Kill','Volley','Faster Than the Eye'],
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'Disarming Shot':{
                'Max':None,
                'Cost':4,
                'Prereq':{
                    'Skill':('Precision',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'Pinning Shot':{
                'Max':None,
                'Cost':2,
                'Prereq':{
                    'Skill':('Precision',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'Repelling Shot':{
                'Max':None,
                'Cost':2,
                'Prereq':{
                    'Skill':('Pinning Shot',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'Reliant':['One Shot, One Kill'],
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'One Shot, One Kill':{
                'Max':None,
                'Cost':5,
                'Prereq':{
                    'Skill':('Master Precision','Repelling Shot'),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'Volley':{
                'Max':1,
                'Cost':10,
                'Prereq':{
                    'Skill':('Master Precision',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Archery'
            },
            'Faster Than the Eye':{
                'Max':1,
                'Cost':8,
                'Prereq':{
                    'Skill':('Master Precision','Stealth Attack'),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Archery'
            }
        },
        'Officer Training':{
            'Sudden Motivation': {
                'Max': None,
                'Cost': 1,
                'cat':'General Skills',
                'subcat':'Officer Training'
            },
            'Inspirational Speech': {
                'Max': None,
                'Cost': 2,
                'cat':'General Skills',
                'subcat':'Officer Training'
            },
            'Defensive Instruction': {
                'Max': None,
                'Cost': 4,
                'Prereq':{
                    'Skill':('Parry',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Officer Training'
            },
            'Evasive Instruction': {
                'Max': None,
                'Cost': 6,
                'Prereq':{
                    'Skill':('Dodge',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Officer Training'
            },
            'Offensive Instruction': {
                'Max': None,
                'Cost': 3,
                'Prereq':{
                    'Skill':('Great Strike',),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'Officer Training'
            },
            'Military Drill': {
                'Max': 1,
                'Cost': 10,
                'Prereq': {
                    'Skill': ['Defensive Instruction', 'Evasive Instruction', 'Offensive Instruction'],
                    'Check': lambda x, y: any(i in y for i in x),
                    'Desc': 'any'
                },
                'cat':'General Skills',
                'subcat':'Officer Training'
            },
            'Self-Observation': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Defensive Instruction', 'Evasive Instruction', 'Offensive Instruction'],
                    'Check': lambda x, y: any(i in y for i in x),
                    'Desc': 'any'
                },
                'cat':'General Skills',
                'subcat':'Officer Training'
            }
        },
        'The Art of Dueling':{
            'Disarm': {
                'Max': None,
                'Cost': 4,
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Feint': {
                'Max': None,
                'Cost': 1,
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Invoke Challenge': {
                'Max': 1,
                'Cost': 5,
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Salute': {
                'Max': 1,
                'Cost': 4,
                'Reliant':['Stylish Hat'],
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Stylish Hat': {
                'Max': 1,
                'Cost': 2,
                'Prereq':{
                    'Skill': ['Salute'],
                    'Check': lambda x, y: any(i in y for i in x),
                    'Desc': 'any'
                },
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Witty Repartee': {
                'Max': 1,
                'Cost': 7,
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Blade Dance': {
                'Max': 1,
                'Cost': 5,
                'Prereq': {
                    'Skill': ['Great Strike', 'Leap'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            },
            'Pure Of Heart': {
                'Max': 1,
                'Cost': 3,
                'cat':'General Skills',
                'subcat':'The Art of Dueling'
            }
        },
        'The School of Suffering':{
            'Armored Forearms': {
                'Max': 1,
                'Cost': 6,
                'Reliant':'Armored Shins',
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            },
            'Armored Shins': {
                'Max': 1,
                'Cost': 9,
                'Prereq': {
                    'Skill': ['Armored Forearms'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            },
            'Slow Bleeding': {
                'Max': 1,
                'Cost': 3,
                'Reliant':'Meditative Stillness',
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            },
            'Meditative Stillness': {
                'Max': 1,
                'Cost': 2,
                'Prereq': {
                    'Skill': ['Slow Bleeding'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':'Slow Death',
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            },
            'Slow Death': {
                'Max': 1,
                'Cost': 3,
                'Prereq': {
                    'Skill': ['Meditative Stillness'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            },
            'Torture Resistance': {
                'Max': None,
                'Cost': 3,
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            },
            'Torture Immunity': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': 'Torture Resistance',
                    'Needed':3,
                    'Check': lambda x,y: x>=y,
                    'Desc': 'x>y'
                },
                'Reliant':['Torture Resistance'],
                'cat':'General Skills',
                'subcat':'The School of Suffering'
            }
        },
        'The Assassins Arts':{
            'Stealth Attack': {
                'Max': 1,
                'Cost': 6,
                'Prereq': {
                    'Skill': ['Short Weapons', 'Thrown Weapons', 'Bow and Arrow'],
                    'Check': lambda x, y: any(i in y for i in x),
                    'Desc': 'any'
                },
                'Reliant':['Studied Killer','Twist the Knife','Deathly Vault'],
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            '10-Damage Strike': {
                'Max': None,
                'Cost': 8,
                'Prereq': {
                    'Skill': ['Short Weapons', 'Thrown Weapons', 'Bow and Arrow'],
                    'Check': lambda x, y: any(i in y for i in x),
                    'Desc': 'lambda x,y:any(i in y for i in x)'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Studied Killer': {
                'Max': 1,
                'Cost': 6,
                'Prereq': {
                    'Skill': ['Stealth Attack'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Twist the Knife': {
                'Max': 1,
                'Cost': 10,
                'Prereq': {
                    'Skill': ['Stealth Attack'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Shin Kick': {
                'Max': None,
                'Cost': 3,
                'Prereq': {
                    'Skill': ['Stun'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Sand in Your Eyes': {
                'Max': None,
                'Cost': 3,
                'Prereq': {
                    'Skill': ['Stun'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Hidden Weapon': {
                'Max': 1,
                'Cost': 3,
                'Prereq': {
                    'Skill': ['Short Weapons'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Leap': {
                'Max': None,
                'Cost': 2,
                'Reliant':['Blade Dance','Leap Attack','Deathly Vault'],
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Leap Attack': {
                'Max': None,
                'Cost': 3,
                'Prereq': {
                    'Skill': ['Leap'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Deathly Vault': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Stealth Attack', 'Leap'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            },
            'Rope Use': {
                'Max': 1,
                'Cost': 3,
                'cat':'General Skills',
                'subcat':'The Assassins Arts'
            }
        },
        'The Honored Path of the Berserker':{
            'Battle Rage': {
                'Max': None,
                'Cost': 7,
                'cat':'General Skills',
                'subcat':'The Honored Path of the Berserker'
            },
            'Enduring Rage': {
                'Max': 1,
                'Cost': 6,
                'cat':'General Skills',
                'subcat':'The Honored Path of the Berserker'
            },
            'Hatred': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Battle Rage'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Battle Rage'],
                'cat':'General Skills',
                'subcat':'The Honored Path of the Berserker'
            },
            'Berserker': {
                'Max': 1,
                'Cost': 10,
                'Prereq': {
                    'Skill': ['Hatred'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':'Hatred',
                'cat':'General Skills',
                'subcat':'The Honored Path of the Berserker'
            },
            'Break Limb': {
                'Max': None,
                'Cost': 5,
                'Reliant':'Break Shield',
                'cat':'General Skills',
                'subcat':'The Honored Path of the Berserker'
            },
            'Break Shield': {
                'Max': 1,
                'Cost': 5,
                'Prereq': {
                    'Skill': ['Break Limb', 'Two-Handed Weapons'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Honored Path of the Berserker'
            }
        },
        'Mundane Healing': {
            'Examine Wounds': {
                'Max': 1,
                'Cost': 2,
                'Reliant':['Detect Disease','Apply Pressure'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Detect Poison': {
                'Max': 1,
                'Cost': 2,
                'Prereq': {
                    'Skill': ['Examine Wounds'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Examine Wounds'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Administer Antidote': {
                'Max': None,
                'Cost': 2,
                'Prereq': {
                    'Skill': ['Detect Poison'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Detect Poison'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Detect Disease': {
                'Max': 1,
                'Cost': 2,
                'Prereq': {
                    'Skill': ['Examine Wounds'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Apply Pressure': {
                'Max': 1,
                'Cost': 1,
                'Prereq': {
                    'Skill': ['Examine Wounds'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Set Bone'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Set Bone': {
                'Max': 1,
                'Cost': 3,
                'Prereq': {
                    'Skill': ['Apply Pressure'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Bandage'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Bandage': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Set Bone'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Set Bone','Trauma Patch','Surgery'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Trauma Patch': {
                'Max': None,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Bandage'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Surgery': {
                'Max': 1,
                'Cost': 5,
                'Prereq': {
                    'Skill': ['Bandage', 'Lore: Anatomy'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'Reliant':['Battlefield Medicine'],
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            },
            'Battlefield Medicine': {
                'Max': 1,
                'Cost': 2,
                'Prereq': {
                    'Skill': ['Surgery'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Mundane Healing'
            }
        },
        'Religious Worship':{
            'Prayer':{
                'Max':1,
                'Cost':4,
                'Reliant':['Secondary Prayer','Priesthood'],
                'cat':'General Skills',
                'subcat':'Religious Worship'
            },
            'Secondary Prayer':{
                'Max':1,
                'Cost':4,
                'Prereq':{
                    'Skill':['Priesthood: Rank 2','Priesthood: Rank 3','Priesthood: Rank 4'],
                    'Check': lambda x,y:any(i in y for i in x)
                },
                'Reliant':['Tertiary Prayer'],
                'cat':'General Skills',
                'subcat':'Religious Worship'
            },
            'Tertiary Prayer':{
                'Max':1,
                'Cost':4,
                'Prereq':{
                    'Skill':['Secondary Prayer'],
                    'Check': lambda x,y:all(i in y for i in x)
                },
                'cat':'General Skills',
                'subcat':'Religious Worship'
            },
            'Repentance':{
                'Max':1,
                'Cost':2,
                'cat':'General Skills',
                'subcat':'Religious Worship'
            },
            'Priesthood':{
                'Max':4,
                'Cost':6,
                'Prereq':{
                    'Skill':['Prayer'],
                    'Check': lambda x,y: all(i in y for i in x)
                },
                'cat':'General Skills',
                'subcat':'Religious Worship'
            }
        },
        'The Bardic Arts': {
            'Commanding Presence': {
                'Max': None,
                'Cost': 3,
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'Serenade': {
                'Max': None,
                'Cost': 8,
                'Prereq': {
                    'Skill': ['Willpower'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'Dance Lesson': {
                'Max': None,
                'Cost': 8,
                'Prereq': {
                    'Skill': ['Dodge'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'True Greatness': {
                'Max': None,
                'Cost': 4,
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'Drinking Song': {
                'Max': 1,
                'Cost': 6,
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'Meditative Song': {
                'Max': 1,
                'Cost': 10,
                'Prereq': {
                    'Skill': ['Mana Focus'],
                    'Check': lambda x: x>=3,
                    'Desc': 'special'
                },
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'Hymn': {
                'Max': 1,
                'Cost': 2,
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            },
            'Requiem': {
                'Max': 1,
                'Cost': 3,
                'cat':'General Skills',
                'subcat':'The Bardic Arts'
            }
        },
        'The Magical Arts':{
            'Weapon Casting':{
                'Cost':8,
                'Max':1,
                'Prereq':{
                    'Skill':['Magical Aptitude'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'Reliant':['Combat Mimic'],
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Elemental Flourish':{
                'Cost':4,
                'Max':1,
                'Prereq':{
                    'Skill':('Sorcery','Great Strike'),
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Armored Casting':{
                'Cost':6,
                'MAx':1,
                'Prereq':{
                    'Skill':['Magical Aptitude'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Combat Mimic':{
                'Cost':4,
                'Max':None,
                'Prereq':{
                    'Skill':('Weapon Casting',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Internal Reserves':{
                'Cost':4,
                'Max':1,
                'Prereq':{
                    'Skill':'Mana Focus',
                    'Needed':10,
                    'Check':lambda x,y: x>=y,
                    'Desc':'x>y'
                },
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Arcane Tutelage':{
                'Cost':10,
                'Max':1,
                'Prereq':{
                    'Skill':'Aptitude',
                    'Check':lambda x: x is True,
                    'Desc':'Special'
                },
                'Reliant':['Arcane Observation'],
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Arcane Observation':{
                'Cost':4,
                'Prereq':{
                    'Skill':('Arcane Tutelage',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'all'
                },
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            },
            'Spellwright':{
                'Cost':2,
                'Max':1,
                'Prereq':{
                    'Skill':('Arcane Tutelage',),
                    'Check':lambda x, y: all(i in y for i in x),
                    'Desc':'Special'
                },
                'cat':'General Skills',
                'subcat':'The Magical Arts'
            }
        },
        'Skullduggery': {
            'Disguise': {
                'Max': 1,
                'Cost': 4,
                'Reliant':['Master Disguise'],
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Master Disguise': {
                'Max': 1,
                'Cost': 6,
                'Prereq': {
                    'Skill': ['Disguise'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Detect Disguise': {
                'Max': 1,
                'Cost': 4,
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Escape': {
                'Max': None,
                'Cost': 3,
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Poison Resistance': {
                'Max': None,
                'Cost': 2,
                'Reliant':['Poison Immunity'],
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Poison Immunity': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': 'Poison Resistance',
                    'Needed':3,
                    'Check': lambda x,y: x>=y,
                    'Desc': 'x>y'
                },
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Lockpicking: Apprentice': {
                'Max': 1,
                'Cost': 4,
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Lockpicking: Journeyman': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Lockpicking: Apprentice'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Lockpicking: Master': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Lockpicking: Journeyman'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Lockpicking: Grandmaster': {
                'Max': 1,
                'Cost': 4,
                'Prereq': {
                    'Skill': ['Lockpicking: Master'],
                    'Check': lambda x, y: all(i in y for i in x),
                    'Desc': 'all'
                },
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Gambling': {
                'Max': None,
                'Cost': 2,
                'cat':'General Skills',
                'subcat':'Skullduggery'
            },
            'Torture': {
                'Max': None,
                'Cost': 2,
                'cat':'General Skills',
                'subcat':'Skullduggery'
            }
        }
    },
    'Magical Arts':{
        'Magics':{
            'Magics':('Alchemy','Channeling','Divination','Sorcery','Warding','Dream Magic','Blood Magic',
                    'Necromancy','Summoning'),
            'Alchemy':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Alchemy',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Channeling':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Channeling',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Divination':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Divination',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Sorcery':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Sorcery',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Warding':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Warding',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Dream Magic':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Dream Magic',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Blood Magic':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Alchemy',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Necromancy':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Necromancy',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Summoning':{
                'cat':'Magical Arts',
                'subcat':'Magics',
                'Prereq':{
                    'Skill':'Lore: Summoning',
                    'Check': lambda x,y,z,m: x in y and z>=m,
                    'Desc':'Magic'
                }
            },
            'Levels':{
                'Lore':0,
                'Apprentice':1,
                'Journeyman':2,
                'Master':3,
                'Grandmaster':4
            },
            'Prereq':{
                lambda x,y:x==y}
            }
        },
    'Knowledge': {
        'History': {
            'Lore: War of Wine': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'History'},
            'Lore: Purges': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'History'},
            'Lore: The First Crusade': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'History'},
            'Lore: The War Of Radiance': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'History'},
            'Lore: The Second Crusade': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'History'},
            'Lore: The War of Giants': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'History'}
        },
        'Religion Lores': {
            'Lore: Church of Chorus': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: Old Ways': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: Dragon Worship': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: The Celestine Faith': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: The Lady of the Mists': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: The Nameless Faith': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: Trahazi Zodiac': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: The Blood Cauldron': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'},
            'Lore: Demon Faiths': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Religion Lores'}
        },
        'Creatures': {
            'Lore: Celestials': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Creatures'},
            'Lore: Demons': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Creatures'},
            'Lore: Fae': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Creatures'},
            'Lore: Dragons': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Creatures'},
            'Lore: Undead': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Creatures'}
        },
        'Magical Arts': {
            'Lore: Alchemy': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Blood Magic': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Channeling': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Divination': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Dream': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Necromancy': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Sorcery': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Summoning': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Warding': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'},
            'Lore: Rituals': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Magical Arts'}
        },
        'Misc': {
            'Lore: Anatomy': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Misc'},
            'Lore: Nature': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Misc'},
            'Lore: Medicine': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Misc'},
            'Lore: Rules of Society': {'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':'Misc'}
        },
        'Skills':{
            'Research':{'Max':1,'Cost':4,'cat':'Knowledge','subcat':'Skills'},
            'Alchemical Examination':{'Max':1,'Cost':3,'cat':'Knowledge','subcat':'Skills','Prereq': {
                    'Skill': ['Illiterate'],
                    'Check': lambda x, y: not any(i in y for i in x),
                    'Desc': 'any'
                }}
        }
    },
    'Crafting':{
        'Metalworking':{
            'Blacksmithing':{'cat':'Crafting','subcat':'Metalworking'},
            'Weaponsmithing':{'cat':'Crafting','subcat':'Metalworking'},
            'Armorsmithing':{'cat':'Crafting','subcat':'Metalworking'},
            'Shieldsmithing':{'cat':'Crafting','subcat':'Metalworking'},
            'Locksmithing':{'cat':'Crafting','subcat':'Metalworking'}
        },
        'Arcane':{
            'Enchanting':{'cat':'Crafting','subcat':'Arcane'},
            'Scroll Scribing':{'cat':'Crafting','subcat':'Arcane'},
            'Artificing':{'cat':'Crafting','subcat':'Arcane'}
        },
        'Edible':{
            'Cooking':{'cat':'Crafting','subcat':'Edible'},
            'Stable Alchemy':{'cat':'Crafting','subcat':'Edible'}
        },
        'Other':{
            'Tailoring':{'cat':'Crafting','subcat':'Other'},
            'Fletching':{'cat':'Crafting','subcat':'Other'},
            'Engineering':{'cat':'Crafting','subcat':'Other'}
        }
    },  
    'Gathering':{
        'gathering':{
            'Mining':{'cat':'Gathering','subcat':'gathering'},
            'Herbalism':{'cat':'Gathering','subcat':'gathering'},
            'Woodcutting':{'cat':'Gathering','subcat':'gathering'},
            'Hunting':{'cat':'Gathering','subcat':'gathering'},
            'Mercantile':{'cat':'Gathering','subcat':'gathering'},
            'Black Market':{'cat':'Gathering','subcat':'gathering'},
            'Academic Influence':{'cat':'Gathering','subcat':'gathering'},
            'Economic Influence':{'cat':'Gathering','subcat':'gathering'},
            'Military Influence':{'cat':'Gathering','subcat':'gathering'},
            'Political Influence':{'cat':'Gathering','subcat':'gathering'},
            'Underworld Influence':{'cat':'Gathering','subcat':'gathering'}
        }
    }
}

prefixdict={
    'Shield Fighter':{
        'details': {}, 
        'Bloodline': {}, 
        'background': {
            'features': {}, 
            'flaws': {
                'Illiterate': {'Quant': '1', 'Cost': '-4', 'Level': None, 'Cat': 'flaws'}}, 
                'memory flaws': {'Clouded Memory': {'Quant': '1', 'Cost': '-2', 'Level': None, 'Cat': 'memory flaws'}}
                }, 
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {'Quant': 1, 'Cost': '1', 'Level': None, 'Cat': 'Weapon Proficiencies'}, 
                'One-Handed Weapons': {'Quant': 1, 'Cost': '2', 'Level': None, 'Cat': 'Weapon Proficiencies'}}, 
            'Armor Proficiencies': {
                'Armor Training: Light': {'Quant': 1, 'Cost': '2', 'Level': None, 'Cat': 'Armor Proficiencies'}, 
                'Armor Training: Heavy': {'Quant': 1, 'Cost': '2', 'Level': None, 'Cat': 'Armor Proficiencies'}, 
                'Shield Use': {'Quant': 1, 'Cost': '6', 'Level': None, 'Cat': 'Armor Proficiencies'}}, 
        'General Combat Skills': {
            'Great Strike': {'Quant': 2, 'Cost': '3', 'Level': None, 'Cat': 'General Combat Skills'}}, 
            'Archery': {}, 
            'Officer Training': {}, 
            'The Art of Dueling': {}, 
            'The School of Suffering': {}, 
            'The Assassins Arts': {}, 
            'The Honored Path of the Berserker': {}, 
            'Mundane Healing': {}, 'Religious Worship': {}, 
            'The Bardic Arts': {}, 'The Magical Arts': {}, 
            'Skullduggery': {}}, 
        'basic': {
            'basic': {
                'Toughness': {'Quant': '3', 'Cost': 3, 'Level': None, 'Cat': 'basic'}, 
                'Parry': {'Quant': '3', 'Cost': 4, 'Level': None, 'Cat': 'basic'}, 
                'Dodge': {'Quant': '1', 'Cost': 6, 'Level': None, 'Cat': 'basic'}, 
                'Willpower': {'Quant': '1', 'Cost': 6, 'Level': None, 'Cat': 'basic'}}}, 
        'Magical Arts': {'Magics': {}}, 
        'Crafting': {'Arcane': {}, 'Metalworking': {}, 'Edible': {}, 'Other': {}}, 
        'Knowledge': {
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        }, 
        'Gathering': {'gathering': {}}
    },
    'Raging Barbarian':{
        'details': {}, 
        'Bloodline': {}, 
        'background': {
            'features': {}, 
            'flaws': {
                'Illiterate': {'Quant': '1', 'Cost': '-4', 'Level': None, 'Cat': 'flaws'},
                'Sovereign Zeal': {'Quant': '1', 'Cost': '-2', 'Level': None, 'Cat': 'flaws'}}, 
            'memory flaws': {'Clouded Memory': {'Quant': '1', 'Cost': '-2', 'Level': None, 'Cat': 'memory flaws'}}
                }, 
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {'Quant': 1, 'Cost': '1', 'Level': None, 'Cat': 'Weapon Proficiencies'}, 
                'One-Handed Weapons': {'Quant': 1, 'Cost': '2', 'Level': None, 'Cat': 'Weapon Proficiencies'},
                'Two-Weapon Fighting':{'Quant': 1, 'Cost': '6', 'Level': None, 'Cat': 'Weapon Proficiencies'}}, 
            'Armor Proficiencies': {
                'Armor Training: Light': {'Quant': 1, 'Cost': '2', 'Level': None, 'Cat': 'Armor Proficiencies'}}, 
            'General Combat Skills': {}, 
            'Archery': {}, 
            'Officer Training': {}, 
            'The Art of Dueling': {}, 
            'The School of Suffering': {}, 
            'The Assassins Arts': {
                'Leap':{'Quant':1,'Cost':'2','Level':None,'Cat':'The Assassins Arts'}
            }, 
            'The Honored Path of the Berserker': {
                'Battle Rage':{'Quant':3,'Cost':'7','Level':None,'Cat':'The Honored Path of the Berserker'},
                'Enduring Rage':{'Quant':1,'Cost':'6','Level':None,'Cat':'The Honored Path of the Berserker'},
                'Break Limb':{'Quant':1,'Cost':'5','Level':None,'Cat':'The Honored Path of the Berserker'}
            }, 
            'Mundane Healing': {}, 'Religious Worship': {}, 
            'The Bardic Arts': {}, 'The Magical Arts': {}, 
            'Skullduggery': {}}, 
        'basic': {
            'basic': {
                'Toughness': {'Quant': '3', 'Cost': 3, 'Level': None, 'Cat': 'basic'}}}, 
        'Magical Arts': {'Magics': {}}, 
        'Crafting': {'Arcane': {}, 'Metalworking': {}, 'Edible': {}, 'Other': {}}, 
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        }, 
        'Gathering': {'gathering': {}}        
    },
    'Knife-Wielding Assassin':{
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {
                'Illiterate': {
                    'Quant': '1',
                    'Cost': '-4',
                    'Level': None,
                    'Cat': 'flaws'
                }
            },
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {
                    'Quant': 1,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                }
            },
            'Armor Proficiencies': {},
            'General Combat Skills': {
                'Stun': {
                    'Quant': 1,
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                }
            },
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {
                'Disarm': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                }
            },
            'The School of Suffering': {
                'Armored Forearms': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The School of Suffering'
                }
            },
            'The Assassins Arts': {
                'Stealth Attack': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The Assassins Arts'
                },
                '10-Damage Strike': {
                    'Quant': 3,
                    'Cost': '8',
                    'Level': None,
                    'Cat': 'The Assassins Arts'
                },
                'Leap': {
                    'Quant': 1,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'The Assassins Arts'
                }
            },
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {},
            'Religious Worship': {},
            'The Bardic Arts': {},
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {}
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        },
                'Gathering': {
            'gathering': {}
        }
    },
    'Stylish Duelist':{
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {},
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {
                    'Quant': 1,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                },
                'One-Handed Weapons': {
                    'Quant': 1,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                }
            },
            'Armor Proficiencies': {},
            'General Combat Skills': {
                'Parry': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                },
                'Dodge': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                }
            },
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {
                'Salute': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                },
                'Stylish Hat': {
                    'Quant': 1,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                },
                'Witty Repartee': {
                    'Quant': 1,
                    'Cost': '7',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                },
                'Disarm': {
                    'Quant': 2,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                }
            },
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {},
            'Religious Worship': {},
            'The Bardic Arts': {
                'Dance Lesson': {
                    'Quant': 1,
                    'Cost': '8',
                    'Level': None,
                    'Cat': 'The Bardic Arts'
                }
            },
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {}
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        },
        'Gathering': {
            'gathering': {}
        }
    },
    'Wandering Monk':{
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                },
                'Bardic Knowledge': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {
                'Illiterate': {
                    'Quant': '1',
                    'Cost': '-4',
                    'Level': None,
                    'Cat': 'flaws'
                }
            },
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {
                    'Quant': 1,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                },
                'One-Handed Weapons': {
                    'Quant': 1,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                }
            },
            'Armor Proficiencies': {},
            'General Combat Skills': {
                'Parry': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                },
                'Willpower': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                }
            },
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {},
            'The School of Suffering': {
                'Armored Forearms': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The School of Suffering'
                }
            },
            'The Assassins Arts': {
                'Leap': {
                    'Quant': 2,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'The Assassins Arts'
                }
            },
            'The Honored Path of the Berserker': {
                'Break Limb': {
                    'Quant': 1,
                    'Cost': '5',
                    'Level': None,
                    'Cat': 'The Honored Path of the Berserker'
                }
            },
            'Mundane Healing': {
                'Examine Wounds': {
                    'Quant': 1,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Apply Pressure': {
                    'Quant': 1,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Set Bone': {
                    'Quant': 1,
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Bandage': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                }
            },
            'Religious Worship': {
                'Prayer': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Religious Worship'
                }
            },
            'The Bardic Arts': {},
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {}
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        },
        'Gathering': {
            'gathering': {}
        }
    },
    'Combat Healer': {
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                },
                'Magical Aptitude': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {},
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {},
            'Armor Proficiencies': {},
            'General Combat Skills': {},
            'Archery': {},
            'Officer Training': {
                'Sudden Motivation': {
                    'Quant': 2,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Officer Training'
                }
            },
            'The Art of Dueling': {},
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {
                'Examine Wounds': {
                    'Quant': 1,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Apply Pressure': {
                    'Quant': 1,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Set Bone': {
                    'Quant': 1,
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Bandage': {
                    'Quant': 1,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                }
            },
            'Religious Worship': {},
            'The Bardic Arts': {},
            'The Magical Arts': {
                'Mana Focus': {
                    'Quant': 10,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'The Magical Arts'
                },
                'Apprentice Magic: Channeling': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The Magical Arts'
                },
                'Journeyman Magic: Channeling': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The Magical Arts'
                },
                'Apprentice Magic: Alchemy': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The Magical Arts'
                },
                'Journeyman Magic: Alchemy': {
                    'Quant': 1,
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'The Magical Arts'
                }
            },
            'Skullduggery': {}
        },
        'basic': {
            'basic': {}
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        },
        'Gathering': {
            'gathering': {}
        }
    },
    'Master Sorceror':{
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                },
                'Magical Aptitude': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {},
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {},
            'Armor Proficiencies': {},
            'General Combat Skills': {},
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {},
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {},
            'Religious Worship': {},
            'The Bardic Arts': {},
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {
                'Mana Focus': {
                    'Quant': 16,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'basic'
                }
            }
        },
        'Magical Arts': {
            'Magics': {
                'Master Magic: Sorcery': {
                    'Quant': 1,
                    'Cost': '18',
                    'Level': None,
                    'Cat': 'Magics'
                }
            }
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {
                'Lore: Sorcery':{'Quant':1,'Cost':4,'Level':None,'Cat':'Knowledge'}
            },
            'Misc': {},
            'Skills': {}
        },
        'Gathering': {
            'gathering': {}
        }
    },
    'Practiced Surgeon':{
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {},
            'flaws': {},
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {},
            'Armor Proficiencies': {},
            'General Combat Skills': {},
            'Archery': {},
            'Officer Training': {
                'Sudden Motivation': {
                    'Quant': 3,
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Officer Training'
                }
            },
            'The Art of Dueling': {},
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {
                'Examine Wounds': {
                    'Quant': '1',
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Detect Poison': {
                    'Quant': '1',
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Apply Pressure': {
                    'Quant': '1',
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Set Bone': {
                    'Quant': '1',
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Administer Antidote': {
                    'Quant': 2,
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Bandage': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Trauma Patch': {
                    'Quant': 2,
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                },
                'Surgery': {
                    'Quant': '1',
                    'Cost': '5',
                    'Level': None,
                    'Cat': 'Mundane Healing'
                }
            },
            'Religious Worship': {},
            'The Bardic Arts': {},
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {
                'Willpower': {
                    'Quant': '1',
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'basic'
                }
            }
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': {
            'Native Lore':{},
            'History':{}, 
            'Religion Lores':{}, 
            'Creatures':{}, 
            'Magical Arts':{}, 
            'Misc':{
                'Lore: Anatomy': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Knowledge'
                }
            }
        },
        'Gathering': {
            'gathering': {}
        }
    },
    'Charismatic Courtier':{
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                },
                'Nobility': {
                    'Quant': '1',
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {
                'Oath Bound': {
                    'Quant': '1',
                    'Cost': '-6',
                    'Level': None,
                    'Cat': 'flaws'
                }
            },
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {
                    'Quant': '1',
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                },
                'One-Handed Weapons': {
                    'Quant': '1',
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                }
            },
            'Armor Proficiencies': {},
            'General Combat Skills': {
                'Dodge': {
                    'Quant': '1',
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                }
            },
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {
                'Salute': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                },
                'Witty Repartee': {
                    'Quant': '1',
                    'Cost': '7',
                    'Level': None,
                    'Cat': 'The Art of Dueling'
                }
            },
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {},
            'Religious Worship': {},
            'The Bardic Arts': {
                'Dance Lesson': {
                    'Quant': '1',
                    'Cost': '8',
                    'Level': None,
                    'Cat': 'The Bardic Arts'
                },
                'Serenade': {
                    'Quant': '1',
                    'Cost': '8',
                    'Level': None,
                    'Cat': 'The Bardic Arts'
                }
            },
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {
                'Willpower': {
                    'Quant': '1',
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'basic'
                }
            }
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        },
        'Gathering': {
            'gathering': {}
        }
    },
    'Alchemical Merchant': {
        'details': {},
        'Bloodline': {},
        'background': {
            'features': {
                'Native Lore: [Your Home Nation]': {
                    'Quant': '1',
                    'Cost': '0',
                    'Level': None,
                    'Cat': 'features'
                }
            },
            'flaws': {},
            'memory flaws': {
                'Clouded Memory': {
                    'Quant': '1',
                    'Cost': '-2',
                    'Level': None,
                    'Cat': 'memory flaws'
                }
            }
        },
        'General Skills': {
            'Weapon Proficiencies': {},
            'Armor Proficiencies': {},
            'General Combat Skills': {},
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {},
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {},
            'Religious Worship': {},
            'The Bardic Arts': {},
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {}
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {
                'Stable Alchemy': {
                    'Quant': '1',
                    'Cost': '18',
                    'Level': 'Master',
                    'Cat': 'Edible'
                }
            },
            'Other': {}
        },
        'Knowledge': { 
            'History': {},
            'Religion Lores': {},
            'Creatures': {},
            'Magical Arts': {},
            'Misc': {},
            'Skills': {}
        },
        'Gathering': {
            'gathering': {
                'Herbalism': {
                    'Quant': '4',
                    'Cost': '16',
                    'Level': None,
                    'Cat': 'gathering'
                },
                'Mercantile': {
                    'Quant': '2',
                    'Cost': '8',
                    'Level': None,
                    'Cat': 'gathering'
                }
            }
        }
    },
    'Dream of Infinite Possibility':{
        'details': {},
        'Bloodline': {
            'Newborn Dream': {
                'Infinite Possibility': {
                    'Quant': '1',
                    'Cost': '4',
                    'Level': None,
                    'Cat': 'Restricted Newborn Dream Skills'
                },
                'Drawn to the Muse': {
                    'Quant': '1',
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'Restricted Newborn Dream Skills'
                },
                'Slumber Sight': {
                    'Quant': '1',
                    'Cost': '8',
                    'Level': None,
                    'Cat': 'Restricted Newborn Dream Skills'
                }
            }
        },
        'background': {
            'features': {},
            'flaws': {
                'Tethered': {
                    'Quant': '1',
                    'Cost': '-10',
                    'Level': None,
                    'Cat': 'flaws'
                }
            },
            'memory flaws': {}
        },
        'General Skills': {
            'Weapon Proficiencies': {
                'Short Weapons': {
                    'Quant': '1',
                    'Cost': '1',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                },
                'One-Handed Weapons': {
                    'Quant': '1',
                    'Cost': '2',
                    'Level': None,
                    'Cat': 'Weapon Proficiencies'
                }
            },
            'Armor Proficiencies': {},
            'General Combat Skills': {
                'Stun': {
                    'Quant': '1',
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'General Combat Skills'
                }
            },
            'Archery': {},
            'Officer Training': {},
            'The Art of Dueling': {},
            'The School of Suffering': {},
            'The Assassins Arts': {},
            'The Honored Path of the Berserker': {},
            'Mundane Healing': {},
            'Religious Worship': {},
            'The Bardic Arts': {},
            'The Magical Arts': {},
            'Skullduggery': {}
        },
        'basic': {
            'basic': {
                'Toughness': {
                    'Quant': '1',
                    'Cost': '3',
                    'Level': None,
                    'Cat': 'basic'
                },
                'Dodge': {
                    'Quant': '1',
                    'Cost': '6',
                    'Level': None,
                    'Cat': 'basic'
                }
            }
        },
        'Magical Arts': {
            'Magics': {}
        },
        'Crafting': {
            'Arcane': {},
            'Metalworking': {},
            'Edible': {},
            'Other': {}
        },
        'Knowledge': {
            'ores': {}
        },
        'Gathering': {
            'gathering': {}
        }
    }
}