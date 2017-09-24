# from ipywidgets import widgets 
# from IPython.display import display, clear_output, Image
# from plotly.graph_objs import *
# from plotly.widgets import GraphWidget
# from plotly.graph_objs import graph_objs as go
# import plotly.plotly as py
# import preprocessing

# import datetime
# import numpy as np
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.plotly as py

# from ipywidgets import widgets 
# from IPython.display import display, clear_output, Image
# from plotly.graph_objs import *
# from plotly.widgets import GraphWidget

# rapeData,murderData,kidnappingData,populationData = preprocessing.preProcessing()
# state = widgets.Dropdown(
#     options=list(kidnappingData['State'].unique()),
#     value='Andhra Pradesh',
#     description='Colour:',
# )
# def validate():
# 	if state.value in kidnappingData['State'].unique():
# 		return True
# 	else:
# 		return False
# def response(change):
	
# state.observe(response, names="value")
# # generate a function to handle changes in the widget
# def update_on_change(change):
#    go.restyle({'marker.color': change['new']})
    
# # set a listener for changes to the dropdown widget    
# w.observe(update_on_change, names="selected_label")

# display(w)
# display(go)
# import plotly
# plotly.tools.set_credentials_file(username='vatsal-sodha', api_key='YtT52QNSc1K2iSzr9rs6')
# 
# 
import matplotlib.pyplot as plt
import preprocessing
from menu import *
rapeData,murderData,kidnappingData,populationData = preprocessing.preProcessing()
rapeYear=rapeData['Year'].unique()
kidnappingYear=kidnappingData['Year'].unique()
murderYear=murderData['Year'].unique()

# stateCrimeData=(rapeData[rapeData['State']=='Gujarat'][:])
# statePopulation=populationData[populationData['State']=='Gujarat'][:]
# y=stateCrimeData["Total"]
# plt.plot(x,y,'o-', color="b",label="Linear-Regression score")
# plt.show()

fig = plt.figure()
fig.subplots_adjust(left=0.3)
props = ItemProperties(labelcolor='black', bgcolor='orange',
                       fontsize=15, alpha=0.2)
hoverprops = ItemProperties(labelcolor='white', bgcolor='blue',
                            fontsize=15, alpha=0.2)

# fig1 = plt.figure()
# fig1.subplots_adjust(left=0.3)
# props1 = ItemProperties(labelcolor='black', bgcolor='orange',
#                        fontsize=15, alpha=0.2)
# hoverprops1 = ItemProperties(labelcolor='white', bgcolor='blue',
#                             fontsize=15, alpha=0.2)

# menuitems1 = []
# for label1 in ('rape','murder','kidnapping'):
# 	label1=str(label1)
# 	def on_select(item1):

# 		# stateCrimeData=rapeData[rapeData['State']==item.labelstr][:]
# 		y=stateCrimeData["Total"]
# 		print(item.labelstr)
# 		plt.cla()
# 		# print(y)
# 		plt.title("Crime In "+item1.labelstr)
# 		plt.xlabel("Year")
# 		plt.ylabel("No of crimes")
# 		plt.plot(x,y)
# 		plt.show()
# 	item1 = MenuItem(fig, label1, props=props, hoverprops=hoverprops,
#                     on_select=on_select)
# 	menuitems1.append(item1)
# 	menu1 = Menu(fig, menuitems1)
# plt.show()
menuitems=[]
for label in list(rapeData['State'].unique()):
	label=str(label)
	def on_select(item):
		stateCrimeDataRape=rapeData[rapeData['State']==item.labelstr][:]
		stateCrimeDataKidnapping=kidnappingData[kidnappingData['State']==item.labelstr][:]
		stateCrimeDataMurder=murderData[murderData['State']==item.labelstr][:]

		# y=stateCrimeData["Total"]
		# print(item.labelstr)
		plt.cla()
		# print(y)
		plt.title("Crime In "+item.labelstr)
		plt.xlabel("Year")
		plt.ylabel("No of crimes")
		plt.plot(rapeYear,stateCrimeDataRape["Total"],'o-', color="b",label="Rape Data")
		plt.plot(kidnappingYear,stateCrimeDataKidnapping["Total"],'o-', color="g",label="Kidnapping data")
		plt.plot(murderYear,stateCrimeDataMurder["Total"],'o-', color="m",label="Murder Data")
		plt.legend(loc="best")
		
		plt.show()
	item = MenuItem(fig, label, props=props, hoverprops=hoverprops,
                    on_select=on_select)
	menuitems.append(item)
	menu = Menu(fig, menuitems)
plt.show()

# print(len(list(stateCrimeData['Total'])))
# print(type(stateCrimeData['Total']))
# stateCrimeData['percentage']=0
# for i in range(0,len(list(stateCrimeData['Total']))):
# 	value=float((stateCrimeData['Total'].values[i])*100)/((float(statePopulation["Growth"].values)/100)*i+float(statePopulation['Population-2001'].values))
# 	print(value)
# 	stateCrimeData.set_value(i,'percentage',value)
# print(stateCrimeData.head)


