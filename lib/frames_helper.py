import tkinter

from customtkinter import *


class FramesHelper:

    def __init__(self, ui_config):
        self.ui_config = ui_config

        self.sizes = {
            "default": {
                "width": self.ui_config['frames']['default_width'],
                "height": self.ui_config['frames']['default_height']
            },
            "XL": {
                "width": self.ui_config['frames']['default_width'],
                "height": self.ui_config['frames']['default_height']
            },
            "L": {
                "width": int(self.ui_config['frames']['default_width'] * 0.8),
                "height": int(self.ui_config['frames']['default_height'] * 0.8)
            },
            "M": {
                "width": int(self.ui_config['frames']['default_width'] * 0.6),
                "height": int(self.ui_config['frames']['default_height'] * 0.6)
            },
            "S": {
                "width": int(self.ui_config['frames']['default_width'] * 0.4),
                "height": int(self.ui_config['frames']['default_height'] * 0.4)
            }
        }


    def create(self, size, master):
        if size not in self.sizes:
            size = "default"

        f = CTkFrame(
                master=master,
                width=self.sizes[size]["width"],
                height=self.sizes[size]["height"],
                border_color=self.ui_config['frames']['border_color'],
                border_width=2
        )

        f.tkraise()
        f.pack_propagate(False)
        f.grid(row=0, column=0, sticky="nesw")
        return f
