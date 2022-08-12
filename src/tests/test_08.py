import json
import pandas as pd
import os

folder_name = os.path.join(os.path.curdir, "src/data/2022-08-12 11-23-53.598013")

all_data_dict = os.path.join(folder_name, "all_data_seperated_dict.json")
csv_file = os.path.join(folder_name, "extracted_data.csv")

with open(all_data_dict, mode="r") as all_data_json_file, open(
    csv_file, mode="w"
) as csv_file:
    json_data = json.load(all_data_json_file)
    df = pd.DataFrame(json_data)

    df.to_csv(csv_file, index=False, line_terminator="\n")
