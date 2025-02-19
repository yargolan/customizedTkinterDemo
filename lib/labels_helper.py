from customtkinter import *


class LabelsHelper:

    def __init__(self, ui_config):
        self.ui_config = ui_config

        self.label_sizes = {
            "S": {
                "color": 'LightBlue',
                "width": 15,
                "height": 3,
                "font": ('Arial', 20)
            },
            "L": {
                "color": '#4aacda',
                "width": 20,
                "height": 4,
                "font": ('Arial', 40)
            },
            "XL": {
                "color": '#4aacda',
                "width": 20,
                "height": 5,
                "font": ('Arial', 50)
            }
        }



    def create(self, size, master):
        if size not in self.label_sizes:
            size = "S"

        return CTkLabel(
            master=master,
            width=self.label_sizes[size]["width"],
            height=self.label_sizes[size]["height"],
            font=self.label_sizes[size]["font"],
            text_color = self.label_sizes[size]["color"],
        )
