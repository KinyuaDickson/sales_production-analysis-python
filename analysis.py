# sales_production-analysis-python
comparing sales with  production and ploting the graph using pandas matplotlib and python
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> from matplotlib import style
>>> style.use("fivethirtyeight")
>>> df=pd.DataFrame({"sale":[1000,900,600,300,500,700],"production":[700,600,450,800,500,650],"year":[2014,2015,2016,2017,2018,2019]})
>>> df.set_index("year", inplace=True)
>>> df.plot()
<matplotlib.axes._subplots.AxesSubplot object at 0x075B6DB0>
>>> plt.show()


