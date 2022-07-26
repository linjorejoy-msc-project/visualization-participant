import pandas as pd
import matplotlib.pyplot as plt

plots = {
    "1": {
        "title": "Drag vs Timestep",
        "y_axis": "drag",
        "x_axis": "currentTimestep",
        "xlabel": "Drag",
        "ylabel": "Current Timestep",
        "interval": 100,
    },
    "3": {
        "title": "MassflowRate vs Timestep",
        "y_axis": "currentMassFlowRate",
        "x_axis": "currentTimestep",
        "xlabel": "Drag",
        "ylabel": "Current Timestep",
        "interval": 100,
    },
}

each_data_1 = {
    "drag": 0.030623872735503047,
    "currentThrust": 123191000.0,
    "currentTimestep": 246,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": -12211.083762233648,
    "currentFuelMass": -2035.1806270338593,
    "currentRocketTotalMass": 416753.73561074864,
    "netThrust": 119102645.82303469,
    "currentAcceleration": 285.7866304389351,
    "currentVelocityDelta": 285.7866304389351,
    "currentVelocity": 9357.821882473534,
    "currentAltitudeDelta": 9357.821882473534,
    "currentAltitude": 497144.33627684374,
    "requiredThrustChange": 3.318711737842303,
}
each_data_2 = {
    "drag": 0.24921595137990143,
    "currentThrust": 123191000.0,
    "currentTimestep": 232,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 355331.2448720619,
    "currentFuelMass": 59221.87414534872,
    "currentRocketTotalMass": 845553.1190174269,
    "netThrust": 114595657.7601349,
    "currentAcceleration": 130.78984047486628,
    "currentVelocityDelta": 130.78984047486628,
    "currentVelocity": 6437.339837771575,
    "currentAltitudeDelta": 6437.339837771575,
    "currentAltitude": 380102.71094946255,
    "requiredThrustChange": 6.977248532656683,
}
each_data_3 = {
    "drag": 0.2150982454684128,
    "currentThrust": 123191000.0,
    "currentTimestep": 233,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 329078.2213981836,
    "currentFuelMass": 54846.370233035675,
    "currentRocketTotalMass": 814924.5916312356,
    "netThrust": 114896123.6532231,
    "currentAcceleration": 135.88279798049575,
    "currentVelocityDelta": 135.88279798049575,
    "currentVelocity": 6573.22263575207,
    "currentAltitudeDelta": 6573.22263575207,
    "currentAltitude": 386675.9335852146,
    "requiredThrustChange": 6.733346061625364,
}
each_data_4 = {
    "drag": 0.18558522425137416,
    "currentThrust": 123191000.0,
    "currentTimestep": 234,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 302825.19792430534,
    "currentFuelMass": 50470.866320722635,
    "currentRocketTotalMass": 784296.0642450443,
    "netThrust": 115497055.42417088,
    "currentAcceleration": 147.26206172581934,
    "currentVelocityDelta": 147.26206172581934,
    "currentVelocity": 6861.843285406142,
    "currentAltitudeDelta": 6861.843285406142,
    "currentAltitude": 400252.3580943011,
    "requiredThrustChange": 6.245541131924506,
}
each_data_5 = {
    "drag": 0.16006294399499985,
    "currentThrust": 123191000.0,
    "currentTimestep": 235,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 276572.17445042706,
    "currentFuelMass": 46095.36240840959,
    "currentRocketTotalMass": 753667.536858853,
    "netThrust": 115797521.30335172,
    "currentAcceleration": 153.64536170149293,
    "currentVelocityDelta": 153.64536170149293,
    "currentVelocity": 7015.488647107635,
    "currentAltitudeDelta": 7015.488647107635,
    "currentAltitude": 407267.8467414087,
    "requiredThrustChange": 6.001638672182453,
}
each_data_6 = {
    "drag": 0.13799855272892628,
    "currentThrust": 123191000.0,
    "currentTimestep": 236,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 250319.15097654882,
    "currentFuelMass": 41719.85849609655,
    "currentRocketTotalMass": 723039.0094726617,
    "netThrust": 116097987.17907465,
    "currentAcceleration": 160.5694653511836,
    "currentVelocityDelta": 160.5694653511836,
    "currentVelocity": 7176.058112458819,
    "currentAltitudeDelta": 7176.058112458819,
    "currentAltitude": 414443.9048538675,
    "requiredThrustChange": 5.757736215247344,
}
each_data_7 = {
    "drag": 0.11892966494203812,
    "currentThrust": 123191000.0,
    "currentTimestep": 237,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 224066.12750267057,
    "currentFuelMass": 37344.35458378351,
    "currentRocketTotalMass": 692410.4820864704,
    "netThrust": 116398453.05180205,
    "currentAcceleration": 168.10613944065892,
    "currentVelocityDelta": 168.10613944065892,
    "currentVelocity": 7344.164251899478,
    "currentAltitudeDelta": 7344.164251899478,
    "currentAltitude": 421788.06910576695,
    "requiredThrustChange": 5.513833760743842,
}
each_data_8 = {
    "drag": 0.10245511964821517,
    "currentThrust": 123191000.0,
    "currentTimestep": 238,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 197813.10402879232,
    "currentFuelMass": 32968.85067147047,
    "currentRocketTotalMass": 661781.954700279,
    "netThrust": 116698918.92193514,
    "currentAcceleration": 176.3404367451936,
    "currentVelocityDelta": 176.3404367451936,
    "currentVelocity": 7520.504688644672,
    "currentAltitudeDelta": 7520.504688644672,
    "currentAltitude": 429308.5737944116,
    "requiredThrustChange": 5.269931308346274,
}
each_data_9 = {
    "drag": 0.08822694294723944,
    "currentThrust": 123191000.0,
    "currentTimestep": 239,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 171560.08055491408,
    "currentFuelMass": 28593.34675915743,
    "currentRocketTotalMass": 631153.4273140877,
    "netThrust": 116999384.78982185,
    "currentAcceleration": 185.3739197578629,
    "currentVelocityDelta": 185.3739197578629,
    "currentVelocity": 7705.878608402534,
    "currentAltitudeDelta": 7705.878608402534,
    "currentAltitude": 437014.4524028142,
    "requiredThrustChange": 5.0260288577722,
}
each_data_10 = {
    "drag": 0.07594335923508912,
    "currentThrust": 123191000.0,
    "currentTimestep": 240,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 145307.05708103583,
    "currentFuelMass": 24217.84284684439,
    "currentRocketTotalMass": 600524.8999278964,
    "netThrust": 117299850.65576397,
    "currentAcceleration": 195.32887090917941,
    "currentVelocityDelta": 195.32887090917941,
    "currentVelocity": 7901.2074793117135,
    "currentAltitudeDelta": 7901.2074793117135,
    "currentAltitude": 444915.6598821259,
    "requiredThrustChange": 4.78212640877664,
}
each_data_11 = {
    "drag": 0.06534271531926643,
    "currentThrust": 123191000.0,
    "currentTimestep": 241,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 119054.03360715759,
    "currentFuelMass": 19842.338934531348,
    "currentRocketTotalMass": 569896.3725417051,
    "netThrust": 117600316.52002317,
    "currentAcceleration": 206.35386043173514,
    "currentVelocityDelta": 206.35386043173514,
    "currentVelocity": 8107.561339743449,
    "currentAltitudeDelta": 8107.561339743449,
    "currentAltitude": 453023.22122186935,
    "requiredThrustChange": 4.538223961147189,
}
each_data_12 = {
    "drag": 0.05619819924641167,
    "currentThrust": 123191000.0,
    "currentTimestep": 242,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 92801.01013327934,
    "currentFuelMass": 15466.835022218307,
    "currentRocketTotalMass": 539267.8451555138,
    "netThrust": 117900782.38282621,
    "currentAcceleration": 218.63121163626218,
    "currentVelocityDelta": 218.63121163626218,
    "currentVelocity": 8326.19255137971,
    "currentAltitudeDelta": 8326.19255137971,
    "currentAltitude": 461349.4137732491,
    "requiredThrustChange": 4.294321514699768,
}
each_data_13 = {
    "drag": 0.04831325098538948,
    "currentThrust": 123191000.0,
    "currentTimestep": 243,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 66547.9866594011,
    "currentFuelMass": 11091.331109905266,
    "currentRocketTotalMass": 508639.31776932254,
    "netThrust": 118201248.2443697,
    "currentAcceleration": 232.38716338868673,
    "currentVelocityDelta": 232.38716338868673,
    "currentVelocity": 8558.579714768397,
    "currentAltitudeDelta": 8558.579714768397,
    "currentAltitude": 469907.99348801747,
    "requiredThrustChange": 4.050419069274784,
}
each_data_14 = {
    "drag": 0.04151757552828103,
    "currentThrust": 123191000.0,
    "currentTimestep": 244,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 40294.96318552285,
    "currentFuelMass": 6715.827197592224,
    "currentRocketTotalMass": 478010.79038313124,
    "netThrust": 118501714.10482392,
    "currentAcceleration": 247.90593954969805,
    "currentVelocityDelta": 247.90593954969805,
    "currentVelocity": 8806.485654318096,
    "currentAltitudeDelta": 8806.485654318096,
    "currentAltitude": 478714.4791423356,
    "requiredThrustChange": 3.8065166247340168,
}
each_data_15 = {
    "drag": 0.03566368074717952,
    "currentThrust": 123191000.0,
    "currentTimestep": 245,
    "currentMassFlowRate": 30628.52738619129,
    "currentOxidiserMass": 14041.939711644602,
    "currentFuelMass": 2340.3232852791825,
    "currentRocketTotalMass": 447382.26299693994,
    "netThrust": 118802179.96433634,
    "currentAcceleration": 265.5495977165034,
    "currentVelocityDelta": 265.5495977165034,
    "currentVelocity": 9072.035252034599,
    "currentAltitudeDelta": 9072.035252034599,
    "currentAltitude": 487786.5143943702,
    "requiredThrustChange": 3.562614180957752,
}


