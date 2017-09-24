import csv
import pandas as pd
import numpy as np
import re
# import matplotlib.pyplot as plt

murderFile1="murder_data/Murder-2001-2012.csv"
murderFile2="murder_data/Murder-2013.csv"
murderFile3="murder_data/Murder-2015.csv"


kidnappingFile1="kidnapping_data/kidnapping-2001-2012.csv"
kidnappingFile2="kidnapping_data/kidnapping-2013.csv"
kidnappingFile3="kidnapping_data/kidnapping-2014.csv"
kidnappingFile4="kidnapping_data/kidnapping-2015.csv"

rapeFile1="rape_data/rape-2001-2012.csv"
rapeFile2="rape_data/rape-2013.csv"
rapeFile3="rape_data/rape-2015.csv"

populationFile="population.csv"

def murderDataIntegration():
	df1=pd.read_csv(murderFile1)
	df2=pd.read_csv(murderFile2)
	df3=pd.read_csv(murderFile3,encoding = "ISO-8859-1")
	df1=df1[['STATE/UT','GENDER','YEAR','Total']]
	df2=df2[['STATE/UT','GENDER','YEAR','Total']]
	df3=df3[['State/UT','Number of Victims - Total of All Age Groups - T']]

	df1['GENDER']=(df1.loc[df1['GENDER']=='Total'])
	df1=df1.dropna()
	# print(df1.head)
	df2['GENDER']=(df2.loc[df2['GENDER']=='Total'])
	df2=df2.dropna()
	# df3=df3[(df3['State/UT']=="")]
	df3=df3.drop(df3[df3['State/UT'].isin(["TOTAL (STATES)","TOTAL (UTS)","TOTAL (ALL INDIA)"])].index)
	# appending data and renaming
	df=df1.append(df2)
	df=df.drop('GENDER',1)
	df=df.rename(columns={'STATE/UT':'State','YEAR':'Year','Total':'Total'})

	df3['Year']='2015'
	df3=df3.rename(columns={'State/UT':'State','Year':'Year','Number of Victims - Total of All Age Groups - T':'Total'})
	df=df.append(df3)
	return df

def kidnappingDataIntegration():
	df1=pd.read_csv(kidnappingFile1)
	df2=pd.read_csv(kidnappingFile2)
	df3=pd.read_csv(kidnappingFile3)
	df4=pd.read_csv(kidnappingFile4,encoding = "ISO-8859-1")

	df1=df1[['STATE/UT','YEAR','Purpose','Grand Total']]
	df2=df2[['STATE/UT','YEAR','Purpose','Grand Total']]
	df3=df3[['States/UTs','Crime Head','Year','Total_Sex and Age Wise']]
	df4=df4[['State/UT','Grand Total']]

	# changed pupose to purpose in data set and preprocessing the data file 1 & 2
	df1['Purpose']=(df1.loc[df1['Purpose']=='Total'])
	df1=df1.dropna()
	df1=df1.drop('Purpose',1)

	df2['Purpose']=(df2.loc[df2['Purpose']=='Total'])
	df2=df2.dropna()
	df2=df2.drop('Purpose',1)

	df3=(df3.loc[df3['Crime Head']=='2 - Total Kidnapped & abducted'])
	df3=df3.drop(df3[df3['States/UTs'].isin(["Total (States)","Total (UTs)","Total (All India)"])].index)
	df3=df3.dropna()
	df3=df3.drop('Crime Head',1)

	df4=df4.drop(df4[df4['State/UT'].isin(["TOTAL (STATES)","TOTAL (UTS)","TOTAL ALL INDIA"])].index)
	df4['Year']='2015'
	df4=df4.rename(columns={'State/UT':'State','Year':'Year','Grand Total':'Total'})

	# appending the data
	df=df1.append(df2)
	df=df.rename(columns={'STATE/UT':'State','YEAR':'Year','Grand Total':'Total'})
	df3=df3.rename(columns={'States/UTs':'State','Year':'Year','Total_Sex and Age Wise':'Total'})
	df=df.append(df3)
	df=df.append(df4)
	return df

def rapeDataIntegration():
    df1=pd.read_csv(rapeFile1)
    df2=pd.read_csv(rapeFile2)
    df3=pd.read_csv(rapeFile3,encoding = "ISO-8859-1")
    df1=df1[['STATE/UT','YEAR','Crime Head','Total Victims']]
    df2=df2[['STATE/UT','YEAR','Crime Head','Total Victims']]
    df3=df3[['State/UT','Number of Victims (Total Rape Cases) - Total Victims']]
    df1['Crime Head']=(df1.loc[df1['Crime Head']=='Total'])
    df1=df1.dropna()
    df1=df1.drop('Crime Head',1)
    df2['Crime Head']=(df2.loc[df2['Crime Head']=='Total'])
    df2=df2.dropna()
    df2=df2.drop('Crime Head',1)
    df2=df2.drop(df2[df2['STATE/UT'].isin(["Total (State)","Total (All-India)","Total (UTs)"])].index)
    df3=df3.drop(df3[df3['State/UT'].isin(["TOTAL (STATES)","TOTAL (UTS)","TOTAL (ALL INDIA)"])].index)
    df3['Year']='2015'
    df1=df1.rename(columns={'STATE/UT':'State','YEAR':'Year','Total Victims':'Total'})
    df2=df2.rename(columns={'STATE/UT':'State','YEAR':'Year','Total Victims':'Total'})
    df3=df3.rename(columns={'State/UT':'State','Year':'Year','Number of Victims (Total Rape Cases) - Total Victims':'Total'})
    df=df1.append(df2)
    df=df.append(df3)
    return df

#rapeDataIntegration()

def preProcessing():
	rapeData=rapeDataIntegration()
	murderData=murderDataIntegration()
	kidnappingData=kidnappingDataIntegration()
	populationData=pd.read_csv(populationFile)
	rapeData.loc[rapeData.State=="A&N Islands",'State']="A & N Islands"
	murderData.loc[murderData.State=="A&N Islands",'State']="A & N Islands"
	kidnappingData.loc[kidnappingData.State=="A&N Islands",'State']="A & N Islands"
	return(rapeData,murderData,kidnappingData,populationData)
