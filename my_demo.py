
from customtkinter import *

import json


# local imports
from lib import frames_helper, labels_helper, buttons_helper


class MyDemo:
    def __init__(self, master):

        # Read the applicative configuration file
        with open("config/app_config.json", "r", encoding="utf-8") as f:
            self.app_config = json.load(f)

        # Read the UI configuration file
        with open("config/ui_config.json", "r", encoding="utf-8") as f:
            self.ui_config = json.load(f)

        # Set the UI helpers
        self.fh = frames_helper.FramesHelper(self.ui_config)
        self.lh = labels_helper.LabelsHelper(self.ui_config)
        self.bh = buttons_helper.ButtonsHelper(self.ui_config)

        # Set the main frame
        g = 'x'.join((str(self.ui_config['frames']['default_width']), str(self.ui_config['frames']['default_height'])))
        self.master = master
        self.master.title(f"Tkinter App,   version {self.app_config['version']}")
        self.master.geometry(f"{g}+300+200")
        self.master.resizable(False, False)


    def show_ui(self):
        f_main = self.fh.create("default", self.master)

        # Labels
        l_v = self.lh.create("XL", f_main)
        l_v.configure(text="Volunteers")
        l_v.place(x=20, y=20)

        # Buttons
        b_vol_add = self.bh.create("XL")
        b_vol_add.configure(text="Add")
        b_vol_add.place(x=20, y=100)
        b_vol_add.configure(command=lambda: self.ui_vol_add())


        self.master.mainloop()


    def ui_vol_add(self):
        f_vol_add = self.fh.create("XL", self.master)

        # Labels
        l_v = self.lh.create("L", f_vol_add)
        l_v.configure(text="1234")
        l_v.place(x=20, y=20)

        # Buttons
        b_back = self.bh.create("L")
        b_back.configure(text="Back")
        b_back.place(x=200, y=100)
        b_back.configure(command=lambda: f_vol_add.destroy())


if __name__ == "__main__":
    app = CTk()
    mpv = MyDemo(app)
    mpv.show_ui()
    app.mainloop()