data_list = [
    each_data_2,
    each_data_3,
    each_data_4,
    each_data_5,
    each_data_6,
    each_data_7,
    each_data_8,
    each_data_9,
]


df = pd.DataFrame(data_list)
df2 = pd.DataFrame()
print(df2)
df2 = pd.concat(
    [
        df2,
        pd.DataFrame(each_data_13, index=[len(df2)]),
    ]
)
df2 = pd.concat(
    [
        df2,
        pd.DataFrame(each_data_14, index=[len(df2)]),
    ]
)
df2 = pd.concat(
    [
        df2,
        pd.DataFrame(each_data_15, index=[len(df2)]),
    ]
)
print(df2)

# print(df)

# print()

# df = df.append(each_data_15, ignore_index=True)
# print(df)

# each_data_15["currentThrust"] = 233
# df = df.append(each_data_15, ignore_index=True)
# print(df)

# df = pd.concat(
#     [
#         df,
#         pd.DataFrame(each_data_15, index=[len(df)]),
#     ]
# )


# print(df)
# fig, axs = plt.subplots(
#     nrows=3,
#     ncols=2,
#     figsize=(12, 6),
#     linewidth=5,
#     edgecolor="#04253a",
#     dpi=55,
# )

# axs[0, 0].plot(df["currentTimestep"], df["drag"])
# axs[0, 1].plot(df["currentTimestep"], df["currentMassFlowRate"])
# axs[1, 0].plot(df["currentTimestep"], df["currentOxidiserMass"])
# axs[1, 1].plot(df["currentTimestep"], df["currentFuelMass"])
# axs[2, 0].plot(df["currentTimestep"], df["currentVelocityDelta"])
# axs[2, 1].plot(df["currentTimestep"], df["requiredThrustChange"])

print(df["drag", "currentTimestep"])

# df.plot(
#     ax=axs[0, 0],
#     kind="line",
#     x="currentTimestep",
#     y="drag",
#     subplots=True,
#     figsize=(12, 6),
#     linewidth=5,
# )

# df["currentTimestep"].plot(
#     ax=axs[0, 0],
#     kind="line",
#     subplots=True,
#     figsize=(12, 6),
#     linewidth=5,
# )

plt.show()

# all_data = {}

# for each_data in data_list:
#     all_data[each_data["currentTimestep"]] = each_data


# #
# x_data = [each_data_dict["currentTimestep"] for each_data_dict in all_data.values()]
# y_data = [each_data_dict["drag"] for each_data_dict in all_data.values()]

# print(x_data)
# print(y_data)

# for index, plotData in plots.items():
#     print(index)
#     print(plotData)
#     print()
