import tkinter as tk
from tkinter import ttk
from SkillsDict import skills, prefixdict
from SheetProcessor import process_choices
from functools import partial
from SheetParse import BuildChar, NoCharacterSheet, CannotParseSheet
from tkinter import filedialog

LARGEFONT = ("Verdana", 35)

class Character:
    def __init__(self, name, email, culture, religion, character, bloodline):
        self.name = name
        self.email = email
        self.culture = culture
        self.religion = religion
        self.character = character
        self.bloodline = bloodline

    def __str__(self):
        return f"Character(name={self.name}, email={self.email}, culture={self.culture}, religion={self.religion}, character={self.character}, bloodline={self.bloodline})"

class SkillChoice:
    def __init__(self, skill, cost, cat, page, quantity=1,  level=None) : # page is the class context, and should correspond to a key of the choices dictionary(background, General Skills, etc.). Cat is used for when page has nested dictionaries.
        self.skill = skill
        self.cost = cost
        self.quant = quantity
        self.cat=cat
        self.level=level
        self.page=page

class DisplayGrid:
    def __init__(self,row,column):
        self.row=row
        self.column=column

choices={
    'details':{},
    'Bloodline':{},
    'background':{
        'features':{},
        'flaws':{},
        'memory flaws':{}
    },
    'General Skills':{
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
    'basic':{
        'basic':{}
    },
    'Magical Arts':{
        'Magics':{}
    },
    'Crafting':{
        'Arcane':{},
        'Metalworking':{},
        'Edible':{},
        'Other':{}
    },
    'Knowledge':{
        'Native Lore':{},
        'History':{}, 
        'Religion Lores':{}, 
        'Creatures':{}, 
        'Magical Arts':{}, 
        'Misc':{},
        'Skills':{}
    },
    'Gathering':{
        'gathering':{}
    }
}

allchoices={}

levels={
    'Lore':0,
    'Apprentice':1,
    'Journeyman':2,
    'Master':3,
    'Grandmaster':4
}

def ValidateSelection(self,choice): # passes two class instances- self(for managing pre-existing lists) and choice(for trackign details of the specifc choice that was made)
    if int(choice.quant)>0: # checks to make sure quantity is at least 1, to avoid processing choices with zero quantity
        if choice.skill in allchoices: # checks if the skill has already been added
            message=f'You have already added {choice.skill}'
            ErrorPopup(self,message)
        else:
            TestSelection(self,choice)
    else:
        message='You must select at least one use.'
        ErrorPopup(self,message)

def TestSelection(self,choice): # checks if there are prerequisites for the chosen skill, rejects in case of failure
    skillref=skills[choice.page][choice.cat][choice.skill]
    if choice.cat=='memory flaws':
        if choices['background']['memory flaws']=={}:
            pass
        else:
            ErrorPopup(self,message='You can only select one memory flaw.')
            return
    if 'Prereq' in skillref.keys():
        prereqdict=skillref['Prereq']
        print(prereqdict)
        if prereqdict['Desc']=='all':
            if prereqdict['Check'](prereqdict['Skill'],allchoices) is True:
                BuildSelection(self,choice)
            else:
                message=f'In order to add {choice.skill} you must have all of the following: {prereqdict['Skill']}.'
                ErrorPopup(self, message)

        elif prereqdict['Desc']=='any': # sepperated from the other lambda- even though the x/y pairs are identical, the error popup is different
            # you can change this to process both any and all in one block and condition the messages- I prefer to do it this way.
            if prereqdict['Check'](prereqdict['Skill'],choices['General Skills']) is True:
                BuildSelection(self,choice)
            else:
                message=f'In order to add {choice.skill} you must add one of the following: {prereqdict['Skill']}'
                ErrorPopup(self, message)
        
        elif prereqdict['Desc']=='x>y':
            try: # Protect against KeyError: if the prerequisite skill has not been added at all, accessing it will raise an error.
                if prereqdict['Check'](int(allchoices[prereqdict['Skill']]['Quant']),prereqdict['Needed']) is True:
                    BuildSelection(self,choice)
                else:
                    message=f'You cannot add {choice.skill}. You must have at least {prereqdict['Needed']} uses of {prereqdict['Skill']}'
                    ErrorPopup(self, message)
            except KeyError:
                message=f'You cannot add {choice.skill}. You must have at least {prereqdict['Needed']} uses of {prereqdict['Skill']}'
                ErrorPopup(self, message)
    
        elif prereqdict['Desc']=='Magic':
            try:
                if prereqdict['Check'](prereqdict['Skill'],allchoices,int(allchoices['Mana Focus']['Quant']),int(levels[choice.level]*5)) is True:
                    BuildSelection(self,choice)
                else:
                    message=f'You cannot add {choice.skill}. You  must first add {prereqdict['Skill']} and at least {levels[choice.level]*5} mana.'
                    ErrorPopup(self, message)
            except KeyError:
                message=f'You cannot add {choice.skill}. You  must first add {prereqdict['Skill']} and at least {levels[choice.level]*5} mana.'
                ErrorPopup(self, message)
        
        elif prereqdict['Desc']=='special':
            if choice.skill == 'Religous Zeal':
                if choices['details']['Religion'] is not None:
                    BuildSelection(self,choice)
                else:
                    message='You must have a religion to take Religous Zeal.'
                    ErrorPopup(self,message)
            else:
                ErrorPopup(self,message='Error- special test was set but no prereq test is detected.')

        elif prereqdict['Desc']=='NBD':
            if prereqdict['Check'](choices['details']['Bloodline']) is True:
                BuildSelection(self, choice)
            else:
                ErrorPopup(self,message=f'Newborn Dreams cannot take {choice.skill}')
        else: 
            ErrorPopup(self,message='Error- prereq was set but no prereq test is detected.')
    else:
        BuildSelection(self,choice)

def BuildSelection(self,choice): # builds a dictionary to track the values of the skill. the finalized version of the skill will be generated elsewhere.
    savedict={'Quant':choice.quant,'Cost':choice.cost, 'Level':choice.level} # saving it this way makes it easier to reference when testing prereq conditions
    choices[self.page][choice.cat][choice.skill]=savedict
    print(savedict)
    allchoices[choice.skill]=savedict # two sepparate dicts- choices is used to group for exporting, allchoices is used for

def DisplaySelection(window, row, column):
    dict_data = choices[window.page]

    # Use scrollable_frame only if page is 'General Skills'
    if window.page == 'General Skills' and hasattr(window, 'scrollable_frame'):
        parent = window.scrollable_frame
    else:
        parent = window

    startrow = row
    startcol = column

    # Initialize widget storage if not exists
    if not hasattr(window, 'selection_widgets') or not isinstance(window.selection_widgets, dict):
        window.selection_widgets = {}

    # Clear previous widgets
    for widgets in window.selection_widgets.values():
        for w in widgets:
            w.destroy()
    window.selection_widgets.clear()

    maxrow = startrow

    for cat in dict_data:
        row = startrow + 1
        if dict_data[cat] != {}:
            catheader = ttk.Label(parent, text=cat, font=("Arial", 10, "bold"), anchor="center", justify="center")
            catheader.grid(row=row, column=column, columnspan=4, padx=10, pady=10, sticky="ew")

            row += 1
        else:
            continue

        for skill in dict_data[cat]:
            if dict_data[cat][skill]['Quant'] == '':
                continue

            skilllabel = ttk.Label(parent, text=skill)
            skilllabel.grid(row=row, column=column, columnspan=1, padx=10, pady=10)

            quantlabel = ttk.Label(parent, text=dict_data[cat][skill]['Quant'])
            quantlabel.grid(row=row, column=column + 1, columnspan=1, padx=10, pady=10)

            # Handle invalid cost gracefully
            cost_str = dict_data[cat][skill]['Cost']
            try:
                cost = int(cost_str)
            except (ValueError, TypeError):
                cost = 0

            costlabel = ttk.Label(parent, text=cost)
            costlabel.grid(row=row, column=column + 2, columnspan=1, padx=10, pady=10)
            if skill!='Tethered':
                remove_button = ttk.Button(
                    parent,
                    text="Remove",
                    command=partial(RemoveSelection, window, skill, cat)
                )
                remove_button.grid(row=row, column=column + 5, padx=10, pady=10)
            else:
                remove_button = ttk.Button(
                    parent,
                    text="Remove",
                    command=partial(RemoveSelection, window, skill, cat)
                )

            window.selection_widgets[skill] = [skilllabel, quantlabel, costlabel, remove_button]

            row += 1
            if row > maxrow:
                maxrow = row

        column += 6
        if column >= startcol + 18:
            column = startcol
            startrow = maxrow + 1

def RemoveSelection(self, skill, cat):
    if 'Reliant' in skills[self.page][cat][skill]:
        for skill_ in skills[self.page][cat][skill]['Reliant']:
            if skill_ in allchoices:
                message=f'You cannot remove {skill} until you remove {skill_}'
                ErrorPopup(self,message)
                return

    del choices[self.page][cat][skill]
    del allchoices[skill]

    if hasattr(self, 'selection_widgets') and skill in self.selection_widgets:
        for widget in self.selection_widgets[skill]:
            widget.destroy()
        del self.selection_widgets[skill]

def ErrorPopup(self,message):
    error_window = tk.Toplevel(self)
    error_window.title("Missing Information")
    error_label = tk.Label(error_window, text=message, font=("Arial", 12), fg="red")
    error_label.pack(padx=10, pady=10)
    ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
    ok_button.pack(pady=(0, 10))

def ImportChara(dict):
        choices.clear()
        choices.update(dict)
        allchoices.clear()
        for cat in choices:
            if cat!='details':
                for subcat in choices[cat]:
                    if cat=='Postage':
                        continue
                    for skill in choices[cat][subcat]:
                        allchoices[skill]=choices[cat][subcat][skill]

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        container=tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}
        self.character=None
        self.allchoices=allchoices
        self.container=container  # save to use later in dynamic init

        self.nav_pages=[
            ChooseBackground, ChooseBasics, ChooseRacial, ChooseSkills,
            AddMagic, AddCrafting, AddGathering, AddKnowledge, ReviewChoices
        ]
        self.navbar=None
        self.nav_initialized=False

        self.start_pages=[StartPage, NewCharacter, LoadCharacter, ChoosePrefix]

        for F in self.start_pages:
            frame=F(container, self)

            if F in [NewCharacter, LoadCharacter, ChoosePrefix]:
                back_btn=tk.Button(frame, text="Back", command=lambda: self.show_frame(StartPage))
                back_btn.grid(row=0, column=0, sticky="w", padx=5, pady=5)

            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        self.protocol("WM_DELETE_WINDOW", self.conclude)

    def initialize_nav_pages(self):
        if self.nav_initialized:
            return
        self.nav_initialized=True

        for F in self.nav_pages:
            frame=F(self.container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.build_navbar()

    def build_navbar(self):
        self.navbar=tk.Frame(self)
        nav_labels=[
            "Background", "Basics", "Bloodline", "Skills",
            "Magic", "Crafting", "Gathering", "Knowledge", "ReviewChoices"
        ]
        for label, frame_class in zip(nav_labels, self.nav_pages):
            btn=tk.Button(self.navbar, text=label, command=lambda f=frame_class: self.show_frame(f))
            btn.pack(side="left", padx=5, pady=5)

    def show_frame(self, cont):
        frame=self.frames[cont]

        for method in ['update_character', 'update_mana', 'UpdateDisplay', 'SetBloodline', 'DisplayAllChoices']:
            if hasattr(frame, method):
                getattr(frame, method)()

        frame.tkraise()

        if cont in self.nav_pages:
            self.navbar.pack(side="bottom", fill="x")
        else:
            if self.navbar: self.navbar.pack_forget()

    def conclude(self):
        self.destroy()

class LoadCharacter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button2 = ttk.Button(self, text="Excel", command=self.ImportExcel)
        button2.grid(row=3, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Google Sheets", command=self.ImportGSheet)
        button3.grid(row=4, column=1, padx=10, pady=10)

    def ImportExcel(self):
        # Open file selection dialog
        file = filedialog.askopenfilename(
            title="Select an Excel file",
            filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
        )

        if not file:
            return  # User cancelled

        if not file.endswith('.xlsx'):
            message = 'Error: Not an excel file.'
            ErrorPopup(self, message)
            return

        try:
            df = BuildChar(file)
        except NoCharacterSheet:
            message = 'Error 1: Sheet does not have a page named "Character"\n\nPlease rename your character page.'
            ErrorPopup(self, message)
            return
        
        except CannotParseSheet:
            message = 'Error 2: Unable to parse sheet. \n\nPlease ensure the character sheet is structured correctly.'
            ErrorPopup(self, message)
            return
        
        ImportChara(df)
        global characterexists
        characterexists = True
        self.controller.initialize_nav_pages()
        self.controller.show_frame(ChooseBackground)

    def ImportGSheet(self):
        message='Google Sheets import is currently unavailable.'
        ErrorPopup(self,message)

class LoadGSheet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Google Sheet Loader", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Character Manager", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="New Character",
                             command=lambda: controller.show_frame(NewCharacter))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Load Character",
                             command=lambda: controller.show_frame(LoadCharacter))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Prefix Character",
                             command=lambda: controller.show_frame(ChoosePrefix))
        button3.grid(row=3, column=1, padx=10, pady=10)

