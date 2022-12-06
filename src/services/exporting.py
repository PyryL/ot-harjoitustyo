from datetime import timedelta
from services.timedelta_format import format_timedelta
from entities.competitor import SpecialResult

class Exporting:
    def __init__(self, competition):
        self._competition = competition

    def start_list_html(self):
        with open("src/assets/start_list_template.html", encoding="utf-8") as file:
            template = file.read()
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
        with open("src/assets/result_list_template.html", encoding="utf-8") as file:
            template = file.read()
        template = template.replace("{competition_name}", self._competition.name)
        template = template.replace("{competitor_rows}", self._results_list_competitor_rows())
        return template

    def _results_list_competitor_rows(self):
        # sort competitors by their result times
        competitors = [
            (competitor, self._competition.result_of_competitor(competitor))
            for competitor in self._competition.competitors
        ]
        competitors.sort(key=self._competitor_result_sort_key)
        best_result = competitors[0][1]

        rows = []
        for i, (competitor, result) in enumerate(competitors):
            if result is None:
                result_format = ""
            elif isinstance(result, SpecialResult):
                result_format = result.value.upper()
            else:
                result_format = format_timedelta(result)

            difference = (
                ""
                if i == 0 or result is None or isinstance(result, SpecialResult)
                or best_result is None or isinstance(best_result, SpecialResult)
                else "+" + format_timedelta(result-best_result)
            )

            rows.append(f"""
            <tr>
                <td>{i+1}</td>
                <td>{competitor.bib}</td>
                <td>{competitor.name}</td>
                <td>{competitor.club}</td>
                <td>{result_format}</td>
                <td>{difference}</td>
            </tr>
            """)

        return "\n".join(rows)

    def _competitor_result_sort_key(self, competitor_result_tuple):
        # sort order datetime, None, DNF, DNS, DQ
        result = competitor_result_tuple[1]
        if result is None:
            return timedelta.max - timedelta(seconds=4)
        if result == SpecialResult.DID_NOT_FINISH:
            return timedelta.max - timedelta(seconds=3)
        if result == SpecialResult.DID_NOT_START:
            return timedelta.max - timedelta(seconds=2)
        if result == SpecialResult.DISQUALIFIED:
            return timedelta.max - timedelta(seconds=1)
        return result
