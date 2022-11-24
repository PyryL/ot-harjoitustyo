from os import path

class Exporting:
  def __init__(self, competition):
    self._competition = competition
  
  def export_as_html(self):
    with open("src/assets/html_export_template.html") as f:
      template = f.read()
    template = template.replace("{competition_name}", self._competition.name)
    template = template.replace("{competitor_rows}", self._html_table_rows())
    return template
  
  def _html_table_rows(self):
    rows = []
    for competitor in self._competition.competitors:
      rows.append(f"""
        <tr>
          <td>{competitor.bib}</td>
          <td>{competitor.name}</td>
          <td>{competitor.club}</td>
          <td>--:--:--</td>
        </tr>
      """)
    return "\n".join(rows)