class NewCharacter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="New Character Creator", font=LARGEFONT)
        label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        field_names = ["name", "email", "character", "religion"]
        self.entries = {}

        for idx, field_name in enumerate(field_names):
            idx+=1
            if field_name == "religion":
                self.create_bloodline_dropdown(idx + 1)
                self.create_culture_dropdown(idx + 2)
                idx += 2  # Adjust row for religion entry

            label = ttk.Label(self, text=f"{field_name.capitalize()}:")
            label.grid(row=idx + 1, column=0, padx=10, pady=5, sticky="w")

            entry = ttk.Entry(self)
            entry.grid(row=idx + 1, column=1, padx=10, pady=5, sticky="ew")

            self.entries[field_name] = entry

        create_btn = ttk.Button(self, text="Create Character", command=self.validateentries)
        create_btn.grid(row=len(field_names) + 5, column=0, columnspan=2, pady=20)

    def create_bloodline_dropdown(self, row):
        bloodline_label = ttk.Label(self, text="Bloodline:")
        bloodline_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.bloodline_options = ['Human', 'Effendal', 'Fae Blooded', 'Celestial Blooded',
                                  'Demon Blooded', 'Dragon Blooded', 'Newborn Dream']
        self.dropdown = ttk.Combobox(self, values=self.bloodline_options, state="readonly")
        self.dropdown.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        self.dropdown.set("Choose Bloodline")

    def update_bloodline_options(self, new_options):
        """Call this method from other classes to update bloodline options dynamically."""
        self.bloodline_options = new_options
        self.dropdown['values'] = self.bloodline_options
        self.dropdown.set("Choose Bloodline")

    def create_culture_dropdown(self, row):
        culture_label = ttk.Label(self, text="Culture:")
        culture_label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        self.culture_options = ['Ad Decimum', 'Castle Thorn', 'Celestine', 'Cestral', 'Cole', 'Dace',
                                'Drir', "Ko'aat", 'Hastings', 'Myre', 'Nadine', 'Saek', 'Trahazi',
                                'Vicaul', 'Bastion', 'Breach', 'Paradox Dawn', 'Paradox Dusk',
                                'Redemption', 'Citadel', 'Endurant Tribes']
        self.culturedropdown = ttk.Combobox(self, values=self.culture_options, state="readonly")
        self.culturedropdown.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        self.culturedropdown.set("Choose Culture")

    def validateentries(self):
        name = self.entries["name"].get()
        email = self.entries["email"].get()
        character = self.entries["character"].get()
        culture = self.culturedropdown.get()
        bloodline = self.dropdown.get()
        religion = self.entries["religion"].get() or None  # Converts blank to None

        missingentries = []
        if not name:
            missingentries.append("name")
        if not email:
            missingentries.append("email")
        if culture == 'Choose Culture' and bloodline!='Newborn Dream':
            missingentries.append("culture")
        if bloodline == 'Choose Bloodline':
            missingentries.append("bloodline")

        if missingentries:
            error_window = tk.Toplevel(self)
            error_window.title("Missing Information")
            error_label = tk.Label(error_window, text=f"Please fill in the following field(s): {', '.join(missingentries)}", font=("Arial", 12), fg="red")
            error_label.pack(padx=10, pady=10)
            ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
            ok_button.pack(pady=(0, 10))
            return None
        else:
            dict = choices['details']
            dict['Player'] = name
            dict['Email'] = email
            dict['Culture'] = culture
            dict['Religion'] = religion
            dict['Character'] = character
            dict['Bloodline'] = bloodline
 
            if bloodline=='Newborn Dream':

                dic={'Tethered':{'Quant':1,'Cost':-10,'Level':None}}
                choices['background']['flaws']=dic
                allchoices=dic
            choices['Bloodline']={}
            choices['Bloodline'][bloodline]={}

        self.controller.initialize_nav_pages()
        self.controller.show_frame(ChooseBackground)

