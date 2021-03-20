# Aula de Métodos Estatísticos com Python
# Teórico-Prática 1, com João Mendes Moreira, dia 02-03-2021 @13:30 -> @15:30 
# Modules
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os
# Styles
plt.style.use('seaborn-whitegrid')
plt.rc('text', usetex=True)
plt.rc('font', family='times')
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('font', size=12)
# Data Mining
def example1 ():
    
    # Manipulating data with python's dictionary
    
    data =  {
        
            'year': [2010, 2011, 2012, 2010, 2011, 2012, 2010, 2011, 2012],
            'team': ['FCBarcelona', 'FCBarcelona', 'FCBarcelona', 'RMadrid', 'RMadrid', 'RMadrid', 'ValenciaCF', 'ValenciaCF', 'ValenciaCF'],
            'wins':   [30, 28, 32, 29, 32, 26, 21, 17, 19],
            'draws':  [6, 7, 4, 5, 4, 7, 8, 10, 8],
            'losses': [2, 3, 2, 4, 2, 5, 9, 11, 11]
            
            }
    
    football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'draws', 'losses'])
    return football
def example2 ():
    
    # Manipulating data with cvs' database
    
    pwd = os.getcwd()
    edu = pd.read_csv(pwd + '/educ_figdp_1_Data.csv', na_values=':', usecols=['TIME', 'GEO', 'Value'])
    
    def read_data(edu):
    
        print (edu)
        print (edu.head())
        print (edu.tail())
        print (edu.columns)
        print (edu.index)
        print (edu.values)
        print (edu.describe())
        
        return None
    
    
    def select_data(edu):
        
        print (edu['Value'])
        print (edu[10:14])
        print (edu.ix[90:94, ['TIME', 'GEO']])
        
        return None
    
    
    def filtering_data(edu):
        
        return edu[edu['Value'] > 6.5].tail()
    
    
    def filtering_miss_value(edu):
        
        return edu[edu['Value'].isnull()].head()
    
    
    def manipulating_data(edu):
        
        print (edu.max(axis=0))
        print ('Pandas max function:', edu['Value'].max())
        
        s = edu['Value'] / 100
        s = edu['Value'].apply(lambda d: d**2)
        print (s.head())
        
        edu['ValueNorm'] = edu['Value'] / edu['Value'].max()
        print (edu.tail())
        
        edu.drop('ValueNorm', axis=1, inplace=True)
        print (edu.head())
        
        edu = edu.append({'TIME': 2000, 'Value': 5.00, 'GEO': 'a'}, ignore_index=True)
        print (edu.tail())
        
        
        edu.drop(max(edu.index), axis=0, inplace=True)
        print (edu.tail())
        
        eduDrop = edu.drop(edu['Value'].isnull(), axis=0)
        print (edu.head())
        
        eduDrop = edu.dropna(how='any', subset=['Value'], axis=0)
        print (edu.head())
        
        eduFilled = edu.fillna(value={'Value': 0})
        print (edu.head())
        
        return None
    
    
    def data_sorting(edu):
        
        edu.sort_values(by='Value', ascending=False, inplace=True)
        print (edu.head())
        
        edu.sort_index(axis=0, ascending=True, inplace=True)
        print (edu.head())
        return None
    
    
    def grouping_data(edu):
        
        group = edu[['GEO', 'Value']].groupby('GEO').mean()
        
        return group.head()
    
    
    def rearranging_data(edu):
        
        filtered_data = edu[edu['TIME'] > 2005]
        pivedu = pd.pivot_table(filtered_data, values='Value', index=['GEO'], columns=['TIME'])
        print (pivedu.head())
        
        return pivedu.ix[['Spain', 'Portugal'], [2006, 2011]]
    
    
    def ranking_data(edu):
        
        pivedu = pivedu.drop(['Euro area (13 countries)',
                              'Euro area (15 countries)',
                              'Euro area (17 countries)',
                              'Euro area (18 countries)',
                              'European Union (25 countries)',
                              'European Union (27 countries)',
                              'European Union (28 countries)'
                              ], axis=0)
        
        pivedu = pivedu.rename(index={'Germany (until 1990 former territory of the FRG)': 'Germany'})
        pivedu = pivedu.dropna()
        pivedu.rank(ascending=False, method='first').head()
        
        totalSum = pivedu.sum(axis=1)
        totalSum.rank(ascending=False, method='dense').sort_values().head()
        return totalSum
    
    
    def plotting_data(edu):
        
        fig = plt.figure(figsize=(12, 5))
        totalSum = pivedu.sum(axis=1).sort_values(ascending=False)
        totalSum.plot(kind='bar', style='b', alpha=0.4, title='Total Values for Country')
        plt.savefig('Totalvalue_Country.png', dpi=300, bbox_inches='tight')
        
        my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
        ax = pivedu.plot(kind='barh', stacked=True, color=my_colors, figsize=(12, 6))
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('Value_Time_Country.png', dpi=300, bbox_inches='tight')
        
        return None
    
    return some_function