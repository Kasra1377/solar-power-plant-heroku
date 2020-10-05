import numpy as np
import pandas as pd
import streamlit as st
#-------------------------------------------------------------------------

st.write("""# Solar Power Generation Dataset Ananlysis
In this web application we are going to analyze solar power generation dataset with multiple aspects.Lets get started...
""")
st.write('---')

html_table = """<a id="top"></a>
<div class="list-group" id="list-tab" role="tablist">
<h3 class="list-group-item list-group-item-action active" data-toggle="list"  role="tab" aria-controls="home">Table Of Contents</h3>"""
st.markdown(html_table, unsafe_allow_html = True)

html_content = ("""

<font color="black" size=+1><b>Reminder on PV Systems</b></font>
* [1. Reminder on PV Systems](#0)
* [2. PV Inverter](#1)

<font color="black" size=+1><b>Initial Overview of Dataset</b></font>
* [1. Initial Overview of Dataset](#2)
* [2. Dataset General Information](#3)
* [3. Dataset Manipulation and Feature Engineering](#4)

<font color="black" size=+1><b>Analyzing Solar Power Plant Dataset</b></font>
* [-. Analyzing Solar Power Plant Dataset](#5)
* [1. DC Power Mean Per Hour](#6)
* [2. Daily Yield Mean Per Hour](#7)
* [3. Daily Yield Mean Per Date](#8)

<font color="black" size=+1><b>Weather Sensor Dataset</b></font>
* [-. Weather Sensor Dataset](#9)
* [-. Dataset General information](#10)
* [4. Ambient Temperature Mean per Hour](#11)
* [5. Module Temperature Mean per Hour](#12)
* [6. Irradiation Mean per Hour](#13)

<font color="black" size=+1><b>Feature Correlation and Relationship</b></font>

* [-. Feature Correlation and Relationship](#14)
* [1. Ambient Temperature and Module Temperature Correlation](#15)
* [2. DC Power and Module Temperature Correlation](#16)
* [3. DC Power Temperature and Ambient Temperature Correlation](#17)
* [4. DC Power Temperature and Irradiation Correlation](#18)
* [5. DC Power Temperature and AC Power Correlation](#19)

<font color="black" size=+1><b>Predicting DC Power with Linear Regression</b></font>

* [-. Predicting DC Power with Linear Regression](#20)
""")
st.markdown(html_content, unsafe_allow_html = True)


st.write('---')

st.subheader('Reminder on PV systems')
html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

html_str = """<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a0/From_a_solar_cell_to_a_PV_system.svg" width="450"><br/>
</center>"""
st.markdown(html_str, unsafe_allow_html = True)
#st.write('![alt text](https://upload.wikimedia.org/wikipedia/commons/a/a0/From_a_solar_cell_to_a_PV_system.svg "DC Power Mean Per Hour")')

st.write("""
`PV system` is a power system designed to supply usable solar power by means of photovoltaics.

`PV Cell` is an electrical device that converts the energy of light directly into electricity by the photovoltaic effect, which is a physical and chemical phenomenon. It is also the basics photovoltaic device that is the building block PV modules.

`Photovoltaic` effect is the generation of voltage and electric current in a material upon exposure to light.

`PV module` is a group of PV cell connected in serie and/or parallel and encapsulated in an environmentally protective laminate.

`PV panel` is a group of modules that is the basic building block of a PV array.

`PV array` is a group of panels that comprises the complete PV generating unit.

""")

st.write('---')
st.subheader('PV inverter')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

html_str = """<center>
<img src="https://www.futuregenerationenergy.ie/wp-content/uploads/2017/03/santnu_new.jpg" width="450"><br/>
</center>"""
st.markdown(html_str, unsafe_allow_html = True)

st.write("""
`PV inverter` convert battery or PV array DC power to AC power for use with conventional utility-powered appliances. It is heart of PV systems because PV array is a DC source, an inverter is required to convert the dc power to normal ac power that is used in our homes and offices.

`PV systems` are very influenced by weather condition, if the weather is good, we get a maximun yield but if the weather is bad, we get a minimun yield. That is why there is important to know how weather condition can impact on yield of the two solar power plants.""")

