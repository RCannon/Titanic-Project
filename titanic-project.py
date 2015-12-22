import pandas as pd
from pandas import Series, DataFrame

titanic = pd.read_csv('train.csv')

titanic.head()

titanic.info()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sns.factorplot(x='Sex', data=titanic, kind = 'count')

sns.factorplot(x= 'Pclass', data = titanic, hue = 'Sex', kind = 'count')

def male_female_child(passenger):
    age, sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex
        
titanic['person'] = titanic[['Age', 'Sex']].apply(male_female_child, axis = 1)

titanic[0:10]

sns.factorplot('Pclass', data = titanic, hue = 'person', kind = 'count')

titanic['Age'].hist(bins = 70)

titanic['Age'].mean()

titanic['person'].value_counts()

fig = sns.FacetGrid(titanic_df, hue = 'Sex', aspect = 4)
fig.map(sns.kdeplot, 'Age', shade=True)

oldest = titanic['Age'].max()

fig.set(xlim=(0, oldest))

fig.add_legend()

titanic['person'].head()

deck = titanic['Cabin'].dropna()

deck.head()

levels = []

for level in deck:
    levels.append(level[0])
    
cabin = DataFrame(levels)
cabin.columns = ['Cabin']
sns.factorplot('Cabin', data = cabin, kind = 'count', palette = 'winter_d')

cabin = cabin[cabin.Cabin != 'T']
sns.factorplot('Cabin', data = cabin, kind = 'count', palette = 'summer')

titanic.head()

sns.factorplot('Embarked', data = titanic, hue = 'Pclass', kind = 'count', order=['C', 'Q', 'S'], 
               hue_order = [1,2,3])
               
titanic.head()

titanic['Alone'] = titanic.SibSp + titanic.Parc

titanic['Alone'].head()

titanic['Alone'].loc[titanic['Alone'] > 0 ] = 'With family'

titanic['Alone'].loc[titanic['Alone'] == 0 ] = 'Alone'

titanic.head()

sns.factorplot('Alone', 'Age', data = titanic, kind = 'bar', palette = 'Blues')

titanic['Survivor'] = titanic.Survived.map({0: 'no', 1: 'yes'})

sns.factorplot('Survivor', data = titanic, kind = 'count', palette = 'Set1

sns.factorplot('Pclass', 'Survived', hue = 'person', data = titanic, order = [1,2,3])

sns.lmplot('Age', 'Survived', data = titanic)

sns.lmplot('Age', 'Survived', hue = 'Pclass', data = titanic, palette = 'winter', hue_order = [1,2,3])

generations = [10, 20, 40, 60, 80]
sns.lmplot(x='Age', y='Survived', hue = 'Pclass',data = titanic, x_bins = generations, palette = 'winter')

sns.lmplot('Age', 'Survived', hue = 'Sex', data = titanic, palette = 'winter', x_bins = generations)
