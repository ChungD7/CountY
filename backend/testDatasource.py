import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
      cls.dataSet = DataSource()
      cls.dataSet.__init__()

    # Base case
  def test_general_start_end(self):
      self.assertEquals(self.dataSet.getCountiesInShareRange('rep', '70', '100', 'Minnesota'),
                           [('MORRISON', 'Minnesota'), ('TODD', 'Minnesota')])

  def test_start_equals_end(self):
      self.assertEquals(self.dataSet.getCountiesInShareRange('dem', '71.76', '71.76', 'California'),
                        [('LOS ANGELES', 'California')])

  def test_negative_start(self):
      self.assertEquals(self.dataSet.getCountiesInShareRange('other', '-3', '3', 'Minnesota'),
                        [('CLEARWATER', 'Minnesota')])

  def test_above_maximum_end(self):
      self.assertEquals(self.dataSet.getCountiesInShareRange('rep', '80', '120', 'Illinois'),
                        [('EDWARDS', 'Illinois'), ('WAYNE', 'Illinois')])

  def test_no_counties_in_range(self):
    self.assertEquals(self.dataSet.getCountiesInShareRange('third', '15', '100'), 'No counties found in specified range.')

  def test_county_overflow(self):
    self.assertEquals(self.dataSet.getCountiesInShareRange('dem', '0', '100', 'Texas'),
                      'Found 254 results. Please narrow your range.')

  def test_no_specified_state(self):
      self.assertEquals(self.dataSet.getCountiesInShareRange('rep', '1', '2'), [('Ward 7', 'District of Columbia'), ('Ward 8', 'District of Columbia')])

if __name__ == '__main__':
    unittest.main()