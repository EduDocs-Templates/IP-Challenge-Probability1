import unittest
from os import path
import numpy as np
import pandas as pd

class Test1Challenge(unittest.TestCase):

	def test_file(self):
		self.assertTrue(path.isfile('challenge.csv'))

	def test_columns(self):
		submission_df = pd.read_csv('challenge.csv', index_col=0)
		self.assertIn('seq_length', submission_df.columns, 'Missing column seq_length')
		self.assertTrue('sample_mean' in submission_df.columns, 'Missing column sample_mean')
		self.assertTrue('sample_variance' in submission_df.columns, 'Missing column sample_variance')

	def test_values(self):
		submission_df = pd.read_csv('challenge.csv', index_col=0)
		sample_means = submission_df['sample_mean'].to_numpy()
		sample_variances = submission_df['sample_variance'].to_numpy()
		self.assertGreater(np.amin(np.absolute(sample_means)), 0, 'Mean values should be updated')
		self.assertGreater(np.amin(np.absolute(sample_variances)), 0, 'Variance  values should be updated')

if __name__ == '__main__':
	unittest.main()
