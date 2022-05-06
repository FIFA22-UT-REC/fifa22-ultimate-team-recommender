# helper method for extracting data of the player

def extract_info(tr):
    td = tr.findAll("td")
    return{
        "name": td[1].find("a").get("aria-label"),
        "country": td[1].find("img").get("title"),
        "age": tr.select('td.col.col-ae')[0].text.strip(),
        "overall": tr.select('td.col.col-oa')[0].text.strip(),
        "potential": tr.select('td.col.col-pt')[0].text.strip(),
        "club": td[5].find("a").text,
        "height": tr.select('td.col.col-hi')[0].text.strip(),
        "weight": tr.select('td.col.col-wi')[0].text.strip(),
        "foot": tr.select('td.col.col-pf')[0].text.strip(),
        "best_position": tr.select('td.col.col-bp')[0].text.strip(),
        "value": tr.select('td.col.col-vl')[0].text.strip(),
        "wage": tr.select('td.col.col-wg')[0].text.strip(),
        "PAC": tr.select('td.col.col-pac')[0].text.strip(),
        "SHO": tr.select('td.col.col-sho')[0].text.strip(),
        "PAS": tr.select('td.col.col-pas')[0].text.strip(),
        "DRI": tr.select('td.col.col-dir')[0].text.strip(),
        "DEF": tr.select('td.col.col-def')[0].text.strip(),
        "PHY": tr.select('td.col.col-phy')[0].text.strip()
    }

