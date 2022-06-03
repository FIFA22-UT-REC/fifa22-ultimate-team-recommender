# Helper method to call other helpers that extracts detailed traits of the player
# from fifa_pack.extract_att import extract_att
# from fifa_pack.extract_def import extract_def
# from fifa_pack.extract_skill import extract_skill
# from fifa_pack.extract_pow import extract_pow
# from fifa_pack.extract_move import extract_move
# from fifa_pack.extract_mentality import extract_mentality
# from fifa_pack.extract_goalkeep import extract_goalkeep


def extract_deep(stats_block):
    return {"Att": extract_att(stats_block[0].find("ul")),
            "Skill": extract_skill(stats_block[1].find("ul")),
            "Move": extract_move(stats_block[2].find("ul")),
            "Power": extract_pow(stats_block[3].find("ul")),
            "Mentality": extract_mentality(stats_block[4].find("ul")),
            "Defending": extract_def(stats_block[5].find("ul")),
            "Goalkeep": extract_goalkeep(stats_block[6].find("ul"))}
