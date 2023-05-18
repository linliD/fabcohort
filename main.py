import fab_cohort
import pandas as pd

# get the base table
data = {
    'user_id': ['6001ef966c', '600wef966c', '600wef966c', '600we4566c', '600we4566c', '623we4566c', '623we4566c', '623we4536c', '678we4536c', '678we4236c', '678we4236c', '678we4236c'],
    'date': ['2023-03-01', '2023-03-01', '2023-04-01', '2023-03-01', '2023-05-01', '2023-04-01', '2023-05-01', '2023-04-01', '2023-05-01', '2023-03-01', '2023-04-01', '2023-05-01']}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])
df['count'] = 1

# Instantiate a cohort object
cohort = fab_cohort.Cohort()
result = cohort.count_cohort(df)
