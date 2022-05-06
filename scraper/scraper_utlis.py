# helper method for extracting data of the player

def extract_info(tr):
    td = tr.findAll("td")
    return{
        "name": tr.select('td.col-name')[0].find("a").get("aria-label"),
        "country": tr.select('td.col-name')[0].find("img").get("title"),
        "age": tr.select('td.col.col-ae')[0].text.strip(),
        "overall": tr.select('td.col.col-oa')[0].text.strip(),
        "potential": tr.select('td.col.col-pt')[0].text.strip(),
        "club": tr.select("td.col-name")[1].find("a").text,
        #"height": tr.select('td.col.col-hi')[0].text.strip(),
        #"weight": tr.select('td.col.col-wi')[0].text.strip(),
        #"foot": tr.select('td.col.col-pf')[0].text.strip(),
        "best_position": tr.select('td.col-name')[0].find("span").text,
        "value": tr.select('td.col.col-vl')[0].text.strip(),
        "wage": tr.select('td.col.col-wg')[0].text.strip(),
        #"PAC": tr.select('td.col.col-pac')[0].text.strip(),
        #"SHO": tr.select('td.col.col-sho')[0].text.strip(),
        #"PAS": tr.select('td.col.col-pas')[0].text.strip(),
        #"DRI": tr.select('td.col.col-dir')[0].text.strip(),
        #"DEF": tr.select('td.col.col-def')[0].text.strip(),
        #"PHY": tr.select('td.col.col-phy')[0].text.strip()
    }

