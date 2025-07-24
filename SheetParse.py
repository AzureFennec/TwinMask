import pandas as pd
import re
from SkillsDict import skills

class NoCharacterSheet(Exception):
    pass
class CannotParseSheet(Exception):
    pass

bloodlineprocessing=False

export={
    'details': {},
    'Bloodline': {},
    'background': {
        'features': {},
        'flaws': {},
        'memory flaws': {}
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
        'Skullduggery': {},
        'Knowledge':{}
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
        'Native Lore':{},
        'History':{}, 
        'Religion Lores':{}, 
        'Creatures':{}, 
        'Magical Arts':{}, 
        'Misc':{},
        'Skills':{}
    },
    'Gathering': {
        'gathering': {}
    },
    'Postage':{
        'Local':None,
        'Oversea':None
    }
}

cats={
    'Bloodline':{
        'Start':0,
        'End':6,
        'Next':'General Skills'
    },
    'General Skills':{
        'Start':11,
        'End':18,
        'Next':'Magical Arts'
    },
    'Magical Arts':{
        'Start':27,
        'End':50,
        'Next':'Background'
    },
    'Background':{
        'Start':3,
        'End':1,
        'Next':'Knowledge'
    },
    'Knowledge':{
        'Start':1,
        'End':2,
        'Next':'Crafting/Gathering'
    },
    'Crafting/Gathering':{
        'Start':1,
        'End':2
    }
}

def BuildExport(df):
    for skill in df:
        ref=df[skill]
        export[ref['cat']][ref['subcat']][skill]={'Quant':ref['Quant'],'Cost':ref['Cost'],'Level':ref['Level'],'Cat':ref['cat']}

def BuildDF(df):
    dflist=[]
    for cat in cats:
        start=cats[cat]['Start']+1
        end=cats[cat]['End']
        catdf=df.iloc[start:end].copy()
        catdf['cat']=cat
        catdf.reset_index(drop=True,inplace=True)
        if cat=='General Skills':
            for i in range(1,6):
                catdf.reset_index(drop=True,inplace=True)
                catdf.iloc[i-1,2]='basic'
        if cat=='Crafting/Gathering':
            for i in range(len(catdf)):
                if re.search(r'Rank', catdf.iloc[i-1,0]):
                    catdf.iloc[i-1,2]='Gathering'
                else:
                    catdf.iloc[i-1,2]='Crafting'
        
        dflist.append(catdf)
    choicedf=pd.concat(dflist)
    choicedf.reset_index(drop=True,inplace=True)

    CleanDF(choicedf)
        
def CleanDF(df):
    df = df.dropna(subset=[df.columns[0]])
    df = df.dropna(subset=[df.columns[1]])
    BuildDic(df)

def BuildDic(df):
    df['subcat']=None
    
    for index, row in df.iterrows():
        skill = row.iloc[0]
        cost = row.iloc[1]
        cat=row.iloc[2]

        if re.search(r'x\d+', skill):
            parts=skill.split('x')
            
            name=parts[0].strip()
            quant=parts[1]
        else:
            name=skill
            quant=1

        if ':' in skill and cat!='Knowledge':
            parts=skill.split(':')
            name=parts[0].strip()
            level=parts[1].strip()
        else:
            level=None

        if cat=='Background':
            cat='background'

        for subcat in skills[cat]:
            bloodlineprocessing=False
            if name in skills[cat][subcat]:
                subcat=skills[cat][subcat][name]['subcat']
                exportdict[name]={'Quant':quant,'Cost':cost,'Level':level,'cat':cat,'subcat':subcat}
                if cat=='Bloodline':
                    bloodlineprocessing=True

    BuildExport(exportdict)
        
def SetLocations(df):
    catlist=list(cats.keys())

    for cat in catlist: # start values must be set before setting end values since end values are based on start values
        try:
            start=df.index.get_loc(df.index[df.iloc[:,0] == cat][0])
        except IndexError:
            raise CannotParseSheet
        cats[cat]['Start']=start
    
    for cat in catlist:
        if cat!='Crafting/Gathering':
            cats[cat]['End']=cats[cats[cat]['Next']]['Start']
        else:
            cats[cat]['End']=len(df)

    BuildDF(df)

def ExtractDetails(df):
    storage=export['details']
    storage['Player']=df.iloc[0,1]
    storage['Email']=df.iloc[1,1]
    storage['Culture']=df.iloc[2,1]
    storage['Religion']=df.iloc[3,1]
    storage['Character']=df.iloc[0,5]
    storage['Bloodline']=df.iloc[1,5]
    export['Bloodline'][df.iloc[1,5]]={}
    try:
        try:
            export['Postage']['Local']=int(df.iloc[13,7])
        except ValueError:
            export['Postage']['Local']=0
        try:
            export['Postage']['Oversea']=int(df.iloc[14,7])
        except ValueError:
            export['Postage']['Oversea']=0
    except IndexError:
        export['Postage']['Local']=0
        export['Postage']['Oversea']=0

def BuildChar(file):

    try:
        df=pd.read_excel(file,sheet_name='Character')
    except ValueError:
        raise NoCharacterSheet

    ExtractDetails(df)

    df.drop([0,1,2,3,4,5,6],inplace=True)

    df.reset_index(drop=True,inplace=True)

    leftdf=df.iloc[0:,0:2]

    rightdf=df.iloc[0:,4:6]

    dfs=[leftdf,rightdf]

    for df in dfs:
        namecol=df.columns[0]
        costcol=df.columns[1]
        df.rename(columns={namecol:'Skill',costcol:'Cost'},inplace=True)

    df=pd.concat(dfs)

    df = df.dropna(subset=[df.columns[0]])
    df.reset_index(drop=True,inplace=True)

    SetLocations(df)

    global export
    return export

exportdict={}