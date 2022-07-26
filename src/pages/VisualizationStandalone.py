import logging
import math
import threading
import time


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
            "3": {
                "title": "Drag vs Timestep",
                "y_axis": "drag",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 1000,
            },
            "4": {
                "title": "MassflowRate vs Timestep",
                "y_axis": "currentMassFlowRate",
                "x_axis": "currentTimestep",
                "xlabel": "Drag",
                "ylabel": "Current Timestep",
                "interval": 1000,
            },
        }

        self.MAX_COLS = 2
        self.ROWS = math.ceil(len(self.plots.keys()) / self.MAX_COLS)

        self.plotObjects = []
        self.fig = None
        self.axs = None
        self.start_server_communication()

    def start_server_communication(self):
        participant_thread = threading.Thread(target=self.participantObject.main)
        participant_thread.start()
        print("participant thread started")
        visualization_thread = threading.Thread(target=self.plotting_function)
        visualization_thread.start()
        print("viz thread started")

    # def update_all_plots(self, i):
    #     plt.cla()
    #     print("Updating Once")
    #     for index, plotData in self.plots.items():
    #         row = (int(index) - 1) // self.MAX_COLS
    #         col = (int(index) - 1) % self.MAX_COLS

    #         # self.axs[row, col].cla()
    #         if set([plotData["x_axis"], plotData["y_axis"]]).issubset(
    #             self.participantObject.all_data_df.columns
    #         ):
    #             self.axs[row, col].plot(
    #                 self.participantObject.all_data_df[plotData["x_axis"]],
    #                 self.participantObject.all_data_df[plotData["y_axis"]],
    #             )
    #     plt.show()

    def plotting_function(self):
        # plt.switch_backend("agg")
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

            if (
                plotData["x_axis"] in self.participantObject.all_data_df.columns
                and plotData["y_axis"] in self.participantObject.all_data_df.columns
            ):
                self.axs[row, col].plot(
                    self.participantObject.all_data_df[plotData["x_axis"]],
                    self.participantObject.all_data_df[plotData["y_axis"]],
                )

        def update_all_plots(i):
            plt.cla()
            print("Updating Once")
            for index, plotData in self.plots.items():
                row = (int(index) - 1) // self.MAX_COLS
                col = (int(index) - 1) % self.MAX_COLS

                self.axs[row, col].cla()
                # print(
                #     f"Checking if {plotData['x_axis']} and {plotData['y_axis']} is in {self.participantObject.all_data_df.columns}"
                # )
                if (
                    plotData["x_axis"] in self.participantObject.all_data_df.columns
                    and plotData["y_axis"] in self.participantObject.all_data_df.columns
                ):
                    # print(
                    #     self.participantObject.all_data_df[
                    #         plotData["x_axis"], plotData["y_axis"]
                    #     ].iloc[-1:]
                    # )
                    self.axs[row, col].plot(
                        self.participantObject.all_data_df[plotData["x_axis"]],
                        self.participantObject.all_data_df[plotData["y_axis"]],
                    )
            # plt.show()

        ani1 = FuncAnimation(self.fig, update_all_plots, interval=plotData["interval"])
        plt.subplots_adjust(
            left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4
        )
        plt.show()


if __name__ == "__main__":
    app = VisualizationStandalone()
