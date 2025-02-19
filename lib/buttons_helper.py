from customtkinter import *


class ButtonsHelper:

    def __init__(self, ui_config):
        self.ui_config = ui_config

        self.button_sizes = {
            "S": {
                "width": 10,
                "height": 1,
            },
            "L": {
                "width": 70,
                "height": 40,
            },
            "XL": {
                "width": 120,
                "height": 60,
            }
        }


    def create(self, size):
        if not size in self.button_sizes:
            size = "S"

        return CTkButton(
                master=None,
                hover=True,
                anchor="center",
                bg_color=self.ui_config['bg_color'],
                fg_color="#90cbf9",
                text_color="black",
                hover_color="#41a7f5",
                border_color="#1477d2",
                border_width=2,
                corner_radius=5,
                width=self.button_sizes[size]['width'],
                height=self.button_sizes[size]['height'],
        )

