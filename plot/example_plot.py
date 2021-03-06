import plotly.graph_objects as go
import plotly
import pandas as pd
import csv
import itertools

# prototype building model parameters
bldg_type = ['SmallOffice','MediumOffice','LargeOffice','SmallRetail','MediumRetail']
bldg_vintage = ['pre1980','post1980','2004','2010','2016']
climate_loc = ['2A','2B','3A','3B','4A']
bldg_cons = ['MassWall','SteelFramed']
bldg_mass = ['LM','MM','HM']
hvac_plant = ['WaterCooled','AirCooled','RTU','HeatPump']
hvac_type = ['VAV','PSZ']
hvac_tstat = [70,71,72,73,74,75,76]
# BldgUse = ['Fixed','Stochastic']
# DF measure parameters for GTA and lighting
event_start = list(range(6,22)) # 6am to 10pm
event_hours = [2,4,6]
precool_hours = [2,4,6]
precool_degF = [0,2,4]
reset_degF = [0,2,4,6]

# a = itertools.product(*[BldgType, BldgVint])
# print(list(a))
#
with open('df_model_list.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(
        ['model_Id', 'hvac_tstat', 'event_start', 'event_hours', 'precool_hours', 'precool_degF', 'reset_degF'])
    for tstat in hvac_tstat:
        for eventStart in event_start:
            for eventHours in event_hours:
                if (eventStart + eventHours) <= 22:
                    for precoolHours in precool_hours:
                        for precool in precool_degF:
                            if (tstat - precool) >= 70:
                                for reset in reset_degF:
                                    if (tstat + reset) <= 80:
                                        measureID = 'DF_{}_{}_{}_{}_{}_{}'.format(tstat, eventStart, eventHours,
                                                                                  precool_hours, precool, reset)
                                        writer.writerow([measureID, tstat, eventStart, eventHours, precoolHours,
                                                         precool, reset])
                                    else:
                                        pass
                            else:
                                pass
                else:
                    pass

# with open('df_model_list.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerow(['model_Id', 'bldg_type', 'bldg_vintage', 'climate'])
#     for bldg in bldg_type:
#         for vint in bldg_vintage:
#             for loc in climate_loc:
#                 model_Id = 'model_{}_{}_{}'.format(bldg, vint, loc)
#                 writer.writerow([model_Id, bldg, vint, loc])
#
def bldg_type_to_number(argument):
    switcher = {'SmallOffice':1,'MediumOffice':2,'LargeOffice':3,'SmallRetail':4,'MediumRetail':5}
    return switcher.get(argument, "nothing")

def bldg_vintage_to_number(argument):
    switcher = {'pre1980':1,'post1980':2,'2004':3,'2010':4,'2016':5}
    return switcher.get(argument, "nothing")

def climate_to_number(argument):
    switcher = {'2A':1,'2B':2,'3A':3,'3B':4,'4A':5}
    return switcher.get(argument, "nothing")

def tstat_to_number(argument):
    switcher = {
        70: 1,
        71: 2,
        72: 3,
        73: 4,
        74: 5,
        75: 6,
        76: 7
    }
    return switcher.get(argument, "nothing")

def event_start_to_number(argument):
    switcher = {
        6: 1,
        7: 2,
        8: 3,
        9: 4,
        10: 5,
        11: 6,
        12: 7,
        13:8,
        14:9,
        15:10,
        16:11,
        17:12,
        18:13,
        19:14,
        20:15,
        21:16
    }
    return switcher.get(argument, "nothing")

def event_hours_to_number(argument):
    switcher = {
        2: 5,
        4: 8,
        6: 11
    }
    return switcher.get(argument, "nothing")

def precool_hours_to_number(argument):
    switcher = {
        4: 6,
        6: 11
    }
    return switcher.get(argument, "nothing")

def precool_deg_to_number(argument):
    switcher = {
        0: 6,
        2: 11
    }
    return switcher.get(argument, "nothing")

def reset_deg_to_number(argument):
    switcher = {
        0: 4,
        2: 7,
        4: 10,
        6: 13
    }
    return switcher.get(argument, "nothing")
