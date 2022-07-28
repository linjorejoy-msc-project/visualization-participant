import logging
import math
import threading
import time

from numpy import integer


from client.ClientVisualizationClass import ClientVisualizationClass

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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


class VisualizationStandalone:
    def __init__(self) -> None:

        self.participantObject = ClientVisualizationClass()
        self.plots = {
            "1": {
                "title": "Drag vs Timestep",
                "y_axis": "drag",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 3000,
            },
            "2": {
                "title": "MassflowRate vs Timestep",
                "y_axis": "currentMassFlowRate",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 3000,
            },
            "3": {
                "title": "Drag vs Timestep",
                "y_axis": "drag",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 3000,
            },
            "4": {
                "title": "MassflowRate vs Timestep",
                "y_axis": "currentMassFlowRate",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 3000,
            },
        }

        self.MAX_COLS = 2
        self.ROWS = math.ceil(len(self.plots.keys()) / self.MAX_COLS)
        self.plots_currentTimestep = [each["y_axis"] for each in self.plots.values()]
        self.plotObjects = []
        self.fig = None
        self.axs = None
        self.start_plotting = False
        self.start_server_communication()

    def start_server_communication(self):
        participant_thread = threading.Thread(target=self.participantObject.main)
        participant_thread.start()
        print("participant thread started")
        self.plotting_function()
        # visualization_thread = threading.Thread(target=self.plotting_function)
        # visualization_thread.start()
        # print("viz thread started")

    def plotting_function(self):

        plt.style.use("fivethirtyeight")
        self.fig, self.axs = plt.subplots(
            nrows=self.ROWS,
            ncols=self.MAX_COLS,
            figsize=(15, 10),
            linewidth=5,
            edgecolor="#04253a",
            dpi=50,
        )

        for index, plotData in self.plots.items():
            row = (int(index) - 1) // self.MAX_COLS
            col = (int(index) - 1) % self.MAX_COLS

            if set([plotData["x_axis"], plotData["y_axis"]]).issubset(
                self.participantObject.all_data_seperated_dict.keys()
            ):
                self.axs[row, col].plot(
                    self.participantObject.all_data_seperated_dict[plotData["x_axis"]],
                    self.participantObject.all_data_seperated_dict[plotData["y_axis"]],
                )

        def update_all_plots(i):
            for index, plotData in self.plots.items():
                row = (int(index) - 1) // self.MAX_COLS
                col = (int(index) - 1) % self.MAX_COLS

                self.axs[row, col].cla()

                if set([plotData["x_axis"], plotData["y_axis"]]).issubset(
                    self.participantObject.all_data_seperated_dict.keys()
                ):
                    self.axs[row, col].plot(
                        self.participantObject.all_data_seperated_dict[
                            plotData["x_axis"]
                        ],
                        self.participantObject.all_data_seperated_dict[
                            plotData["y_axis"]
                        ],
                    )

        ani1 = FuncAnimation(self.fig, update_all_plots, interval=1000)
        plt.subplots_adjust(
            left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4
        )
        plt.show()

        #
        #
        #
        # Working Set 1
        #
        #
        # self.fig, self.axs = plt.subplots(
        #     figsize=(15, 10),
        #     linewidth=5,
        #     edgecolor="#04253a",
        #     dpi=50,
        # )
        # if self.start_plotting or set(self.plots_currentTimestep).issubset(
        #     self.participantObject.all_data_df.columns
        # ):
        #     self.start_plotting = True
        #     self.participantObject.all_data_df[self.plots_currentTimestep].plot(
        #         ax=self.axs, subplots=True
        #     )

        # def update(i):
        #     if self.start_plotting or set(self.plots_currentTimestep).issubset(
        #         self.participantObject.all_data_df.columns
        #     ):
        #         self.start_plotting = True
        #         self.participantObject.all_data_df[self.plots_currentTimestep].plot(
        #             ax=self.axs, subplots=True
        #         )

        # ani = FuncAnimation(self.fig, update, interval=2000)
        # plt.show()
        #
        #
        # Working Set 2
        #
        #
        #

        # plt.style.use("fivethirtyeight")
        # self.fig, self.axs = plt.subplots(
        #     nrows=self.ROWS,
        #     ncols=self.MAX_COLS,
        #     figsize=(15, 10),
        #     linewidth=5,
        #     edgecolor="#04253a",
        #     dpi=50,
        # )

        # for index, plotData in self.plots.items():
        #     row = (int(index) - 1) // self.MAX_COLS
        #     col = (int(index) - 1) % self.MAX_COLS

        #     if set([plotData["x_axis"], plotData["y_axis"]]).issubset(
        #         self.participantObject.all_data_df.columns
        #     ):
        #         self.participantObject.all_data_df.plot(
        #             ax=self.axs[row, col], x=plotData["x_axis"], y=plotData["y_axis"]
        #         )

        # def update_all_plots(i):
        #     plt.cla()
        #     for index, plotData in self.plots.items():
        #         row = (int(index) - 1) // self.MAX_COLS
        #         col = (int(index) - 1) % self.MAX_COLS

        #         self.axs[row, col].cla()

        #         if set([plotData["x_axis"], plotData["y_axis"]]).issubset(
        #             self.participantObject.all_data_df.columns
        #         ):
        #             self.participantObject.all_data_df.plot(
        #                 ax=self.axs[row, col],
        #                 x=plotData["x_axis"],
        #                 y=plotData["y_axis"],
        #             )

        # ani1 = FuncAnimation(self.fig, update_all_plots, interval=2000)
        # # plt.subplots_adjust(
        # #     left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4
        # # )
        # plt.show()


if __name__ == "__main__":
    app = VisualizationStandalone()
