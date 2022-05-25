# helper method for extracting data of the player
from stats_utils.extract_stats import extract_stats


def extract_info(tr):
    base = "https://sofifa.com/"
    link = base + tr.select('td.col-name')[0].find("a").get("href")
    return {
        "name": tr.select('td.col-name')[0].find("a").get("aria-label"),
        "country": tr.select('td.col-name')[0].find("img").get("title"),
        "age": tr.select('td.col.col-ae')[0].text.strip(),
        "overall": tr.select('td.col.col-oa')[0].text.strip(),
        "potential": tr.select('td.col.col-pt')[0].text.strip(),
        "club": tr.select("td.col-name")[1].find("a").text,
        "best_position": tr.select('td.col-name')[0].find("span").text,
        "value": tr.select('td.col.col-vl')[0].text.strip(),
        "wage": tr.select('td.col.col-wg')[0].text.strip(),
        "stats": extract_stats(link)
    }











