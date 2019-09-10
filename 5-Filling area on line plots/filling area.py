import pandas as pd 
from matplotlib import pyplot as plt 

data = pd.read_csv("data.csv")

## Age , All_Devs , Python and JavaScript are columns in data.csv

ages = data["Age"]

dev_salaries = data["All_Devs"]

py_salaries = data["Python"]

js_salaries = data["JavaScript"]

plt.plot(ages , dev_salaries , color = "#444444" , linestyle = "--" , label = "All Devs")

plt.plot(ages , py_salaries , label = "Python")


overall_median = 57287

## using fill_between b/w python and a fixed value overall_median
# plt.fill_between(ages , py_salaries , overall_median , alpha = 0.25)

# ## using fill_between b/w python and a fixed value overall_median with different colors for above and below part 

# plt.fill_between(ages,py_salaries,overall_median,
# 				 where=(py_salaries > overall_median),
# 				  interpolate=True , alpha =0.6)

# plt.fill_between(ages,py_salaries,overall_median,
# 				 where=(py_salaries <= overall_median),
# 				  interpolate=True , color = 'red' ,alpha =0.6)



## using fill_between b/w python and other plotted line dev_salaries
# plt.fill_between(ages , py_salaries , dev_salaries , alpha = 0.25)



## using fill_between b/w python and dev_salaries with different colors for above and below part 

plt.fill_between(ages,py_salaries,dev_salaries,
				 where=(py_salaries > dev_salaries),
				  interpolate=True , alpha =0.6)

plt.fill_between(ages,py_salaries,dev_salaries,
				 where=(py_salaries <= dev_salaries),
				  interpolate=True , color = 'red' ,alpha =0.6)




plt.legend()

plt.title("Medain Salary (INR) by Age")

plt.xlabel("Ages")

plt.ylabel("Median Salary (INR)")

plt.tight_layout()

plt.show()