# from langchain_helper import get_plotting_agent
# import json

# plotter = get_plotting_agent()
# # ans = plotter.invoke("Plot a bar chart on gender column? and don't return imgur link as output instead return in the format as JSON: chart type, data, label and title?")
# ans = plotter.invoke("Plot a bar chart on gender column? and don't use plotly and don't return imgur link as output instead return in the format of chart js?")
# print(ans["output"])

# # {'chartType': 'bar', 'data': [['Female', 5075], ['Male', 4925]], 'labels': ['Female', 'Male'], 'title': 'Patients by Gender'}

# data = json.loads(ans["output"])
# print(data)