st.write('---')
st.write("""
According to the notion of PV systems, the important feature are:

* **DC power**

* **AC power**

* **Yield**

* **Ambiant Temperature**

* **Module temperature**

* **Irradiation**

""")


st.write('---')
st.subheader('Initial overview of Dataset')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('first of all we have to import our dataset :')
df = pd.read_csv('E:\Datasets\Plant_1_Generation_Data.csv')
st.write(df)
st.write("""* This dataset has `68778` rows and `7` columns.

The name of columns are :

> 1. **DATE_TIME** : The date and the time that features was recorded


> 2. **PLANT_ID** : The ID of the solar plant.In this dataset the features was recorded from one unique solar plant.

> 3. **SOURCE_KEY** : The source key(ID) of the inverters.Note that this solar power plant has **22 inverters**.

> 4. **DC_POWER**(kW) : The DC power of solar plant in that particular time and date.

> 5. **AC_POWER**(kW) : The DC power of solar plant in that particular time and date.

> 6. **DAILY_YIELD**

> 7. **TOTAL_YIELD**


""")
st.write('---')
st.subheader('Dataset Genreral Information')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Lets take a look at general information of the dataset : ')
st.write(df[['DC_POWER' , 'AC_POWER' , 'DAILY_YIELD' , 'TOTAL_YIELD']].describe())
st.write('* For example DC_POWER have been recorded **68778** times and the mean of all of the samples is about **3147** kW and the standard deviation of them is about **4000** kW and etc.')
st.write('---')
st.subheader('Dataset Manipulation and Feature Engineering')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Lets sum of the features(DC_POWER , AC_POWER ,...) of 22 inverters and we will get this data frame down below : ')

df = df.groupby('DATE_TIME')[['DC_POWER','AC_POWER', 'DAILY_YIELD','TOTAL_YIELD']].agg('sum').reset_index()
df.columns = ['DATE_TIME' , 'DC_POWER' , 'AC_POWER' , 'DAILY_YIELD' , 'TOTAL_YIELD']
st.write(df)

st.write("For easing our data analyzing and processing we split up the `TIME` AND `DATE` components from `DATE_TIME` column and put them into two columns : ")

df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'] , errors='coerce')
df['DATE'] = df['DATE_TIME'].apply(lambda x : x.date())
df['TIME'] = df['DATE_TIME'].apply(lambda x : x.time())
st.write(df)

st.write('---')
st.subheader('Analyzing The Solar Power Plant Dataset')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('In this section we are going go answer the most frequent questions that we ususaly encounter with.')
st.subheader('1. DC Power Mean Per Hour')
st.write('First we have to group `DC_POWER` by time of the day :')
ds = df.groupby(['TIME'])['DC_POWER'].mean().reset_index().sort_values(by = ['TIME'])
ds.columns = ['TIME' , 'DC_POWER']
st.write(ds)

st.write('And then we plot our resulting data : ')
st.write('![alt text](https://img.techpowerup.org/201003/Nzk1OTM2YzJlMzY0.png "DC Power Mean Per Hour")')
st.write('* As we can see from chart above, we have peak values between **11 AM** and **1 PM**.This is because in this hours we have maximum irradiation of sun and then we can get maximum DC power from it.On the other hand Between **6 PM** and **00:00** we have minimum DC power because of lack of sum irradiation.')
st.write('* Every **blue markers** represent a `DC power` value from inverter(22 inverters oveall) in a particular Time of day and the **black line** represents the mean of this markers in a particular time')

st.subheader('Decomposing The Data into Each Date')

st.write('In the next step we are going to decompose this data by each date')
st.write('First we decompose the data by `TIME`(row) , `DATE`(column) and `DC_POWER`(value)')

