
# Internal Library
import re
import os
import customtkinter
from threading import Thread
from CTkMessagebox import CTkMessagebox

# custom config appearance of GUI
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# harcode MBEA project
COMPONENT_PATH \
    = r'C:\Learning'

def Core_ReviewPoint_Updater():
    """
        This function 
            + Input:
            + Output:
    """

    Thread(target=Core_MarkdownFile_Reader).start()

def Core_Component_Seeker(COMPONENT_PATH):
    """
        This function 
            + Input:
            + Output:
    """

    try:
        componentName_List \
            = [cpn for cpn in os.listdir(COMPONENT_PATH)
               if os.path.isdir(os.path.join(COMPONENT_PATH, cpn) and cpn != '__pycache__')]
        return componentName_List
    except Exception as e:
        print(f'An error occurred: {e}')

def Core_MarkdownFile_Reader():
    """
        This function 
            + Input:
            + Output:
    """
    All_List = []
    Specific_List = []
    pattern = re.compile(r'^[Rr]eview?$')
    try:
        if Target_ComponentName:
            for cpn_name in Target_ComponentName:
                component_path = os.path.join(COMPONENT_PATH, cpn_name)
                if os.path.exists(component_path):
                    for folder in os.listdir(component_path):
                        if pattern.match(folder):
                            md_path = os.path.join(component_path, folder)
                            for file in os.listdir(md_path):
                                if file.endswith('.md'):
                                    markdown_file = os.path.join(md_path, file)
                                    if os.path.exists(markdown_file):
                                        with open(markdown_file, 'r', encoding='UTF-8') as f:
                                            content = f.read()
                                        Specific_List.append(content)
                                else:
                                    CTkMessagebox(title='Error Handling',
                                                  message=f'{cpn_name}\nMarkdown file not found !',
                                                  icon='cancel',
                                                  option_1='OK')
            return Specific_List
    except:
        if Selected_All_ComponentName:
            for cpn_name in Target_ComponentName:
                component_path = os.path.join(COMPONENT_PATH, cpn_name)
                if os.path.exists(component_path):
                    for folder in os.listdir(component_path):
                        if pattern.match(folder):
                            md_path = os.path.join(component_path, folder)
                            for file in os.listdir(md_path):
                                if file.endswith('.md'):
                                    markdown_file = os.path.join(md_path, file)
                                    if os.path.exists(markdown_file):
                                        with open(markdown_file, 'r', encoding='UTF-8') as f:
                                            content = f.read()
                                        All_List.append(content)
                                else:
                                    CTkMessagebox(title='Error Handling',
                                                  message=f'{cpn_name}\nMarkdown file not found !',
                                                  icon='cancel',
                                                  option_1='OK')
            return All_List
    else:
        CTkMessagebox(title='Error Handling',
                        message='Please choose\nComponent Name',
                        icon='cancel',
                        option_1='OK')
        
class Component(customtkinter.CTkScrollableFrame):
    """
        This function 
            + Input:
            + Output:
    """

    def __init__(self, master, component_list, command=None, **kwargs):
        """
            This function 
                + Input:
                + Output:
        """

        super().__init__(master, **kwargs)
        self.command = command
        self.checkbox_list = []
        for _, item in enumerate(component_list):
            self.add_cpn(item)

    def add_cpn(self, item):
        """
            This function 
                + Input:
                + Output:
        """

        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, padx=20, pady=(0, 20), sticky='w')
        self.checkbox_list.append(checkbox)

    def remove_cpn(self, item):
        """
            This function 
                + Input:
                + Output:
        """

        for checkbox in self.checkbox_list:
            if item == checkbox.cget('text'):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return
            
    def select_specific_cpn(self):
        """
            This function 
                + Input:
                + Output:
        """

        checkbox_clicked \
            = [checkbox.cget('text') for checkbox in self.checkbox_list if checkbox.get() == 1]
        
        return checkbox_clicked
    
    def select_all_cpn(self):
        """
            This function 
                + Input:
                + Output:
        """

        select_all_event = []
        for checkbox in self.checkbox_list:
            checkbox.select()
            select_all_event.append(checkbox.cget('text'))

        return select_all_event
    
    def unselect_all_cpn(self):
        """
            This function 
                + Input:
                + Output:
        """

        for checkbox in self.checkbox_list:
            unselect_all_event = checkbox.deselect()

        return unselect_all_event
    
class DashBoard(customtkinter.CTk):
    """
        This function 
            + Input:
            + Output:
    """

    width = 500
    height = 550

    def __init__(self):
        """
            This function 
                + Input:
                + Output:
        """

        super().__init__()
        self.title('ReviewPoint Updater')
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)

        # Create Title
        self.Title_Tool \
            = customtkinter.CTkLabel(self,
                                     text='ReviewPoint Updater',
                                     fg_color='#242424',
                                     font=customtkinter.CTkFont('Centuty Gothic',
                                                                size=24))
        self.Title_Tool.place(x=130, y=40)

        # Get component name form repository
        componentName_List = Core_Component_Seeker(COMPONENT_PATH)
        self.ComponentName_ScrollableCheckbox \
            = Component(self,
                        width=300,
                        height=250,
                        component_list=componentName_List,
                        command=self.GetTarget_ComponentName,
                        label_text='Component Name')
        self.ComponentName_ScrollableCheckbox.place(x=90, y=100)

        # Create 'Select All' radio
        self.getVal_selectall_checkbox \
            = customtkinter.StringVar(value='off')
        self.selectall_checkbox \
            = customtkinter.CTkCheckBox(self,
                                        text='Select all',
                                        width=50,
                                        height=20,
                                        variable=self.getVal_selectall_checkbox,
                                        command=self.SelectComponentName_Event,
                                        onvalue='on',
                                        offvalue='off')
        self.selectall_checkbox.place(x=331, y=425)

        # Create Update Button
        self.Push_button \
            = customtkinter.CTkButton(self,
                                      command=Core_ReviewPoint_Updater,
                                      text='Push Review Point',
                                      fg_color='#1F41A9',
                                      width=320,
                                      height=50,
                                      font=customtkinter.CTkFont('Centuty Gothic',
                                                                size=24,
                                                                weight='bold'),
                                      corner_radius=10)
        self.Push_button.place(x=90, y=480)

    def GetTarget_ComponentName(self):
        """
            This function 
                + Input:
                + Output:
        """

        global Target_ComponentName

        Target_ComponentName \
            = self.ComponentName_ScrollableCheckbox.select_specific_cpn()
        
    def SelectComponentName_Event(self):
        """
            This function 
                + Input:
                + Output:
        """

        global Selected_All_ComponentName

        if self.getVal_selectall_checkbox.get() == 'on':
            Selected_All_ComponentName \
                = self.ComponentName_ScrollableCheckbox.select_all_cpn()
        else:
            self.Selected_All_ComponentName.unselect_all_cpn()

# __MAIN__ #
if __name__ == '__main__':
    app = DashBoard()
    app.mainloop()