class ChooseBackground(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        # Create header frame for the back button
        header=tk.Frame(self)
        header.grid(row=0, column=0, sticky="w", columnspan=5)

        # Main content starts at row 1
        ttk.Label(self, text="Choose Background Skills", font=LARGEFONT).grid(
            row=1, column=0, columnspan=5, padx=10, pady=10)

        ttk.Label(self, text="This is the ChooseBackground page.\nMore content coming soon!", font=("Arial", 14)).grid(
            row=2, column=0, columnspan=5, padx=10, pady=10)

        categories=skills['background'].keys()
        self.entries={}
        self.cost_labels={}
        self.entry_rows={}
        self.selection_widgets=[]
        self.page='background'

        start_row=4
        ttk.Label(self, text='Quantity', font=("Arial", 10)).grid(
            row=start_row-1, column=2, padx=5, pady=(0, 5), sticky="w")
        ttk.Label(self, text='Cost', font=("Arial", 10)).grid(
            row=start_row-1, column=3, padx=5, pady=(0, 5), sticky="w")

        for idx, field_name in enumerate(categories):
            row=start_row+idx
            self.entry_rows[field_name]=row

            ttk.Label(self, text=f"{field_name.capitalize()}:").grid(
                row=row, column=0, padx=(5, 2), pady=5, sticky="e")

            options=list(skills['background'][field_name].keys())
            dropdown=ttk.Combobox(self, values=options, state="readonly")
            dropdown.grid(row=row, column=1, padx=(0, 2), pady=5, sticky="ew")
            dropdown.set(f"Choose {field_name}")

            qty_var=tk.StringVar(value="")
            ttk.Label(self, textvariable=qty_var).grid(row=row, column=2, sticky="w")

            cost_var=tk.StringVar(value="—")
            ttk.Label(self, textvariable=cost_var).grid(row=row, column=3, sticky="w")

            self.cost_labels[field_name]=(cost_var, qty_var)
            self.entries[field_name]=dropdown

            def update_text(event, fn=field_name):
                selected=self.entries[fn].get()
                cost_var, qty_var=self.cost_labels[fn]
                cost_var.set(skills['background'][fn][selected].get('Cost', '—'))
                max_=skills['background'][fn][selected].get('Max')

                if hasattr(self, 'quantity_dropdowns') and fn in self.quantity_dropdowns:
                    self.quantity_dropdowns[fn].destroy()
                    del self.quantity_dropdowns[fn]

                if max_==1:
                    qty_var.set('1')
                else:
                    qty_var.set('')
                    quantity_values=[str(i) for i in range(0, max_+1)]
                    qty_dropdown=ttk.Combobox(self, values=quantity_values, state="readonly", width=3)
                    qty_dropdown.set(quantity_values[0])
                    qty_dropdown.grid(row=self.entry_rows[fn], column=2, sticky="w")
                    qty_dropdown.bind("<<ComboboxSelected>>", lambda e, var=qty_var, box=qty_dropdown: var.set(box.get()))
                    if not hasattr(self, 'quantity_dropdowns'):
                        self.quantity_dropdowns={}
                    self.quantity_dropdowns[fn]=qty_dropdown

            dropdown.bind("<<ComboboxSelected>>", partial(update_text, fn=field_name))

            ttk.Button(self, text="Add", command=partial(self.capture_selection, field_name)).grid(
                row=row, column=4, padx=(2, 5), pady=5, sticky="w"
            )

        ttk.Label(self, text="Selected").grid(row=row+1, column=0, columnspan=3, padx=10, pady=10)
        self.selectedrow=row+2

        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)

        self.displayrow=8
        self.displalycol=1

        self.flawpoints=0

    def capture_selection(self,field_name):
        # Loop through each field_name (category)
        category = field_name  # category is the field name key
        name = self.entries[field_name].get()  # selected skill name

        cost_var, qty_var = self.cost_labels[field_name]
        cost = cost_var.get()
        quantity = qty_var.get()
        cost=int(cost)*int(quantity)

        choice = SkillChoice(name, cost, cat=field_name, page='background', quantity=quantity)
        self.choicedict=None
        ValidateSelection(self,choice)
        self.UpdateDisplay()
        if cost<0:
            self.DisplayFlawPoints(cost)

    def DisplayFlawPoints(self,cost):
        if self.flawpoints==-10:
            pass
        else:
            self.flawpoints+=cost
            if self.flawpoints<=-10:
                self.flawpoints=-10
                ttk.Label(self, text='Max Flaw Points Reached').grid(row=5, column=5, padx=10, pady=10)              
        flawdisplay=ttk.Label(self, text=f'Flaw Points: {self.flawpoints}').grid(row=1, column=99, padx=10, pady=10)
    
    def UpdateDisplay(self):
        DisplaySelection(self, row=8,column=0)

