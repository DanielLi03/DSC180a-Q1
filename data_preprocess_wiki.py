import pandas as pd
import transformers as t

# read the train.csv.zip from Toxic Comment Classification Challenge on Kaggle
df = pd.read_csv('data/train.csv.zip', compression='zip')

# get useful columns
df = df[['comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']]

# relevant row extraction to balance and get the data
first_100 = df.head(150)
severe_toxic = df[df['severe_toxic'] == 1].head(50)
obscene = df[df['obscene'] == 1].head(50)
threat = df[df['threat'] == 1].head(50)
insult = df[df['insult'] == 1].head(50)
identity_hate = df[df['identity_hate'] == 1].head(50)
combined_df = pd.concat([first_100, severe_toxic, obscene, threat, insult, identity_hate]).drop_duplicates()

# rename columns for convenience later
combined_df = combined_df.rename(columns={'toxic': 'toxicity', 'severe_toxic': 'severe_toxicity', 'obscene': 'obscene', 'threat': 'threat', 'insult': 'insult', 'identity_hate': 'identity_attack'})

# export data into csv file
combined_df.to_csv('data/cleaned_data_wiki.csv', index=False)