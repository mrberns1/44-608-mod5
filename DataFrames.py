# coding: utf-8
import pandas as pd
grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob':[83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades
grades.index = ['Test1', 'Test2', 'Test3']
grades
grades['Eva']
grades.sam
grades.Sam
grades.loc['Test1']
grades.iloc[1]
grades.loc['Test1':'Test3']
grades.iloc[0:2]
grades.loc[['Test1', 'Test3']]
grades.iloc[[0, 2]]
grades.loc['Test1':'Test2', ['Eva', 'Katie']]
grades.iloc[[0, 2], 0:3]
grades[grades >= 90]
grades[(grades >= 80) & (grades < 90)]
grades.at['Test2', 'Eva']
grades.iat[2, 0]
grades.at['Test2', 'Eva'] = 100
grades.at['Test2', 'Eva']
grades.iat[1, 2] = 87
grades.iat[1, 2] 
grades.describe()
pd.set_option('percision', 2)
pd.set_option('precision', 2)
grades.describe()
pd.set_option('precision' , 2)
grades.mean()
grades.T
grades.T.describe()
grades.T.mean()
grades.sort_index(ascending = False)
pd.set_option("display.precision",2)
grades.describe()
grades.mean()
grades.T
grades.T.mean()
grades.sort_index(ascending = False)
grades.sort_index(axis=1)
grades.sort_value(by='Test1', axis=1, ascending=False)
grades.sort_values(by='Test1', axis=1, ascending=False)
grades.loc['Test1'].sort_values(ascending=False)
#missybernskoetter
