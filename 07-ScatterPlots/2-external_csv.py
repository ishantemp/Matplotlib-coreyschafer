
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')


## data of top 200 trending videos of youtube is in 2019-05-31-data.csv 

data = pd.read_csv('2019-05-31-data.csv')

# list of views for particular video
view_count = data['view_count'] 
likes = data['likes']

# list of likes to dislikes ratio 
ratio = data['ratio']


plt.scatter(view_count,likes, c=ratio, cmap='summer',
			edgecolor='black',linewidth=1)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')





plt.tight_layout()

plt.show()