ds_calendar = df.pivot_table(values = 'DC_POWER', index = 'TIME', columns = 'DATE')
st.write('And we can get the manipulated dataset : ')
st.write(ds_calendar)
st.write('And then we plot our resulting data :')
st.write('![alt text](https://img.techpowerup.org/201003/2644.png "DC Power Mean Per Hour By Each Date")')

st.write('* And again we can see that most of the peak values of DC power takes place between **11 AM** and **1 PM** and between **6 PM** and **5 AM** we have minimum DC power because of shortage of sun irradiation.')
st.write('* As we can see most of the charts are bell shaped(like the previous chart), but we have some exceptions and maybe some of the charts are irrational which originates from this issues :')
st.write("""
> 1. Human error during creating the Dataset

> 2. The error that originates from a sensor that recording the measurements

> 3. The error that originates from a equipment

> 3. Weather Condition(It will be covered in the next section)
""")

st.write('---')
st.subheader('2. Daily Yield Mean Per Hour')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Again we have to group `DAILY_MEAN` by time of the day :')
ds = df.groupby('TIME')['DAILY_YIELD'].mean().reset_index().sort_values(by = 'TIME')
ds.columns = ['TIME' , 'MEAN OF DAILY YIELD']
st.write(ds)

st.write('And then we plot our resulting data : ')
st.write('![alt text](https://img.techpowerup.org/201003/3.png "Daily Yield Mean Per Hour")')
st.write('* As we can observe, in general, yield of solar plant starts increasingly from **7 AM**(sunrise) and it increses gradualy(it has **positive** relationship with **irradiation** of the sun) and reach its peak at about **6 PM**(sunset) and then after sunset the solar plant starts to discharge and it starts to distribute the energy between consumers.As a result the yield drops gradually untill **00:00**.At this time the solar plant doesnt have any energy untill **7 AM**.')

st.subheader('Decomposing The Data into Each Date')
st.write('Like the privious one we want to decompose this chart into each date')
st.write('First we decompose the data by `TIME`(row) , `DATE`(column) and `DAILY_YIELD`(value)')

ds_calendar = df.pivot_table(values = 'DAILY_YIELD', index = 'TIME', columns = 'DATE')
st.write('And we can get the manipulated dataset : ')
st.write(ds_calendar)

st.write('![alt text](https://img.techpowerup.org/201003/4.png "Daily Yiled Mean Per Hour By Each Date")')
st.write('Most of the chart have a certain shape like the previous chart.Like the privious one we have some exceptations that occures in some date.The reason of this exceptations was discussed in the privious section.')
st.write('* Every **blue markers** represent a `Daily Yield` value from inverter(22 inverters oveall) in a particular Time of day and the **black line** represents the mean of this markers in a particular time')

st.subheader('3.Daily Yield Mean Per Date')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Lets group the `DAILY_YIELD` column by each date :')

ds = df.groupby(['DATE'])['DAILY_YIELD'].sum().reset_index().sort_values(by = 'DATE')
ds.columns = ['DATE' , 'DAILY_YIELD']

st.write(ds)

st.write('And then we plot our resulting data :')
st.write('![alt text](https://img.techpowerup.org/201003/55.png "Daily Yield Mean Per Date")')

st.write('* According to chart above, we have maximum daily yield on `2020-05-25` and `2020-06-14`.There are many reasons for this such as **weather consition** and **sun irradiation**.Most likely on this date the weather condition was sunny and for those dates that had minimum values the weather condition was **rainy** our **cloudy**.')

weather_df = pd.read_csv('E:\Datasets\Plant_1_Weather_Sensor_Data.csv')
weather_df.drop(columns = {'PLANT_ID' , 'SOURCE_KEY'} , inplace = True)

st.write('---')
st.subheader('Weather Sensor Dataset')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Lets import another dataset that contains crucial features : ')
st.write(weather_df)

