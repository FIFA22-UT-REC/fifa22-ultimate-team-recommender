# helper method for extracting data of the player
from scraper.stats_utils.extract_stats import extract_stats


def extract_info(tr, *args):
    # base = "https://sofifa.com/"
    name = tr.select('td.col-name')
    # attr = "?attr=classic"
    # link = base + name[0].find("a").get("href") + attr
    return {
        "name": name[0].find("a").get("aria-label"),
        "country": name[0].find("img").get("title"),
        "age": tr.select('td.col.col-ae')[0].text.strip(),
        "overall": tr.select('td.col.col-oa')[0].text.strip(),
        "potential": tr.select('td.col.col-pt')[0].text.strip(),
        "club": name[1].find("a").text,
        "best_position": name[0].find("span").text,
        "value": tr.select('td.col.col-vl')[0].text.strip(),
        "wage": tr.select('td.col.col-wg')[0].text.strip(),
        "stats": extract_stats(*args)
    }