class ChooseBasics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        self.character=self.controller.character

        # Data structures

        self.page='basic'

        # UI setup
        self.create_widgets()

        self.flawpoints=0

    def create_widgets(self):
        # Title
        title=ttk.Label(self, text="Add Basic Skills", font=LARGEFONT)
        title.grid(row=0, column=0, padx=10, pady=10)

        # Headers
        ttk.Label(self, text="Skills").grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self, text="Cost").grid(row=1, column=1, padx=10, pady=10)
        ttk.Label(self, text="Quantity").grid(row=1, column=2, padx=10, pady=10)      

        row=2
        for skill, skilldata in skills['basic']['basic'].items():
            cost=skilldata['Cost']
            max_=skilldata['Max']

            # Labels
            ttk.Label(self, text=skill).grid(row=row, column=0, padx=10, pady=10)
            ttk.Label(self, text=cost).grid(row=row, column=1, padx=10, pady=10)

            # Quantity combobox
            qty_values=[str(i) for i in range(0,51)] if max_ is None else [str(i) for i in range(0,6)]
            quant_cb=ttk.Combobox(self, values=qty_values, state="readonly", width=5)
            quant_cb.set(qty_values[0])
            quant_cb.grid(row=row, column=2, padx=10, pady=10)

            # Add button
            addbutton=ttk.Button(
                self, 
                text="Add", 
                command=partial(self.capture_selection, skill, cost, quant_cb)
            )
            addbutton.grid(row=row, column=3, padx=10, pady=10)

            row+=1

        # Back button
        ttk.Button(self, text="<Back", command=lambda: self.controller.show_frame(ChooseBackground)).grid(
            row=row, column=0, columnspan=4, padx=10, pady=10)

    def capture_selection(self, skill, cost, quant_widget):
        quantity=quant_widget.get()
        cost=cost*quantity
        choice=SkillChoice(skill, cost, cat='basic', page='basic', quantity=quantity)
        self.choicedict=None
        ValidateSelection(self, choice)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        DisplaySelection(self, row=10, column=0)

