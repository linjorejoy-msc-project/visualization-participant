import socket
import threading
import json
import datetime
import os

# import pandas as pd

from common_functions import (
    atmosphere_received,
    check_to_run_cycle,
    drag_received,
    field_received,
    format_msg_with_header,
    fuel_flow_received,
    make_all_cycle_flags_default,
    motion_received,
    recv_msg,
    recv_topic_data,
    request_constants,
    send_config,
    send_topic_data,
    thrust_received,
)

# Logging
import logging
import os


class ClientVisualizationClass:
    def __init__(self) -> None:
        self.file_path = os.path.join(
            os.path.abspath(os.curdir), "src\\client_main\\LOGS"
        )

        self.HEADERSIZE = 5
        self.CONFIG_DATA = {
            "id": "CLIENT_7",
            "name": "visualization",
            "subscribed_topics": [
                "motion",
                "field",
                "thrust",
                "fuel_flow",
                "drag",
                "atmosphere",
            ],
            "published_topics": [],
            "constants_required": [],
            "variables_subscribed": [],
        }

        self.server_socket: socket.socket = None  #

        self.CONSTANTS = {}

        self.cycle_flags = {
            "motion": False,
            "field": False,
            "thrust": False,
            "fuel_flow": False,
            "drag": False,
            "atmosphere": False,
        }
        self.topic_func_dict = {
            "motion": motion_received,
            "field": field_received,
            "thrust": thrust_received,
            "fuel_flow": fuel_flow_received,
            "drag": drag_received,
            "atmosphere": atmosphere_received,
        }

        # to store data received
        self.data_dict = {}

        self.all_data_list = []

        # self.all_data = {}
        self.all_data_seperated_dict = {}
        self.all_data_combined_dict = {}
        # self.all_data_df = pd.DataFrame()
        self.convert_df_period = 5
        self.current_period_cycle = 0

        # Filepaths and mkdir
        self.data_dir = os.path.join(os.path.curdir, "src/data")
        self.folder_name = os.path.join(
            self.data_dir, str(datetime.datetime.now()).replace(":", "-")
        )
        os.mkdir(path=self.folder_name)
        self.log_file = os.path.join(self.folder_name, "logs_visualization.log")
        self.all_data_json_file = os.path.join(
            self.folder_name, "all_data_seperated_dict.json"
        )
        self.all_data_combined_json_file = os.path.join(
            self.folder_name, "all_data_combined_dict.json"
        )

        self.FORMAT = "%(levelname)-10s %(asctime)s: %(message)s"
        logger = logging.getLogger("matplotlib")
        logging.basicConfig(
            handlers=[
                logging.FileHandler(filename=self.log_file, encoding="utf-8", mode="w")
            ],
            level=logging.DEBUG,
            format=self.FORMAT,
        )
        logger.setLevel(logging.WARNING)

    def run_one_cycle(self):
        # global data_dict
        # self.all_data[self.data_dict["currentTimestep"]] = self.data_dict.copy()

        for each_key in self.data_dict.keys():
            if each_key in self.all_data_seperated_dict.keys():
                self.all_data_seperated_dict[each_key].append(self.data_dict[each_key])
            else:
                self.all_data_seperated_dict[each_key] = [self.data_dict[each_key]]

        self.all_data_combined_dict[
            f"{self.data_dict['versions']}.{self.data_dict['currentTimestep']}"
        ] = self.data_dict.copy()

        # self.all_data_list.append(self.data_dict.copy())
        # self.current_period_cycle += 1
        # if self.current_period_cycle == self.convert_df_period:
        #     self.all_data_df = pd.DataFrame.from_dict(self.all_data_list)
        #     self.current_period_cycle = 0
        # self.all_data_df = pd.concat(
        #     [
        #         self.all_data_df,
        #         pd.DataFrame(self.data_dict, index=[self.data_dict["currentTimestep"]]),
        #     ]
        # )
        # self.all_data_df = self.all_data_df.append(self.data_dict, ignore_index=True)
        logging.debug(
            f"Timestep: {self.data_dict['currentTimestep']:5}-{self.data_dict}"
        )
        if self.data_dict["currentTimestep"] == 246:
            with open(self.all_data_json_file, mode="w") as json_file:
                json.dump(self.all_data_seperated_dict, json_file, indent=2)
            with open(self.all_data_combined_json_file, mode="w") as combined_json_file:
                json.dump(self.all_data_combined_dict, combined_json_file, indent=2)
        # print(f"Timestep: {self.data_dict['currentTimestep']:5}-{self.data_dict}")

    def run_cycle(self):
        # global cycle_flags
        while True:
            if check_to_run_cycle(self.cycle_flags):
                make_all_cycle_flags_default(self.cycle_flags)
                self.run_one_cycle()

    def listen_analysis(self):
        # global data_dict
        # global cycle_flags
        logging.info(f"Started Listening for analysis")
        while True:
            topic, sent_time, recv_time, info = recv_topic_data(self.server_socket)
            if topic in self.cycle_flags.keys():
                self.cycle_flags[topic] = True
                self.topic_func_dict[topic](self.data_dict, sent_time, recv_time, info)
            else:
                logging.error(
                    f"{self.CONFIG_DATA['name']} is not subscribed to {topic}"
                )

    # Helper Functions

    def listening_function(self, server_socket):
        # global CONFIG_DATA
        # global CONSTANTS

        while True:
            try:
                msg = recv_msg(server_socket)
                if msg == "CONFIG":
                    send_config(server_socket, self.CONFIG_DATA)
                    self.CONSTANTS = request_constants(server_socket)
                elif msg == "START":
                    analysis_listening_thread = threading.Thread(
                        target=self.listen_analysis
                    )
                    analysis_listening_thread.start()
                    break
            except Exception as e:
                logging.error(f"listening_function error: {str(e)}")
                break
        self.run_cycle()

    def main(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server_socket.connect(("192.168.1.2", 1234))
        self.server_socket.connect(("localhost", 1234))

        listening_thread = threading.Thread(
            target=self.listening_function, args=(self.server_socket,)
        )

        listening_thread.start()


if __name__ == "__main__":
    obj = ClientVisualizationClass()
    obj.main()
