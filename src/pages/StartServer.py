from tkinter import SW, NSEW
from tkinter import scrolledtext
from turtle import width

# from helperfunctions.logger import add_log
from helpermodules.RequiredObjects import Participant, ConfigData

import pages.MasterPage as MasterPage

from widgetclasses.MyButton import MyButton
from widgetclasses.MyLabelFrame import MyLabelFrame

from helperfunctions.serverfunctions import on_new_participant, start_server


class StartServer(MasterPage.MasterPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.body_sublabelframe1 = None
        self.body_sublabelframe2 = None
        self.body_sublabelframe3 = None

        self.start_server_button = None

        self.start_listening_button = None
        self.stop_listening_button = None
        self.start_listening_cycle_button = None
        self.stop_listening_cycle_button = None

        self.logs_scrolled_text = None

        self.listening = True
        self.server_started = False
        self.listening_cycle_continue = True
        self.listen_max_times = 5

    def set_subframes_bodyframe(self):
        self.body_sublabelframe1 = MyLabelFrame(
            parent=self.body_label_frame,
            controller=self.controller,
            text="Menu",
            height="600",
            grid=(0, 0),
            sticky=NSEW,
        )

        self.body_sublabelframe2 = MyLabelFrame(
            parent=self.body_label_frame,
            controller=self.controller,
            text="Info",
            height="600",
            grid=(0, 1),
            sticky=NSEW,
        )

        self.body_sublabelframe3 = MyLabelFrame(
            parent=self.body_label_frame,
            controller=self.controller,
            text="Logs",
            height="600",
            grid=(0, 2),
            sticky=NSEW,
        )

    def column_configure_body_frame(self):
        self.body_label_frame.columnconfigure(0, weight=1)
        self.body_label_frame.columnconfigure(1, weight=1)
        self.body_label_frame.columnconfigure(2, weight=3)

    def set_ui_sublabelframe1(self):
        self.start_server_button = MyButton(
            parent=self.body_sublabelframe1,
            controller=self.controller,
            text="Start Server - NIU",
            rely=1,
            relx=0,
            x=5,
            y=-5,
            grid=(0, 0),
            anchor=SW,
        )

        self.start_listening_button = MyButton(
            parent=self.body_sublabelframe1,
            controller=self.controller,
            text="Start Listening - NIU",
            rely=1,
            relx=0,
            x=5,
            y=-5,
            grid=(1, 0),
            anchor=SW,
        )

        self.stop_listening_button = MyButton(
            parent=self.body_sublabelframe1,
            controller=self.controller,
            text="Stop Listening - NIU",
            rely=1,
            relx=0,
            x=5,
            y=-5,
            grid=(2, 0),
            anchor=SW,
        )

    def set_ui_sublabelframe3(self):
        # self.logs_scrolled_text = scrolledtext.ScrolledText(self.body_sublabelframe3)
        self.logs_scrolled_text = scrolledtext.ScrolledText(
            self.body_sublabelframe3, width=100, height=40, font=("courier", 8)
        )
        self.logs_scrolled_text.pack()
        self.logs_scrolled_text.config(state="disabled")

    def set_ui(self):
        self.set_subframes_bodyframe()
        self.set_ui_sublabelframe1()
        self.set_ui_sublabelframe3()
        self.column_configure_body_frame()
        return super().set_ui()

    def add_log_to_textarea(self, message: str):

        self.logs_scrolled_text.config(state="normal")
        self.logs_scrolled_text.insert("end", message)
        self.logs_scrolled_text.yview("end")
        self.logs_scrolled_text.config(state="disabled")