st.write('This dataset contains `3182` rows and `4` columns.')
st.write(r"""
The name of columns are :

> 1. **AMBIENT_TEMPERATURE**(°C) : The teprature of solar power plant ambient in a particular time and date.


> 2. **MODULE_TEMPERATURE**(°C) :  The teprature of solar power plant module in a particular time and date.

> 3. **IRRADIATION**$$( \frac{W}{m^2} )$$ : the process by which an object is exposed to radiation by sun.

""")
st.write('---')
st.subheader('Dataset Genreral Information')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Lets take a look at general information of the dataset : ')
st.write(weather_df.describe())

st.write("For easing our data analyzing and processing we split up the `TIME` AND `DATE` components from `DATE_TIME` column and put them into two columns : ")
weather_df['DATE_TIME'] = pd.to_datetime(weather_df['DATE_TIME'] , errors='coerce')
weather_df['DATE'] = weather_df['DATE_TIME'].apply(lambda x : x.date())
weather_df['TIME'] = weather_df['DATE_TIME'].apply(lambda x : x.time())
st.write(weather_df)
st.write('---')

st.subheader('4. Ambient Temperature Mean Per Hour')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Lets group the `AMBIENT_TEMPRATURE` column by each time of the day :')

day_ambient_mean = weather_df.groupby(['TIME'])['AMBIENT_TEMPERATURE'].mean().reset_index().sort_values(by = 'TIME')
st.write(day_ambient_mean)
st.write('And then we plot our resulting data : ')
st.write('![alt text](https://img.techpowerup.org/201003/download.png "Ambient Temperature Mean Per Hour")')
st.write('* As this chart illustrates, ambient temparature has peak value at **2 PM** because in this this time of day ambient can get **maximum sun irradiation**.And in sunrise time(between **5 AM** and **6 AM**)ambient has minimum temprature.')

st.subheader('Decomposing The Data into Each Date')
st.write('Lets decompose this data by each date')
st.write('First we decompose the data by `TIME`(row) , `DATE`(column) and `AMBIENT_TEMPERATURE`(value) : ')

ambient_mean_calendar = weather_df.pivot_table(values = 'AMBIENT_TEMPERATURE', index = 'TIME', columns = 'DATE')
st.write(ambient_mean_calendar)

st.write('And then we plot our resulting graph : ')
st.write('![alt text](https://img.techpowerup.org/201004/7.png "Ambient Temperature Mean Per Each Date")')
st.write('* As this chart shows,for most days ambient temprature has peak value at **2 PM**.Like the previuos graphs we have some exceptions.For example on `2020-06-05` at about **2 PM** we have a significant drop which shows that the solar power plant did not recieve enough irradiation.This is because in that particular period we had a **rainy** or **cloudy** weather.On the other hand we have **lack of datapoints** in particular date and time(`2020-06-17` for instance),maybe it originates from an **sensor or human** error.')

st.write('![alt text](https://img.techpowerup.org/201004/8.png "Ambient Temprature Mean Per Each Date")')
st.write('---')
st.write('![alt text](https://img.techpowerup.org/201004/9.png "Ambient Temperature Mean Per Each Date")')
st.write('* This two graphs are easy to interpret.For example `2020-05-21` and `2020-05-18` have maximum and minimum ambient temperautre mean in respect.')

st.write('---')
st.subheader('5. Module Temperature Mean Per Hour')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Grouping the `MODULE_TEMPRATURE` column by each time of the day :')
module_daily_mean = weather_df.groupby(['TIME'])['MODULE_TEMPERATURE'].mean().reset_index().sort_values(by = 'TIME')
st.write(module_daily_mean)

st.write('Plotting the dataset : ')
st.write('![alt text](https://img.techpowerup.org/201004/10.png "Module Temperature Mean Per Each Hour")')
st.write('* According to the graph above, the module temperature has the peak value (**55 °C**) at **12 PM** which is normal.Because in this period the module recieves maximum sun irradiation.')
st.write('---')

st.write('![alt text](https://img.techpowerup.org/201004/11.png "Module Temperature Mean Per Each Date")')
st.write('---')
st.write('![alt text](https://img.techpowerup.org/201004/12.png "Module Temperature Mean Per Each Date")')
st.write('* on `2020-05-21` and `2020-05-18` module have maximum and minimum temperature mean in respect, In addition to this previous line graph and bar chart(ambient temperature) have maximum and minimum values on this dates.')

