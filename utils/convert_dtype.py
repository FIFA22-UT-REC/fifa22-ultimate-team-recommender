# Helper for pipeline
def convert_dtype(df):
    all_feats = df.columns.to_list()
    category_feats = ["name", "country", "club", "best_position",
                      "work_rate", "preferred_foot"]
    numeric_feats = list(set(all_feats) - set(category_feats))
    df[numeric_feats] = df[numeric_feats].astype("int64")
    return df