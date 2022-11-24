import unittest
from bs4 import BeautifulSoup
from datetime import datetime
from entities.competitor import Competitor
from entities.competition import Competition
from services.exporting import Exporting

class TestExporting(unittest.TestCase):
  def setUp(self):
    finish_time = datetime(2022, 11, 24, 12, 27, 13, 614432)
    john_doe = Competitor("John Doe", 57, "Compile & Run club", finish_time)
    start_time = datetime(2022, 11, 24, 12, 5, 17, 937554)
    competition = Competition("Helsinki marathon", [john_doe], start_time)
    exported_html_string = Exporting(competition).export_as_html()
    self.exported_document = BeautifulSoup(exported_html_string, 'html.parser')
  
  def test_header(self):
    header_text = self.exported_document.find("h1").text
    self.assertEqual(header_text, "Helsinki marathon")
  
  def test_table_row_count(self):
    rows = self.exported_document.find_all("tr")
    self.assertEqual(len(rows), 2)
  
  def test_competitor_result(self):
    result = self.exported_document.find_all("td")[-1].text
    self.assertEqual(result, "0:21:56.7")
