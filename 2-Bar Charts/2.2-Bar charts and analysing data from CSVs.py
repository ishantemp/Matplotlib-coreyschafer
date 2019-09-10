## we will now grab data from external CSVs and show that data to graph
import csv
from matplotlib import pyplot as plt 

import pandas as pd

from collections import Counter


plt.style.use("fivethirtyeight")

# ## for reading with DictReader method


# with open("data.csv") as csv_file:
# 	csv_reader = csv.DictReader(csv_file)

# language_counter = Counter()
	 
# for row in csv_reader:
# 	# languages in each row
# 	row_langs = row['LanguagesWorkedWith'].split(';')
# 	# updating counter so it will automatically manage counter for every key(key is our languages)
# 	language_counter.update(row_langs)




data = pd.read_csv('data.csv')

ids = data['Responder_id']  ## Responder_id is a column
lang_responses = data['LanguagesWorkedWith'] ## LanguagesWorkedWith is a column

language_counter = Counter()
	 
for response in lang_responses: ## lang_response contains string values of langs contained in each row separated by ';'
	# langs in each row
	row_langs = response.split(';')
	# updating counter so it will automatically manage counter for every key(key is our languages)
	language_counter.update(row_langs)


languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

# print(languages)
# print(popularity)	

# we want to plot a bar graph of most popular programming languages.
# we will use default Counter class to maintain counter for each programming languages grabbed from each list from each rows.

languages.reverse()
popularity.reverse()

plt.barh(languages , popularity)


plt.title('Most Popular Languages')

# plt.ylabel('Programming languages')

plt.xlabel('Popularity')




plt.tight_layout()

# ## for showing the plotted graph
plt.show()