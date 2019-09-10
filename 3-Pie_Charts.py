import matplotlib.pyplot as plt 

plt.style.use("fivethirtyeight")


slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java',]

explodes = [0,0,0,0.1,0]

# colors = ['blue','red','yellow','green']

# plt.pie(slices,labels=labels,colors=colors,wedgeprops={'edgecolor':'black'})


plt.pie(slices,labels=labels,explode=explodes,
	autopct = '%1.1f%%',
	wedgeprops={'edgecolor':'black'})

plt.title("Most Popular Languages")

plt.tight_layout()

plt.show()