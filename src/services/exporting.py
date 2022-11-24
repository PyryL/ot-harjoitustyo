
class Exporting:
  def __init__(self, competition):
    self._competition = competition

  def start_list_html(self):
    with open("src/assets/start_list_template.html") as f:
      template = f.read()
    template = template.replace("{competition_name}", self._competition.name)
    template = template.replace("{competitor_rows}", self._start_list_competitor_rows())
    return template
  
  def _start_list_competitor_rows(self):
    rows = []
    for competitor in self._competition.competitors:
      rows.append(f"""
        <tr>
          <td>{competitor.bib}</td>
          <td>{competitor.name}</td>
          <td>{competitor.club}</td>
        </tr>
      """)
    return "\n".join(rows)
  
  def results_list_html(self):
    with open("src/assets/result_list_template.html") as f:
      template = f.read()
    template = template.replace("{competition_name}", self._competition.name)
    template = template.replace("{competitor_rows}", self._results_list_competitor_rows())
    return template
  
  def _results_list_competitor_rows(self):
    rows = []
    for i, competitor in enumerate(self._competition.competitors):
      result = self._competition.result_of_competitor(competitor)
      resultFormat = "--:--:--" if result is None else str(result)
      rows.append(f"""
        <tr>
          <td>{i+1}</td>
          <td>{competitor.bib}</td>
          <td>{competitor.name}</td>
          <td>{competitor.club}</td>
          <td>{resultFormat}</td>
          <td>+XX.X</td>
        </tr>
      """)
    return "\n".join(rows)
