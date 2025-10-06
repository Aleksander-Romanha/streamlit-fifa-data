import pandas as pd
import requests
import os

df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)

for col_id, col_img in [("ID", "Photo"), ("Nationality", "Flag"), ("Club", "Club Logo")]:
    os.makedirs(f"imgs/{col_img}", exist_ok=True)

    for id in df_data[col_id].unique():
        id_safe = id
        if type(id) is str:
            if '/' in id:
                id_safe = "id".replace("/", "_")

        photo_path = f"imgs/{col_img}/{id_safe}.png"
        if not os.path.exists(photo_path):
            photo_url = df_data.loc[df_data[col_id] == id, col_img].iat[0]
            img_data = requests.get(photo_url).content
            with open(photo_path, "wb") as f:
                f.write(img_data)

        df_data.loc[df_data[col_id] == id, col_img + ' png'] = photo_path

df_data.to_csv("datasets/CLEAN_FIFA23_official_data_mod.csv")