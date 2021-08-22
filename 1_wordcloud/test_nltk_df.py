import pandas as pd
import nltk
from nltk.tokenize import  word_tokenize

df = pd.DataFrame({'Phrases': ['The greatest glory in living lies not in never falling, but in rising every time we fall.', 
                              'The way to get started is to quit talking and begin doing.', 
                              'If life were predictable it would cease to be life, and be without flavor.',
                              "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."]})
df['tokenized'] = df.apply(lambda row: nltk.word_tokenize(row['Phrases']), axis=1)
print(df.head())