st.write('---')
st.subheader('6. Irradiation Mean Per Hour')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('Grouping the `IRRADIATION` column by each time of the day :')

irradiation_daily_mean = weather_df.groupby(['TIME'])['IRRADIATION'].mean().reset_index().sort_values(by = 'TIME')
st.write(irradiation_daily_mean)

st.write('Plotting the dataset : ')
st.write('![alt text](https://img.techpowerup.org/201004/13.png "Irradiation Mean Per Hour")')
st.write('* According to previous graphs we can easily predict that solar power plant recieves maximum sun irradiation **11 AM** and **1 PM** and the minimum irradiation at night ')
st.write('---')

st.subheader('Decomposing The Data into Each Date')
st.write('First we decompose the data by `TIME`(row) , `DATE`(column) and `IRRADIATION`(value) : ')

irradiation_mean_calendar = weather_df.pivot_table(values = 'IRRADIATION', index = 'TIME', columns = 'DATE')
st.write(irradiation_mean_calendar)
st.write('Plotting the dataset : ')

st.write('![alt text](https://img.techpowerup.org/201004/14.png "Irradiation Mean Per Hour by Each Date")')
st.write('* As this graph represents a bell shape curve like the original bar plot.In some cases we have datapoint shortage in a certain time and date.The reason of this have been discussed.')
st.write('---')

st.write('![alt text](https://img.techpowerup.org/201004/15.png "Irradiation Mean Per Hour")')
st.write('---')
st.write('![alt text](https://img.techpowerup.org/201004/16.png "Irradiation Mean Per Hour")')
st.write('* Like the privious graphs(module and ambient temperature) on `2020-05-21` and `2020-05-18` solar power plant recieves maximum and minimum sun irradiation mean in respect.')
st.write('* **TIP** : This graphs shows that there is a positive relationship(coorelation) between `AMBIENT_TEMPERATURE` , `MODULE_TEMPERATURE` and `IRRADIATION` which we will cover in the next section.')

st.write('---')
st.write('## Features Correlation and Relationship')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write(r"""In this section we are going to analyze the correlations between features and find out weather the relationships between features is strong or not.
In statistics we determine the relationships between two components(for example X and Y) by correlation and covariance :

### Covariance : COV(X , Y) = $$( \frac{\sum (X_{i} - \bar{X})(Y_{i} - \bar{Y})}{N}  )$$
### Correlation : CORR(X , Y) = $$( \frac {COV(X , Y)}{\sigma_{X} \sigma_{Y}}  )$$

""")

st.write("""
**Where** :

> 1. **Xi** : the values of the X-variable

> 2. **Yj** :  the values of the Y-variable

> 3. **X̄**  : the mean (average) of the X-variable

> 4. **Ȳ**  : the mean (average) of the Y-variable

> 5. **N**  : the number of data points

> 6. **σX** : the standard deviation of the X-variable

> 7. **σY** : the standard deviation of the Y-variable

""")

st.write('* Correlation determineS the relationship between two variables.If we have a correlation **close to 1**, we have a **linear relationship** between two variables and we have **less errors** between datapoints and **trendline(regresshion line)** and if we have a correlation which is **close to zero** the relationship between two variables is **weak** and they can not be modelled by a regression line.Covariance determines that the slope of regression line is positive or negetive.If the covariance is negative we have a **regression line with negative slope** and if the covariance is positive is shows that the **slope of trendine is positive.**')
st.write('---')
st.write('First of all we have to merge this to datasets and then we get this resulting dataset down below : ')

total_df = pd.merge(weather_df , df , left_on = 'DATE_TIME' , right_on = 'DATE_TIME')
total_df.drop(columns = {'DATE_x' , 'TIME_x'} , inplace = True)
total_df.rename(columns = {'DATE_y' : 'DATE' , 'TIME_y' : 'TIME'} , inplace = True)

st.write(total_df)

st.write('Lets take a look at heatmap, which represents the correlation between features :')
st.write('![alt text](https://img.techpowerup.org/201004/17.png "Heat Map")')

st.write('* As we can observe, feature with themselves have strong correlation which is equal to 1 which is obvious.On the other hand some feature like `Module_temperature` , `DC_POWER` , `AC_POWER` and `IRRADIATION` which their correlation is above **90 %** and we can model them by linear regression and predict future.')

st.write('---')
st.subheader('1. Ambient Temperature and Module Temperature Correlation')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('![alt text](https://img.techpowerup.org/201004/18.png "Ambient Temperature and Module Temperature Correlation")')
st.write('* As we can see, the correlation between two features is not compeletely linear.This is because the correlations between this two features is **below 90%** but we are still able to predict future by this trendline.For instance, if we have around **30 C** Ambient temperature on a day we will have about **35 C** module temperature.')

st.write('---')
st.subheader('2. DC Power and Module Temperature Correlation')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('![alt text](https://img.techpowerup.org/201004/19.png "DC Power and Module Temperature Correlation")')
st.write('* This graph shows that the DC power and module temperature correlation is way more linear than the previous one.This two feature can be easily pridicted.For example if we have **50 C** module temprature mean on a day, we will get about **200,000 kW** DC power in total on a day.')

st.write('---')
st.subheader('3. DC Power and Ambient Temperature Correlation')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('![alt text](https://img.techpowerup.org/201004/20.png "DC Power and Ambient Temperature Correlation")')

st.write('---')
st.subheader('4. DC Power and Irradiation Correlation')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('![alt text](https://img.techpowerup.org/201004/21.png "DC Power and Irradiation Correlation")')

st.write('---')
st.subheader('5. DC Power and AC Power Correlation')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('![alt text](https://img.techpowerup.org/201004/22.png "DC Power and AC Power Correlation")')
st.write('* As we can see, this two feature have correlation close to `1`.This is because this two features have `DC Power = 10 . AC Power` relationship.It shows a compeletely linear relationship with slope equals to `10`.(`Y = 10 . X`)')
st.write('* In engineering aspect this inverter loses **90 %** of its power when it converts DC power into AC power.')

st.write('---')
st.subheader('Predicting DC Power with Linear Regression')

html_button = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to Table of Contents</a>'
st.markdown(html_button, unsafe_allow_html = True)

st.write('First of all we have to group the dataset by `DATE` column.Because we want to predict the `DC Power` in the next 3 days.')
st.write('* In this model we are trying to build a model that predict the `DC_POWER` by `AMBIENT_TEMPERATURE` , `MODULE_TEMPERATURE`  , `IRRADIATION` and `AC_POWER`.')
total_reg_df = total_df[['DATE' , 'TIME' , 'AMBIENT_TEMPERATURE' , 'MODULE_TEMPERATURE' , 'IRRADIATION' , 'AC_POWER' ,  'DC_POWER']]
total_reg_df = total_reg_df.groupby(['DATE'])[['AMBIENT_TEMPERATURE' , 'MODULE_TEMPERATURE' , 'IRRADIATION' , 'AC_POWER' , 'DC_POWER']].mean().reset_index().sort_values(by = 'DATE')
total_reg_df['DATE'] = pd.to_datetime(total_reg_df['DATE'])
total_reg_df.set_index('DATE' , inplace =  True)

st.write(total_reg_df)
st.write('If we use Linear Regression methon we will get this graph : ')
st.write('![alt text](https://img.techpowerup.org/201005/23.png "DC Power and AC Power Correlation")')
st.write('* As we can see we can not get the desired accuracy from this type of dataset, because we only have **31 instances(days)**.This number of instances is not enough to bulid a training model for linear regression.As a result we can not get a high accuracy for this model.')

#html_string = '<a href="#top" class="btn btn-primary btn-sm" role="button" aria-pressed="true" style="color:white" data-toggle="popover" title="go to Colors">Go to TOC</a>'

#st.markdown(html_string, unsafe_allow_html=True)
