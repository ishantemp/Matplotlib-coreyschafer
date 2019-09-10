import pandas as pd 
from matplotlib import pyplot as plt 

plt.style.use("fivethirtyeight")

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

## bins means no. of bins
## below will create 5 bins of equal width in the range 18 to 55 
## suppose one of our age range is 18 to 26 then height of that bin will be 4 (bcoz it will contain 18,19,21,25)
## and so on for other bins 
# plt.hist(ages , bins=5, edgecolor='black')



# passing list to bins for customized range 

bins = [10,20,30,40,50,60] 
plt.hist(ages , bins=bins, edgecolor='black')


# data = pd.read_csv("data.csv")

# ids = data["Responder_id"]
# ages = data["Age"]


plt.title("Ages of Respondents")
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()