class ChooseRacial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller  # ensure controller is stored

        title=ttk.Label(self, text=f"Add Bloodline Skills", font=LARGEFONT)
        title.grid(row=0, column=0, padx=10, pady=10)

        skillsheader=ttk.Label(self, text="Skills")
        skillsheader.grid(row=1, column=0, padx=10, pady=10)

        costheader = ttk.Label(self, text="Cost")
        costheader.grid(row=1, column=1, padx=10, pady=10)

        quantityheader=ttk.Label(self, text='Quantity')
        quantityheader.grid(row=1, column=2, padx=10, pady=10)

        self.page='Bloodline'

        self.bloodlineset=False

    def SetBloodline(self):
        self.race=choices['details']['Bloodline']

    def update_character(self):
        self.race=choices['details']['Bloodline']
        list_=list(skills['Bloodline'][self.race].keys())
        self.selections={}
        for skill in list_:
            self.selections[skill]={'Quant':'','Cost':''}
        skill_1=ttk.Label(self, text="Skills")
        skill_1.grid(row=2, column=0, padx=10, pady=10)
        row=2
        column=0
        for skill in list_:
            skill_label=ttk.Label(self,text=skill)
            skill_label.grid(row=row,column=column, padx=10, pady=10)
            column+=1

            cost=skills['Bloodline'][self.race][skill]['Cost']
            cost_label=ttk.Label(self,text=cost)
            cost_label.grid(row=row,column=column, padx=10, pady=10)
            column+=1

            max_qty=skills['Bloodline'][self.race][skill]['Max']
            if max_qty==1:
                qty_value = 1
                quant_label=ttk.Label(self,text=qty_value)
                quant_label.grid(row=row,column=column, padx=10, pady=10)
            else:
                qty_values=[str(i) for i in range(0,51)]
                quant_label=ttk.Combobox(self, values=qty_values, state="readonly", width=5)
                quant_label.set(qty_values[0])  # default to 0
                quant_label.grid(row=row,column=column, padx=10, pady=10)

            # Create the add button with partial to pass these captured values
            add_button = tk.Button(
                self,
                text="Add",
                command=partial(self.capture_choice, skill, cost, quant_label)
            )
            add_button.grid(row=row,column=column+1, padx=10, pady=10)

            column=0
            row+=1

    def capture_choice(self, skill, cost, quant):
        quant = quant.get() if isinstance(quant, ttk.Combobox) else 1
        choice=SkillChoice(skill,cost,page='Bloodline',quantity=quant, cat=choices['details']['Bloodline'])
        ValidateSelection(self,choice)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        DisplaySelection(self, row=10,column=0)

