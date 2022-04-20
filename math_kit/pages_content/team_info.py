from tkinter import Tk, Frame, Button, Label, messagebox
from PIL import Image, ImageDraw, ImageFilter, ImageTk
import webbrowser
import threading


class TeamInfoPage:
    """
    This class is the team info page of the application. It contains the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """
    
    def __init__(self, master, tools):
        self.tools = tools
        self.requesting = False
        
        self.width = int(tools.screen_width*0.8)
        self.height = int(tools.screen_height*0.8)
        
        self.team_info_frame = Frame(master, width=self.width, height=self.height, bg=tools.pallete["gray"])
        master.add(self.team_info_frame)
        
        self.padx, self.pady, self.ipadx, self.ipady = 20, 30, 10, 10
        self.card_width, self.card_height = int(self.width*0.20), int(self.height*0.5)
        self.avatar_side_lemgth = int(self.width*0.15)
        self.bg, self.bd, self.bd_thickness = "#E3E9C8", self.tools.pallete["blue"], 5
        
        self._SaraCard()
        self._MustafaCard()
        self._BatoolCard()
        self._SalimCard()


    def _SaraCard(self):
        self.sara = Frame(self.team_info_frame, height=self.card_height, bg=self.bg,
                         highlightthickness= self.bd_thickness)
        self.sara.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.sara.grid(row=0, column=0, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.sara.grid_columnconfigure(0, weight=1)
        
        self.sara_img = Image.open(r"../math_kit/assets/sara.png")
        self.sara_img = self.sara_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.sara_img = self.tools.mask_circle_transparent(self.sara_img, 1.5)
        self.sara_avatar_img = ImageTk.PhotoImage(self.sara_img)
        self.sara_avatar = Label(self.sara, image=self.sara_avatar_img, bg=self.bg)
        self.sara_avatar.image = self.sara_avatar_img
        self.sara_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.name = Label(self.sara, text="Sarah \nHudaib", bg=self.bg, font=("Berlin Sans FB", 20))
        self.name.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.sara_github = "https://github.com/sarahhudaib"
        self.sara_linkedin = "https://www.linkedin.com/in/sarah-hudaib-2298a5184/"
        self.sara_github_button = Button(self.sara, text="Github", bg=self.tools.pallete["blue"], 
                                         fg=self.tools.pallete["white"], font=("Berlin Sans FB", 18),
                                  command=lambda: self.url_button_handler(self.sara_github))
        self.sara_linkedin_button = Button(self.sara, text="LinkedIn", bg=self.tools.pallete["blue"], 
                                         fg=self.tools.pallete["white"], font=("Berlin Sans FB", 18),
                                    command=lambda: self.url_button_handler(self.sara_linkedin))
        self.sara_github_button.pack(padx=10, fill="x", expand=True)
        self.sara_linkedin_button.pack(padx=10, fill="x", expand=True)
    
    
    def _MustafaCard(self):
        self.mustafa = Frame(self.team_info_frame,height=self.card_height,
                                bg=self.bg, highlightthickness= self.bd_thickness)
        self.mustafa.grid(row=0, column=1, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.mustafa.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.mustafa.grid_columnconfigure(0, weight=1)
        
        self.mustafa_img = Image.open(r"../math_kit/assets/mustafa.jpg")
        self.mustafa_img = self.mustafa_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.mustafa_img = self.tools.mask_circle_transparent(self.mustafa_img, 1.5)
        self.mustafa_avatar_img = ImageTk.PhotoImage(self.mustafa_img)
        self.mustafa_avatar = Label(self.mustafa, image=self.mustafa_avatar_img, bg=self.bg)
        self.mustafa_avatar.image = self.mustafa_avatar_img
        self.mustafa_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.name = Label(self.mustafa, text="Mustafa \nAlhasanat", bg=self.bg, font=("Berlin Sans FB", 20))
        self.name.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.mustafa_github = ""
        self.mustafa_linkedin = ""
        self.mustafa_github_button = Button(self.mustafa, text="Github", bg=self.tools.pallete["blue"], 
                                         fg=self.tools.pallete["white"], font=("Berlin Sans FB", 18),
                                  command=lambda: self.url_button_handler(self.mustafa_github))
        self.mustafa_linkedin_button = Button(self.mustafa, text="LinkedIn", bg=self.tools.pallete["blue"], 
                                         fg=self.tools.pallete["white"], font=("Berlin Sans FB", 18),
                                    command=lambda: self.url_button_handler(self.mustafa_linkedin))
        self.mustafa_github_button.pack(padx=10, fill="x", expand=True)
        self.mustafa_linkedin_button.pack(padx=10, fill="x", expand=True)
        
        
    def _BatoolCard(self):
        self.batool = Frame(self.team_info_frame,height=self.card_height,
                                bg=self.bg, highlightthickness= self.bd_thickness)
        self.batool.grid(row=0, column=2, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.batool.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.batool.grid_columnconfigure(0, weight=1)
        
        self.batool_img = Image.open(r"../math_kit/assets/batool.png")
        self.batool_img = self.batool_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.batool_img = self.tools.mask_circle_transparent(self.batool_img, 1.5)
        self.batool_avatar_img = ImageTk.PhotoImage(self.batool_img)
        self.batool_avatar = Label(self.batool, image=self.batool_avatar_img, bg=self.bg)
        self.batool_avatar.image = self.batool_avatar_img
        self.batool_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        
    def _SalimCard(self):
        self.salim =  Frame(self.team_info_frame,  height=self.card_height,
                                bg=self.bg, highlightthickness= self.bd_thickness)
        self.salim.grid(row=0, column=3, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.salim.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.salim.grid_columnconfigure(0, weight=1)
        
        self.salim_img = Image.open(r"../math_kit/assets/salim.png")
        self.salim_img = self.salim_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.salim_img = self.tools.mask_circle_transparent(self.salim_img, 1.5)
        self.salim_avatar_img = ImageTk.PhotoImage(self.salim_img)
        self.salim_avatar = Label(self.salim, image=self.salim_avatar_img, bg=self.bg)
        self.salim_avatar.image = self.salim_avatar_img
        self.salim_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        
    def url_button_handler(self, url):
        """
        opens the url in the default browser

        Args:
            url (string): url to be opened
        """
        
        def thread(url):
            """
            a function that opens the url in the default browser

            Args:
                url (string): url to be opened
            """
            
            self.requesting = True
            webbrowser.open_new(url)
            self.requesting = False
        
        
        # if there is a web page is openning now, raise an error message box
        if self.requesting:
            messagebox.showerror("Page is openning !!!", "There is a page opening currently, please wait until it is finished.")

        # open the web page in a new thread only if there is no web page is openning now
        threading.Thread(target=thread, args=(url,)).start()