
# coding: utf-8

# In[ ]:


import csv
with open("guns.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)


# In[ ]:


print(data[:5])


# In[ ]:


headers = data[:1]
data = data[1:]
print(headers)
print(data[:5])


# In[ ]:


years = [row[1] for row in data]

year_counts = {}
for year in years:
    if year not in year_counts:
        year_counts[year] = 0
    year_counts[year] += 1

year_counts


# In[ ]:


import datetime

dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
dates[:5]


# In[ ]:


date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 0
    date_counts[date] += 1

date_counts


# In[ ]:


sexes = [row[5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex] += 1
sex_counts


# In[ ]:


races = [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
race_counts


# Gun deaths in the US seem to disproportionately affect men vs women. They also seem to disproportionately affect minorities, although having some data on the percentage of each race in the overall US population would help.
# There appears to be a minor seasonal correlation, with gun deaths peaking in the summer and declining in the winter. It might be useful to filter by intent, to see if different categories of intent have different correlations with season, race, or gender.

# In[ ]:


import csv

with open("census.csv", "r") as f:
    reader = csv.reader(f)
    census = list(reader)
    
census


# In[ ]:


mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# In[ ]:


intents = [row[3] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1

race_per_hundredk = {}
for k,v in homicide_race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

race_per_hundredk


# It appears that gun related homicides in the US disproportionately affect people in the Black and Hispanic racial categories.
# Some areas to investigate further:
# - The link between month and homicide rate.
# - Homicide rate by gender.
# - The rates of other intents by gender and race.
# - Gun death rates by location and education.