class ChooseSkills(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page = 'General Skills'

        row = 1

        # ======= TOP CONTROLS FRAME =======
        top_controls = tk.Frame(self)
        top_controls.grid(row=row, column=0, sticky="ew")

        label = ttk.Label(top_controls, text="Choose Skills", font=LARGEFONT)
        label.grid(row=row, column=0, columnspan=5, padx=10, pady=10, sticky="n")

        categories = list(skills['General Skills'].keys())
        self.cat_dropdown = ttk.Combobox(top_controls, values=categories, state="readonly", width=15)
        self.cat_dropdown.set('pick category')
        self.cat_dropdown.grid(row=row+1, column=0, sticky="ew", padx=5)

        self.option_dropdown = ttk.Combobox(top_controls, state="readonly", width=15)
        self.option_dropdown.set('pick option')
        self.option_dropdown.grid(row=row+1, column=1, sticky="ew", padx=5)

        # Fixed placeholder for quantity widget
        self.qty_placeholder = tk.Frame(top_controls, width=60)  # enough space for a dropdown or label
        self.qty_placeholder.grid(row=row+1, column=2, sticky="ew", padx=5)
        self.qty_widget = None

        self.cost_var = tk.StringVar(value="-")
        cost_label = ttk.Label(top_controls, textvariable=self.cost_var)
        cost_label.grid(row=row+1, column=3, sticky="ew", padx=5)

        add_button = ttk.Button(top_controls, text="Add", command=self.add_skill)
        add_button.grid(row=row+1, column=4, padx=10, pady=10)

        # ======= Scrollable canvas setup =======
        canvas = tk.Canvas(self, height=400)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=row+1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.scrollable_frame = scrollable_frame

        def remove_qty_widget():
            if self.qty_widget is not None:
                self.qty_widget.destroy()
                self.qty_widget = None
        self.remove_qty_widget = remove_qty_widget

        def update_options(event):
            selected_category = self.cat_dropdown.get()
            if selected_category in skills['General Skills']:
                options = list(skills['General Skills'][selected_category].keys())
                self.option_dropdown.config(values=options)
                self.option_dropdown.set('pick skill')
                self.cost_var.set("-")
                self.remove_qty_widget()
            else:
                self.option_dropdown.config(values=[])
                self.option_dropdown.set('no options')
                self.cost_var.set("-")
                self.remove_qty_widget()

        self.cat_dropdown.bind("<<ComboboxSelected>>", update_options)

        def update_cost_and_qty(event):
            selected_category = self.cat_dropdown.get()
            selected_skill = self.option_dropdown.get()
            if selected_category in skills['General Skills'] and selected_skill in skills['General Skills'][selected_category]:
                base_cost = skills['General Skills'][selected_category][selected_skill].get('Cost', '-')
                max_value = skills['General Skills'][selected_category][selected_skill].get('Max', 1)

                def calculate_and_update_cost(event=None):
                    try:
                        qty = int(self.qty_widget.get()) if isinstance(self.qty_widget, ttk.Combobox) else 1
                    except (ValueError, AttributeError):
                        qty = 1
                    if isinstance(base_cost, (int, float)):
                        total_cost = qty * base_cost
                        self.cost_var.set(str(total_cost))
                    else:
                        self.cost_var.set("-")

                self.remove_qty_widget()

                if max_value == 1:
                    self.qty_widget = ttk.Label(self.qty_placeholder, text="1")
                else:
                    qty_values = [str(i) for i in range(0, (max_value or 100) + 1)]
                    self.qty_widget = ttk.Combobox(self.qty_placeholder, values=qty_values, state="readonly", width=5)
                    self.qty_widget.set('0')
                    self.qty_widget.bind("<<ComboboxSelected>>", calculate_and_update_cost)

                self.qty_widget.pack(fill="both", expand=True)
                calculate_and_update_cost()
            else:
                self.cost_var.set("-")
                self.remove_qty_widget()

        self.option_dropdown.bind("<<ComboboxSelected>>", update_cost_and_qty)

    def add_skill(self):
        category = self.cat_dropdown.get()
        skill = self.option_dropdown.get()
        cost = self.cost_var.get()
        print(cost)
        try:
            qty = int(self.qty_widget.get()) if isinstance(self.qty_widget, ttk.Combobox) else 1
        except Exception:
            qty = 1
        choice = SkillChoice(skill, cost, quantity=qty, cat=category, page='General Skills')
        self.choicedict = None
        if category == 'Knowledge':
            self.page = 'Knowledge'
        ValidateSelection(self, choice)
        self.page = 'General Skills'
        self.UpdateDisplay()

    def UpdateDisplay(self):
        DisplaySelection(self, row=0, column=0)

class AddMagic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller  # store controller

        label = ttk.Label(self, text="Add Magic", font=("Arial", 20))
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        placeholder = ttk.Label(self, text="Magic feature coming soon.", font=("Arial", 14))
        placeholder.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        selectionheader = ttk.Label(self, text="Selected", font=("Arial", 14))
        selectionheader.grid(row=0, column=4, padx=10, pady=10, columnspan=3)

        magicsubheader = ttk.Label(self, text="Magic", font=("Arial", 14))
        magicsubheader.grid(row=1, column=4, padx=10, pady=10)

        levelsubheader = ttk.Label(self, text="Level", font=("Arial", 14))
        levelsubheader.grid(row=1, column=6, padx=10, pady=10)

        self.magic_dropdown = ttk.Combobox(self, values=skills['Magical Arts']['Magics']['Magics'], state="readonly", width=20)
        self.magic_dropdown.set('Select Magic')
        self.magic_dropdown.grid(row=2, column=0, padx=10, pady=10)

        self.leveldropdown = ttk.Combobox(self, values=list(skills['Magical Arts']['Magics']['Levels'].keys()), state="readonly", width=20)
        self.leveldropdown.set('Select Level')
        self.leveldropdown.grid(row=2, column=1, padx=10, pady=10)

        add_button = ttk.Button(self, text="Add", command=self.capture_entry)
        add_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        
        try:
            mana=allchoices['Mana Focus']['Quant']
        except KeyError:
            mana=0

        self.mana_counter=ttk.Label(self, text=mana)
        self.mana_counter.grid(row=0, column=20, padx=10, pady=10, columnspan=2)

        ttk.Button(self, text="<Back", command=lambda: controller.show_frame(ChooseSkills)).grid(
            row=10, column=0, columnspan=4, padx=10, pady=10)
        
        self.page='Magical Arts'
        
    def update_mana(self):
        try:
            mana = allchoices['Mana Focus']['Quant']
        except KeyError:
            mana = 0
        self.mana_counter.config(text=mana)

    def capture_entry(self):
        magic=self.magic_dropdown.get()
        level=self.leveldropdown.get()
        cost=levels[level]*6

        
        choice= SkillChoice(magic, cost, cat='Magics', page='Magical Arts', level=level)
        self.choicedict=None
        ValidateSelection(self,choice)
        self.UpdateDisplay()
    
    def UpdateDisplay(self):
        DisplaySelection(self, row=5,column=3)

class AddCrafting(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Add Crafting", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(self, text="Choose crafting")
        label.grid(row=1, column=0, padx=10, pady=10)

        self.page='Crafting'

        # headers...
        catheader = ttk.Label(self, text="Category", font=("Arial", 14))
        catheader.grid(row=3, column=0, padx=10, pady=10)
        skillheader = ttk.Label(self, text="Skill", font=("Arial", 14))
        skillheader.grid(row=3, column=1, padx=10, pady=10)
        quantheader = ttk.Label(self, text="Quantity", font=("Arial", 14))
        quantheader.grid(row=3, column=2, padx=10, pady=10)
        costheader = ttk.Label(self, text="Cost", font=("Arial", 14))
        costheader.grid(row=3, column=3, padx=10, pady=10)

        categories = list(skills['Crafting'].keys())
        self.cat_dropdown = ttk.Combobox(self, values=categories, state="readonly", width=15)
        self.cat_dropdown.set('pick category')
        self.cat_dropdown.grid(row=4, column=0, sticky="w")

        self.option_dropdown = ttk.Combobox(self, state="readonly", width=15)
        self.option_dropdown.set('pick option')
        self.option_dropdown.grid(row=4, column=1, sticky="w")

        self.cost_var = tk.StringVar(value="-")
        cost_label = ttk.Label(self, textvariable=self.cost_var)
        cost_label.grid(row=4, column=3, sticky="w")

        self.qty_widget = ttk.Combobox(self, values=('Apprentice','Journeyman','Master','Grandmaster'), state="readonly")
        self.qty_widget.set('pick option')
        self.qty_widget.grid(row=4, column=2, sticky="w")

        self.cat_dropdown.bind("<<ComboboxSelected>>", self.update_options)

        self.addedcrafts = {
            'Metalworking': {},
            'Arcane': {},
            'Edible': {},
            'Other': {}
        }
        self.addedskills = []

        add_button = ttk.Button(self, text="Add", command=self.capture_selection)
        add_button.grid(row=4, column=8, padx=10, pady=10)

        page='Crafting'

    def update_options(self, event):
        selected_category = self.cat_dropdown.get()
        if selected_category in skills['Crafting']:
            options = list(skills['Crafting'][selected_category])
            self.option_dropdown.config(values=options)
            self.option_dropdown.set('pick skill')
            self.cost_var.set("-")
        else:
            self.option_dropdown.config(values=[])
            self.option_dropdown.set('no options')
            self.cost_var.set("-")

    def capture_selection(self):
        category = self.cat_dropdown.get()
        skill = self.option_dropdown.get()
        level = self.qty_widget.get()
       
        cost = levels[level]*6

        choice = SkillChoice(skill,cost,cat=category,page='Crafting',quantity=levels[level],level=level)
        ValidateSelection(self,choice)
        self.UpdateDisplay()
    
    def UpdateDisplay(self):
        DisplaySelection(self, row=5,column=3)

class AddGathering(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Add Gathering", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(self, text="Choose type and level")
        label.grid(row=1, column=0, padx=10, pady=10)

        categories=list(skills['Gathering']['gathering'].keys())

        self.skillsdropdown=ttk.Combobox(self, values=categories, state="readonly", width=15)
        self.skillsdropdown.grid(row=2,column=0, sticky='w')

        self.levelsdropdown=ttk.Combobox(self, values=(1,2,3,4), state="readonly", width=15)
        self.levelsdropdown.grid(row=2,column=1, sticky='w')

        addbutton=ttk.Button(self, text="Add",command=self.validateentry)
        addbutton.grid(row=2,column=2, sticky='w')      

        self.addedskills = []

        self.page='Gathering'

    def validateentry(self):
        skill=self.skillsdropdown.get()
        quantity=self.levelsdropdown.get()
        cost=int(quantity)*4

        choice=SkillChoice(skill,cost,cat='gathering',page='Gathering',quantity=quantity)

        self.choicedict=None
        ValidateSelection(self,choice)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        DisplaySelection(self, row=4,column=0)

class AddKnowledge(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page='Knowledge'

        dropdown_options=list(skills['Knowledge'].keys())
        global characterexists
        if characterexists is True:
            dropdown_options.append('Non-Starting Lore')
            skills[self.page]['Non-Starting Lore']={}
            choices[self.page]['Non-Starting Lore']={}
        

        # Category dropdown
        self.catdropdown=ttk.Combobox(self, values=dropdown_options, state="readonly")
        self.catdropdown.set("Select Knowledge Category")
        self.catdropdown.grid(row=0, column=0, padx=10, pady=10)
        self.catdropdown.bind("<<ComboboxSelected>>", self.update_subdropdown)

        # Subcategory dropdown (initially empty)
        self.subdropdown=ttk.Combobox(self, values=[], state="readonly")
        self.subdropdown.set("Select Specific Knowledge")
        self.subdropdown.grid(row=1, column=0, padx=10, pady=10)

        # Add button
        add_button=tk.Button(self, text="Add", command=self.capture_selection)
        add_button.grid(row=1, column=1, padx=10, pady=10)

    def update_subdropdown(self, event):
        selected_cat=self.catdropdown.get()

        # Clean up previous widgets if they exist
        if hasattr(self, 'lore_entry'):
            self.lore_entry.destroy()
            del self.lore_entry
        if hasattr(self, 'lore_label'):
            self.lore_label.destroy()
            del self.lore_label

        if selected_cat == 'Non-Starting Lore':
            self.subdropdown.grid_forget()
            self.lore_label = tk.Label(self, text="Lore:")
            self.lore_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
            self.lore_entry = tk.Text(self, height=4, width=30)
            self.lore_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        elif selected_cat in skills['Knowledge']:
            self.subdropdown.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
            new_options = list(skills['Knowledge'][selected_cat].keys())
            self.subdropdown['values'] = new_options
            self.subdropdown.set("Select Specific Knowledge")

        else:
            self.subdropdown.grid_forget()

    def capture_selection(self):
        cat = self.catdropdown.get()
        if cat == 'Non-Starting Lore' and hasattr(self, 'lore_entry'):
            skill = self.lore_entry.get('1.0', 'end').strip()
            skill=f'Lore: {skill}'
            skills[self.page]['Non-Starting Lore'][skill]={'Max': 1, 'Cost': 4, 'cat':'Knowledge', 'subcat':cat}
        else:
            skill = self.subdropdown.get()

        if not skill:
            # Handle empty input if needed
            return

        choice = SkillChoice(skill, cost=4, cat=cat, page='Knowledge')
        ValidateSelection(self, choice)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        DisplaySelection(self, row=7, column=0)

class ReviewChoices(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # ======= TOP CONTROLS FRAME =======
        top_controls = tk.Frame(self)
        top_controls.grid(row=0, column=0, sticky="ew")

        add_button = ttk.Button(top_controls, text="Create Character", command=self.TestFunc)
        add_button.configure(style="Bold.TButton")
        add_button.grid(row=0, column=0, padx=10, pady=10)

        # Center the button using grid options
        top_controls.grid_columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure("Bold.TButton", font=("TkDefaultFont", 10, "bold"))

        # ======= Scrollable canvas setup =======
        canvas = tk.Canvas(self, height=400)  # set desired height
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.scrollable_frame = scrollable_frame

    def DisplayAllChoices(self):

        global choices

        row = 1  # Start from row 1
        max_columns = 1  # Track the longest column span for consistent separators

        for cat in choices:
            subcats = []

            if cat not in ['details', 'Postage']:
                ref = choices[cat]
                for subcat in ref:
                    if ref[subcat] != {}:
                        subcats.append(subcat)
            else:
                continue

            # === Calculate max number of rows needed for subcats ===
            max_skill_rows = 1  # at least one for subcat label
            if subcats == []:
                max_skill_rows = 1
            else:
                for subcat in subcats:
                    num_skills = len(ref[subcat])
                    total_rows = 1 + num_skills  # 1 for subcat label + skills
                    if total_rows > max_skill_rows:
                        max_skill_rows = total_rows

            # === Update max_columns based on current subcats ===
            num_columns = len(subcats) + 1  # +1 for category column
            if num_columns > max_columns:
                max_columns = num_columns

            # === Calculate center row for category label ===
            center_row = row + (max_skill_rows // 2)

            # === Display category label centered ===
            label = ttk.Label(self.scrollable_frame, text=cat)
            label.grid(row=center_row, column=0, padx=10, pady=10)

            # === Display subcategories horizontally starting at top row ===
            if subcats == []:
                label = ttk.Label(self.scrollable_frame, text='None selected')
                label.grid(row=row, column=1, padx=10, pady=10)
            else:
                for i, subcat in enumerate(subcats):
                    col = i + 1  # start from column 1 since column 0 is category

                    # Subcategory label at top row of the section
                    label = ttk.Label(self.scrollable_frame, text=subcat, font=("Arial", 10, 'bold'))
                    label.grid(row=row, column=col, padx=10, pady=10)

                    # Skills listed below subcategory
                    skill_row = row + 1
                    for skill in ref[subcat]:
                        label = ttk.Label(self.scrollable_frame, text=skill, font=("Arial", 8))
                        label.grid(row=skill_row, column=col, padx=10, pady=2)
                        skill_row += 1

            # === Move row down by max_skill_rows + 1 for spacing ===
            row += max_skill_rows + 1

            # === Insert separator line with consistent length ===
            separator = ttk.Separator(self.scrollable_frame, orient='horizontal')
            separator.grid(row=row, column=0, columnspan=max_columns, sticky="ew", pady=5)
            row += 1  # Move to the next row after separator


    def TestFunc(self):
        choices['Knowledge']['Native Lore'][f"Native Lore: {choices['details']['Culture']}"]={'Quant':1,'Cost':0,'Level':None,'Cat':'Knowledge'}
        filepath = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                        filetypes=[("Excel files", "*.xlsx")])

        process_choices(choices, filepath)

class ChoosePrefix(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        prefixchars=['Shield Fighter', 'Raging Barbarian', 'Knife-Wielding Assassin','Stylish Duelist','Wandering Monk','Combat Healer',
                     'Master Sorceror','Practiced Surgeon','Charismatic Courtier','Alchemical Merchant','Dream of Infinite Possibility']

        row=1

        for build in prefixchars:
            add_button = ttk.Button(self, text=build, command=partial(self.LoadPrefix,prefixdict[build],build))
            add_button.grid(row=row, column=8, padx=10, pady=10)
            row+=1

    def LoadPrefix(self,dict,build):
        refpage=self.controller.frames[NewCharacter]
        target=refpage.update_bloodline_options
        if build!='Dream of Infinite Possibility':
            target(['Human','Effendal'])
        else:
            target(['Newborn Dream'])
        ImportChara(dict)
        global characterexists
        characterexists=True 
        self.controller.show_frame(NewCharacter)

flawpoints=0
characterexists=False

def StartApp():
    characterexists=False
    app = tkinterApp()
    app.mainloop()
