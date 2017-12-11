
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from scipy import stats
import json
from pandas.io.json import json_normalize
import datetime
import ast


# In[19]:

from odo import odo
import pandas as pd

df = odo('mongodb://system:system@ds127936.mlab.com:27936/heroku_njlc7ffz::tedtalks', pd.DataFrame)
df


# In[3]:

import ast
df['tags'] = df['tags'].apply(lambda x: ast.literal_eval(x))
df['tags']


# In[4]:

s = df.apply(lambda x: pd.Series(x['tags']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'theme'


# In[5]:


theme_df = df.drop('tags', axis=1).join(s)
theme_df.head()


# In[6]:

pop_themes = pd.DataFrame(theme_df['theme'].value_counts()).reset_index()
pop_themes.columns = ['theme', 'talks']
pop_themes.head(10)


# In[7]:

pop_list=pop_themes['theme'].head(4).tolist()
pop_list


# In[8]:

# pop_theme_talks = theme_df.loc[(theme_df['theme'].isin(pop_themes.head(10)['theme'])) & (theme_df['theme'] != 'TEDx')]
top_tags_df=theme_df.loc[theme_df['theme'].isin(pop_list)]
top_tags_df


# In[9]:

top_technology_df=theme_df.loc[theme_df['theme']=="technology"].sort_values('views', ascending=False)[:10]
top_10_technology=top_technology_df[['main_speaker','speaker_occupation','url','image_url']].reset_index(drop=True)
top_10_technology.to_json(orient='records')


# In[10]:

top_science_df=theme_df.loc[theme_df['theme']=="science"].sort_values('views', ascending=False)[:10]
top_10_science=top_science_df[['main_speaker','speaker_occupation','url','image_url']].reset_index(drop=True)
top_10_science.to_json(orient='records')


# In[11]:

top_global_df=theme_df.loc[theme_df['theme']=="global issues"].sort_values('views', ascending=False)[:10]
top_10_global=top_global_df[['main_speaker','speaker_occupation','url','image_url']].reset_index(drop=True)
top_10_global.to_json(orient='records')


# In[12]:

top_culture_df=theme_df.loc[theme_df['theme']=="culture"].sort_values('views', ascending=False)[:10]
top_10_culture=top_culture_df[['main_speaker','speaker_occupation','url','image_url']].reset_index(drop=True)
top_10_culture.to_json(orient='records')


# In[13]:

sub_technology_data = {"main_speaker": "Technology",
        "speaker_occupation": "Technology Speakers",
        "link": "https://www.ted.com/topics/technology",
        "children": top_10_technology.to_json(orient='records')}
sub_technology_data


# In[14]:

sub_global_data = {"main_speaker": "Global Issues",
        "speaker_occupation": "Global Issues Speakers",
        "link": "https://www.ted.com/topics/global+issues",
        "children": top_10_global.to_json(orient='records')}
sub_global_data


# In[15]:

sub_science_data = {"main_speaker": "Science",
        "speaker_occupation": "Science Speakers",
        "link": "https://www.ted.com/topics/science",
        "children": top_10_science.to_json(orient='records')}
sub_science_data


# In[16]:

sub_culture_data = {"main_speaker": "Culture",
        "speaker_occupation": "Culture Speakers",
        "link": "https://www.ted.com/topics/culture",
        "children": top_10_culture.to_json(orient='records')}
sub_culture_data


# In[17]:

data=({"main_speaker": "TedTalk",
      "speaker_occupation": "A trendy talk", 
      "link": "https://www.ted.com/",
      "img": "https://cdn0.iconfinder.com/data/icons/circle-icons/512/ted.png",    
      "children": (sub_technology_data, sub_science_data, sub_global_data, sub_culture_data)})
data


# In[18]:

with open('speakers.json', 'w') as outfile:
     json.dump(data, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)


# In[ ]:




# In[ ]:



