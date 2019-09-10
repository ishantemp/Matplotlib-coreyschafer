from matplotlib import pyplot as plt 

## prints style available for plot 
# print(plt.style.available)

## list of default styles available printed from above list
# ['seaborn-talk', '_classic_test', 'seaborn-poster', 'seaborn-dark-palette', 'seaborn-darkgrid', 'fast', 'seaborn', 'ggplot',
#  'seaborn-paper', 'seaborn-whitegrid', 'seaborn-colorblind', 'fivethirtyeight', 'classic', 'seaborn-ticks', 'seaborn-pastel', 
#  'bmh', 'Solarize_Light2', 'seaborn-deep', 'tableau-colorblind10', 'seaborn-bright', 'dark_background', 'seaborn-muted',
#  'seaborn-dark', 'seaborn-notebook', 'grayscale', 'seaborn-white']


plt.style.use("fivethirtyeight")

## hand-drawn like style for plot
# plt.xkcd()


## dev_x and dev_y are grabbed from snippets.py(ishan/codes/corey-schafer/clonned-code_snippets/Python/Matplotlib/01-Introduction)

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]



# Median Python Developer Salaries by Age

## removes py_dev_x bcoz it is the same age range as above so we will use above
# py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

## we plotted multiple plot here first plt.plot(ages_x,dev_y) and now this 
## Both lines of plots will be in same plot
# b :- blue default line 
plt.plot(ages_x,py_dev_y,color='red',label="Python")



# Median JavaScript Developer Salaries by Age

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]


## alpha(opacity) is used to avoid overlapping of two lines 
## i.e it will make line transparent so we can see the line which is staying below this line 
## alpha is generally applied to above line bcoz it cuts the line below it. 
plt.plot(ages_x,js_dev_y,label="JavaScript")


## For all devlopers

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


##for plotting graph
# k-- :- Black dashed line
plt.plot(ages_x,dev_y,color='#444444',linestyle='--',label="All Devs")




## label for X axis
plt.xlabel('Ages')
## label 
plt.ylabel('Median Salary (INR)')
plt.title('Median Salary (INR) by Age')


## legend is used to identify which line in plot is for which data
## list is passed to this as label to this lines in order of they were plotted
## here first we plotted with all developers and then plotted specific for python so following is according to that order 
# plt.legend(['All Devs','Python'])



## we have passed label argument to plots so we don't need to pass list here and that is much better way.
plt.legend()

## to bring grid instead of plain background to find exact points sometimes
plt.grid(True)


plt.tight_layout()

# plt.savefig('new_demo.png')

## for showing the plotted graph
plt.show()