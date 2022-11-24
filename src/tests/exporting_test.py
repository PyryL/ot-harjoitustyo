import unittest
from bs4 import BeautifulSoup
from datetime import datetime
from entities.competitor import Competitor
from entities.competition import Competition
from services.exporting import Exporting

class ExportTestHelper:
  @classmethod
  def generate_competition(cls):
    start_time = datetime(2022, 11, 24, 12, 5, 17, 937554)
    john_finish_time = datetime(2022, 11, 24, 12, 27, 13, 614432)
    unelma_finish_time = datetime(2022, 11, 24, 12, 31, 11, 542380)

    john = Competitor("John Doe", 57, "Compile & Run club", john_finish_time)
    unelma = Competitor("Unelma Sirpa Leena", 1241, "", unelma_finish_time)
    matti = Competitor("Matti Meikäläinen", 98, "Hello world runners", None)

    return Competition("Helsinki marathon", [unelma, john, matti], start_time)

class TestExportingResultsList(unittest.TestCase):
  def setUp(self):
    competition = ExportTestHelper.generate_competition()
    exported_html_string = Exporting(competition).results_list_html()
    self.exported_document = BeautifulSoup(exported_html_string, 'html.parser')
  
  def test_header(self):
    header_text = self.exported_document.find("h1").text
    self.assertEqual(header_text, "Helsinki marathon")
  
  def test_table_row_count(self):
    rows = self.exported_document.find_all("tr")
    self.assertEqual(len(rows), 4)
  
  def test_competitor_result(self):
    result = self.exported_document.select_one("tbody tr:nth-child(1) td:nth-child(5)").text
    self.assertEqual(result, "00:21:55.7")
  
  def test_competitor_difference_to_winner(self):
    result = self.exported_document.select_one("tbody tr:nth-child(2) td:nth-child(6)").text
    self.assertEqual(result, "+00:03:57.9")
  
  def test_competitor_nonexistent_result(self):
    result = self.exported_document.select_one("tbody tr:nth-child(3) td:nth-child(5)").text
    self.assertEqual(result, "")

class TestExportingStartList(unittest.TestCase):
  def setUp(self):
    competition = ExportTestHelper.generate_competition()
    exported_html_string = Exporting(competition).start_list_html()
    self.exported_document = BeautifulSoup(exported_html_string, 'html.parser')
  
  def test_competition_name(self):
    header_text = self.exported_document.find("h1").text
    self.assertEqual(header_text, "Helsinki marathon")
  
  def test_table_row_count(self):
    rows = self.exported_document.find_all("tr")
    self.assertEqual(len(rows), 4)
  
  def test_bibs_in_ascending_order(self):
    bibs = [
      row.select_one("td:first-of-type").text
      for row in self.exported_document.select("tbody tr")
    ]
    for i in range(1, len(bibs)):
      self.assertGreater(int(bibs[i]), int(bibs[i-1]))
