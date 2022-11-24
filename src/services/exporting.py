from datetime import timedelta
from services.timedelta_format import format_timedelta

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
    # sort competitors by their bib number
    competitors = sorted(self._competition.competitors, key=lambda competitor : competitor.bib)

    rows = []
    for competitor in competitors:
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
    # sort competitors by their result times
    competitors = [
      (competitor, self._competition.result_of_competitor(competitor))
      for competitor in self._competition.competitors
    ]
    competitors.sort(key=lambda pair : timedelta.max if pair[1] is None else pair[1])
    best_result = competitors[0][1]

    rows = []
    for i, (competitor, competitor_result) in enumerate(competitors):
      resultFormat = "" if competitor_result is None else format_timedelta(competitor_result)
      difference = "" if i == 0 or competitor_result is None or best_result is None else "+" + format_timedelta(competitor_result-best_result)

      rows.append(f"""
        <tr>
          <td>{i+1}</td>
          <td>{competitor.bib}</td>
          <td>{competitor.name}</td>
          <td>{competitor.club}</td>
          <td>{resultFormat}</td>
          <td>{difference}</td>
        </tr>
      """)

    return "\n".join(rows)