#
# df = pd.read_csv("model_list.csv")
# df['bldg_type'] = df.bldg_type.apply(lambda x: bldg_type_to_number(x))
# df['bldg_vintage'] = df.bldg_vintage.apply(lambda x: bldg_vintage_to_number(x))
# df['climate'] = df.climate.apply(lambda x: climate_to_number(x))
#
# fig = go.Figure(data=
# go.Parcoords(
#     line=dict(color = df['bldg_type'],
#               colorscale = [[1,'lightgray'],[0.5,'blue'],[0.5,'red']]),
#     dimensions=list([
#         dict(range=[1, 5],
#              # constraintrange = [1,2], # change this range by dragging the pink line
#              tickvals=[1, 2, 3, 4, 5],
#              label='Building Type ( X 5)', values=df['bldg_type'],
#              ticktext=['Small Office', 'Medium Office', 'Large Office','Small Retail', 'Medium-Large Retail']),
#         dict(range=[1, 5],
#              tickvals=[1, 2, 3, 4, 5],
#              label='Building Vintage ( X 5)', values=df['bldg_vintage'],
#              ticktext=['Pre-1980', '1980-2004', '90.1-2004', '90.1-2010', '90.1-2016']),
#         dict(range=[1, 5],
#              tickvals=[1, 2, 3, 4, 5],
#              label='Climate Zone ( X 5)', values=df['climate'],
#              ticktext=['2A (Hot-Humid)', '2B (Hot-Dry)', '3A (Warm-Humid)', '3B (Warm-Dry)', '4A (Mixed–Humid)'])
#     ])
# )
# )
# fig.update_layout(
#     autosize=False,
#     width=1000,
#     height=600,
#     # title="Prototype building model types, vintages, and climates",
#     font=dict(
#         size=16,
#         color="#7f7f7f",
#     ),
#     margin=go.layout.Margin(
#         l=150,
#         r=100,
#         b=100,
#         t=100,
#         pad=4
#     ),
#     # paper_bgcolor="LightSteelBlue",
# )
#
# fig.show()
# fig.write_image(file="test.png", width=600, height=350, scale=2)
# data=[go.Parcoords(
#     line=dict(color = df['bldg_type'],
#               colorscale = [[1,'lightgray'],[0.5,'blue'],[0.5,'red']]),
#     dimensions=list([
#         dict(range=[1, 5],
#              tickvals=[1, 2, 3, 4, 5],
#              label='Building Type', values=df['bldg_type'],
#              ticktext=['Small Office', 'Medium Office', 'Large Office','Small Retail', 'Medium-Large Retail']),
#         dict(range=[1, 5],
#              tickvals=[1, 2, 3, 4, 5],
#              label='Building Vintage', values=df['bldg_vintage'],
#              ticktext=['Pre-1980', '1980-2004', '90.1-2004', '90.1-2010', '90.1-2016']),
#         dict(range=[1, 5],
#              tickvals=[1, 2, 3, 4, 5],
#              label='Climate Zone', values=df['climate'],
#              ticktext=['2A (Hot-Humid)', '2B (Hot-Dry)', '3A (Warm-Humid)', '3B (Warm-Dry)', '4A (Mixed–Humid)'])
#     ])
# )]
# plotly.offline.plot(data, image_filename='test', image='png',image_height=300, image_width=400)
# fig.show()
df = pd.read_csv("df_model_list.csv")
print(len(df))
# fig = go.Figure(data=
# go.Parcoords(
#     line=dict(color = df['hvac_tstat'],
#               colorscale = [[1,'lightgray'],[0.5,'blue'],[0.5,'red']]),
#     dimensions=list([
#
#         dict(range=[0, 23],
#              # constraintrange = [1,2], # change this range by dragging the pink line
#              tickvals=list(range(0,24)),
#              label='Event Start (x16)', values=df['event_start'],
#              ticktext=['0','1','2','3','4','5','6','7','8','9','10','11','12',
#                        '13','14','15','16','17','18','19','20','21','22','23']),
#         dict(range=[2,6],
#              tickvals=[2,4,6],
#              label='Event Hours (x3)', values=df['event_hours'],
#              ticktext=['2','4','6']),
#         dict(range=[2,6],
#              tickvals=[2,4,6],
#              label='Precooling Hours (x3)', values=df['precool_hours'],
#              ticktext=['2','4', '6']),
#         dict(range=[0,4],
#              tickvals=[0,2,4],
#              label='Precooling Degrees (x3)', values=df['precool_degF'],
#              ticktext=['0', '-2F','-4F']),
#         dict(range=[68,80],
#              tickvals=[70,71,72,73,74,75,76],
#              label='Cooling T-Stat (x3)', values=df['hvac_tstat'],
#              ticktext=['70','71','72','73','74','75','76']),
#         dict(range=[0, 6],
#              tickvals=[0,2,4,6],
#              label='Reset Degrees (x4)', values=df['reset_degF'],
#              ticktext=['0F', '2F','4F','6F'])
#     ])
# )
# )
# fig.update_layout(
#     autosize=False,
#     width=1200,
#     height=600,
#     font=dict(
#         size=16,
#         color="#7f7f7f",
#     ),
#     margin=go.layout.Margin(
#         l=150,
#         r=100,
#         b=100,
#         t=100,
#         pad=4
#     ),
#     # paper_bgcolor="LightSteelBlue",
# )
# fig.show()
# print(len(df))