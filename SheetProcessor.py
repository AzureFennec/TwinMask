from datetime import date
from SheetBuilder import newcreatesheet
from datetime import date
from SkillsDict import skills

choices={
    'details':{'bloodline':'Fae Blooded'},
    'Bloodline':{},
    'background':{},
    'basic':{},
    'General Skills':{},
    'Magical Arts':{},
    'Crafting':{},
    'Knowledge':{},
    'Gathering':{},
    'Postage':{
        'Local':0,
        'Oversea':0
    }
}


craftinglevels={
    1:'Apprentice',
    2:'Journeyman',
    3:'Master',
    4:'Grandmaster'
}

def process_choices(dict,filepath):
    choices={
        'details':{},
        'Bloodline':{},
        'background':{},
        'basic':{},
        'General Skills':{},
        'Magical Arts':{},
        'Crafting':{},
        'Knowledge':{},
        'Gathering':{},
        'Postage':{
            'Local':0,
            'Oversea':0
        }
    }
    
    for cat in dict:
        if cat=='details':
            dict_=choices['details']
            dict_['name']=dict['details']['Player']
            dict_['email']=dict['details']['Email']
            dict_['Culture']=dict['details']['Culture']
            dict_['Religion']=dict['details']['Religion']
            dict_['Character']=dict['details']['Character']
            dict_['bloodline']=dict['details']['Bloodline']

        elif cat in ('Magical Arts','Crafting'): # issue is happening here
            for type in dict[cat]:
                for skill in dict[cat][type]:
                    name=f'{skill}: {dict[cat][type][skill]['Level']}'
                    choices[cat][name]=dict[cat][type][skill]['Cost']

        elif cat in ('Bloodline','basic'):
            if cat=='Bloodline':
                bloodline=dict['details']['Bloodline']
                for skill in skills['Bloodline'][bloodline]:
                    skillref=skills['Bloodline'][bloodline][skill]
                    if skillref['Max'] is None or skillref['Max']>1:
                        try:
                            name=f'{skill} x{dict['Bloodline'][bloodline][skill]['Quant']}'
                            cost=dict['Bloodline'][bloodline][skill]['Cost']
                        except KeyError:
                            name=f'{skill} x0'
                            cost='N/A'
                    else:
                        name=skill
                        try:
                            cost=dict['Bloodline'][bloodline][skill]['Cost']
                        except KeyError:
                            cost='N/A'
                    choices['Bloodline'][name]=cost

            if cat=='basic':
                for skill in skills['basic']['basic']:
                    try:
                        name=f'{skill} x{dict['basic']['basic'][skill]['Quant']}'
                        cost=int(dict['basic']['basic'][skill]['Quant'])*dict['basic']['basic'][skill]['Cost']
                    except:
                        name=f'{skill} x0'
                        cost='N/A'
                    choices['basic'][name]=cost
        
        elif cat=='Gathering':
            dict_=dict[cat]['gathering']
            for skill in dict_:
                reference=dict_[skill]
                name=f'{skill}: Rank {reference['Quant']}'
                cost=reference['Cost']
                choices['Gathering'][name]=cost

        else:
            for type in dict[cat]:
                if cat=='Postage':
                    choices['Postage'][type]=dict[cat][type]
                    continue
                dict_=dict[cat][type]
                for skill in dict_:
                    if int(dict_[skill]['Quant'])>1:
                        name=f'{skill} x{dict_[skill]['Quant']}'
                    else:
                        name=skill
                    cost=int(dict_[skill]['Cost'])
                    choices[cat][name]=cost

    newcreatesheet(choices,filepath)