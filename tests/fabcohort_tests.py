import unittest
from fab_cohort import Cohort
import pandas as pd
from pandas.testing import assert_frame_equal
import numpy as np


class FabcohortTestCase(unittest.TestCase):

    def setUp(self):
        self.cohort = Cohort()

    def test_one(self):
        """Test count_cohort_segments"""
        # sample input
        data = {
            'user_id': ['6001ef966c', '600wef966c', '600wef966c', '600we4566c', '600we4566c', '623we4566c', '623we4566c', '623we4536c', '678we4536c', '678we4236c', '678we4236c', '678we4236c'],
            'date': ['2023-03-01', '2023-03-01', '2023-04-01', '2023-03-01', '2023-05-01', '2023-04-01', '2023-05-01', '2023-04-01', '2023-05-01', '2023-03-01', '2023-04-01', '2023-05-01']
            }
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        df['segment'] = 'default'
        df['count'] = 1
        # function output
        result = self.cohort.count_cohort_segments(df, 'MS')
        print(result)

        # asserted output
        data = {
            'created': ['2023-03-01', '2023-03-01', '2023-03-01', '2023-04-01', '2023-04-01', '2023-04-01','2023-05-01', '2023-05-01', '2023-05-01'],
            'cohort': ['t0', 't1', 't2', 't0', 't1', 't2', 't0', 't1', 't2'],
            'segment': ['default', 'default', 'default', 'default', 'default', 'default', 'default', 'default', 'default'],
            'count': [4.0, 2.0, 2.0, 2.0, 1.0, np.nan, 1.0, np.nan, np.nan]
            }
        asserted_df = pd.DataFrame(data)
        asserted_df['created'] = pd.to_datetime(asserted_df['created'])
        print(asserted_df)

        # assert
        assert_frame_equal(result, asserted_df)

if __name__ == '__main__':
    unittest.main()
