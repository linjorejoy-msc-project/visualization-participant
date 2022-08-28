import json
import pandas as pd
import os

folder_name = os.path.join(os.path.curdir, "src/data/2022-08-13 13-36-28.504380")

all_data_dict = os.path.join(folder_name, "all_data_seperated_dict.json")
all_data_dict_combined = os.path.join(folder_name, "all_data_combined_dict.json")

csv_file = os.path.join(folder_name, "extracted_data.csv")
csv_file_combined = os.path.join(folder_name, "all_data_combined_dict.csv")

with open(all_data_dict, mode="r") as all_data_json_file, open(
    csv_file, mode="w"
) as csv_file_fp, open(
    all_data_dict_combined, mode="r"
) as all_data_combined_json_file, open(
    csv_file_combined, mode="w"
) as csv_file_combined_fp:

    json_data = json.load(all_data_json_file)
    df = pd.DataFrame(json_data)

    json_data_combined = json.load(all_data_combined_json_file)
    df_combined = pd.DataFrame.from_dict(json_data_combined, orient="index")
    df_combined.index.name = "branch_timestep"
    # print(df_combined["branch_timestep"])
    # df_combined.set_index("branchtimestep")
    # df_combined["branch_timestep"] = df_combined["currentTimestep"].apply(str)
    # print(df_combined)

    df.to_csv(csv_file_fp, line_terminator="\n")
    df_combined.to_csv(csv_file_combined_fp, line_terminator="\n")
