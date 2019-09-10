import pandas as pd 
from matplotlib import pyplot as plt 

plt.style.use("fivethirtyeight")

data = pd.read_csv("data.csv")

ids = data["Responder_id"]
ages = data["Age"]

bins = []

for i in range(10,101,10):
	bins.append(i)


## for some ranges data is much much less that we can't show it on histogram with smaller range like above bins bcoz some ranges may have too large data
## so we set here log = True to measure it on logarithmic scale (i.e. on powers of 10 scale )
## so now it will be visible for ranges with less data
plt.hist(ages , bins=bins , edgecolor='black' , log=True)


## To draw verticle line on graph by which we can split graph into 2 parts.

median_age = 29
plt.axvline(median_age , color="#fc4f30" , label="Age Median" , linewidth=2)	


plt.legend()

plt.title("Ages of Respondents")
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()