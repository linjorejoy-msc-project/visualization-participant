import logging
import threading
import time
import pages.MasterPage as MasterPage

# from client.clientVisualization import main as participantMain
from client.ClientVisualizationClass import ClientVisualizationClass

from tkinter import SW, NSEW, LEFT, BOTH
from tkinter import scrolledtext

from widgetclasses.MyButton import MyButton
from widgetclasses.MyLabelFrame import MyLabelFrame

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

# matplotlib.use("tkagg")


FORMAT = "%(levelname)-10s %(asctime)s: %(message)s"
logging.basicConfig(
    handlers=[
        logging.FileHandler(
            filename="logs_visualization.log", encoding="utf-8", mode="w"
        )
    ],
    level=logging.DEBUG,
    format=FORMAT,
)

print("Started Viz page")


class VisualizationPage1(MasterPage.MasterPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.participantObject = ClientVisualizationClass()

        self.body_sublabelframe1 = None
        self.body_sublabelframe2 = None

        self.start_server_button = None

        self.start_listening_button = None
        self.stop_listening_button = None
        self.start_listening_cycle_button = None
        self.stop_listening_cycle_button = None

        self.MAX_COLS = 3
        self.plots = {
            "1": {
                "title": "Drag vs Timestep",
                "y_axis": "drag",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 1000,
            },
            "2": {
                "title": "MassflowRate vs Timestep",
                "y_axis": "currentMassFlowRate",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 1000,
            },
        }

    def set_subframes_bodyframe(self):
        self.body_sublabelframe1 = MyLabelFrame(
            parent=self.body_label_frame,
            controller=self.controller,
            text="Menu",
            height="800",
            grid=(0, 0),
            sticky=NSEW,
        )

        self.body_sublabelframe2 = MyLabelFrame(
            parent=self.body_label_frame,
            controller=self.controller,
            text="Plots",
            height="800",
            grid=(0, 1),
            sticky=NSEW,
            padx=8,
            pady=8,
        )

    def column_configure_body_frame(self):
        self.body_label_frame.columnconfigure(0, weight=1)
        self.body_label_frame.columnconfigure(1, weight=6)

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

    def start_server_communication(self):
        # participant_thread = threading.Thread(target=self.participantObject.main)
        # participant_thread.start()
        # print("participant thread started")
        visualization_thread = threading.Thread(target=self.plotting_function)
        visualization_thread.start()
        print("viz thread started")

    def animate_plot(self, i, axis, plotData):
        print(f'animate_plot for {plotData["title"]}')
        x_data = [
            each_data_dict[plotData["x_axis"]]
            for each_data_dict in self.participantObject.all_data.values()
        ]
        y_data = [
            each_data_dict[plotData["y_axis"]]
            for each_data_dict in self.participantObject.all_data.values()
        ]
        print(f"x_data: {x_data[-1]}")
        print(f"y_data: {y_data[-1]}\n")
        axis.cla()
        axis.plot(x_data, y_data)

    def plot_one_data(self, index, plotData):
        # axis.legend(["Stock_Index_Price"])
        print(f"plot_one_data for Plot No: {index} started")
        this_figure = plt.figure(
            figsize=(7, 7), linewidth=5, edgecolor="#04253a", dpi=35
        )
        axis = this_figure.add_subplot(111)
        this_plot = FigureCanvasTkAgg(this_figure, self.body_sublabelframe2)
        row_i = (int(index) - 1) // self.MAX_COLS
        col_i = (int(index) - 1) % self.MAX_COLS

        this_plot.get_tk_widget().grid(
            row=row_i, column=col_i, ipadx=50, ipady=30, padx=10, pady=10
        )
        axis.set_xlabel(plotData["xlabel"])
        axis.set_ylabel(plotData["ylabel"])
        axis.set_title(plotData["title"])

        def animate_plot_2(i):
            print("This func called")
            print(f"{self.participantObject.all_data.values()=}")
            x_data = [
                each_data_dict[plotData["x_axis"]]
                for each_data_dict in self.participantObject.all_data.values()
            ]
            y_data = [
                each_data_dict[plotData["y_axis"]]
                for each_data_dict in self.participantObject.all_data.values()
            ]
            print(f"{x_data=}")
            axis.cla()
            axis.plot(x_data, y_data)
            # plt.show()

        count = 0
        while True:
            time.sleep(1)
            animate_plot_2(0)
            count += 1
            if count > 10:
                break

        # this_ani = FuncAnimation(
        #     this_figure,
        #     animate_plot_2,
        #     fargs=(
        #         axis,
        #         plotData,
        #     ),
        #     interval=1000,
        # )

    def plotting_function(self):
        # plt.switch_backend("agg")
        # plt.style.use("fivethirtyeight")
        # for index, plotData in self.plots.items():
        #     print(f"Creating thread for Plot No: {index} - Data: {plotData}")
        #     this_plot_thread = threading.Thread(
        #         target=self.plot_one_data,
        #         args=(
        #             index,
        #             plotData,
        #         ),
        #     )
        #     this_plot_thread.start()

        # this_figure = plt.figure(
        #     figsize=(7, 7), linewidth=5, edgecolor="#04253a", dpi=35
        # )
        # this_ax = this_figure.add_subplot(111)
        # this_plot = FigureCanvasTkAgg(this_figure, self.body_sublabelframe2)
        # row_i = (int(index) - 1) // self.MAX_COLS
        # col_i = (int(index) - 1) % self.MAX_COLS

        # this_plot.get_tk_widget().grid(
        #     row=row_i, column=col_i, ipadx=50, ipady=30, padx=10, pady=10
        # )

        # plt.switch_backend("agg")
        plt.style.use("fivethirtyeight")
        x_val = []
        y_val = []

        figure1 = plt.figure(figsize=(8, 8), linewidth=5, edgecolor="#04253a", dpi=35)
        ax1 = figure1.add_subplot(111)
        canvas_1 = FigureCanvasTkAgg(figure1, self.body_sublabelframe2)
        canvas_1.get_tk_widget().grid(row=0, column=0)
        # scatter3.update_idletasks()
        ax1.legend(["Stock_Index_Price"])
        ax1.set_xlabel("Interest Rate")
        ax1.set_ylabel("Interest Rate")
        ax1.set_title("Interest Rate Vs. Stock Index Price")

        def animate(i):
            x_val.append(len(x_val))
            y_val.append(2 ** len(y_val))

            canvas_1 = FigureCanvasTkAgg(figure1, self.body_sublabelframe2)
            canvas_1.get_tk_widget().grid(row=0, column=0)

            ax1.cla()
            ax1.plot(x_val, y_val)

        ani1 = FuncAnimation(figure1, animate, interval=100)
        # plt.show()

        # x_val_2 = []
        # y_val_2 = []

        # figure2 = plt.figure(figsize=(8, 8), linewidth=5, edgecolor="#04253a", dpi=35)
        # ax2 = figure2.add_subplot(111)
        # scatter3 = FigureCanvasTkAgg(figure2, self.body_sublabelframe2)
        # scatter3.get_tk_widget().grid(row=1, column=0)
        # ax2.legend(["Stock_Index_Price"])
        # ax2.set_xlabel("Interest Rate")
        # ax2.set_ylabel("Interest Rate")
        # ax2.set_title("Interest Rate Vs. Stock Index Price")

        # def animate2(i):
        #     x_val_2.append(len(x_val_2))
        #     y_val_2.append(2 ** len(y_val_2))

        #     ax2.cla()
        #     ax2.plot(x_val_2, y_val_2)

        # ani2 = FuncAnimation(figure2, animate2, interval=100)

    def set_ui(self):
        self.set_subframes_bodyframe()
        self.set_ui_sublabelframe1()
        self.column_configure_body_frame()
        self.start_server_communication()
        return super().set_ui()

    def add_log_to_textarea(self, message: str):

        self.logs_scrolled_text.config(state="normal")
        self.logs_scrolled_text.insert("end", message)
        self.logs_scrolled_text.yview("end")
        self.logs_scrolled_text.config(state="disabled")
