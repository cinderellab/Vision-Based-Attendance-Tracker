from clean_data import clean_class
import pandas as pd


for x in range(1, 5):
  globals()['data%s' % x] = pd.read_csv('test' + str(x) + '.csv', e