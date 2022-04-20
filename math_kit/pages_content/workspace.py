from tkinter import Tk, Frame, Button, Label



class WorkspacePage:
    """
    This class is the workspace page of the application. It contains the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """
    
    def __init__(self, master, tools):
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.workspace_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.workspace_frame)
        


