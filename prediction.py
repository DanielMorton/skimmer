import numpy as np
import pandas as pd
from model import get_model
from preprocess import read_image

animal_map = {"reptile": ["Amphibia", "Reptilia"],
              "bird": ["Aves"],
              "insect": ["Insecta"]}


def predict(args):
    img = read_image(args["name"])
    animal, level, model = get_model(args)
    categories = pd.read_csv("./models/category_levels.csv")
    categories = categories[categories["class"].isin(animal_map[animal])][level].unique()

    return animal, level, pd.Series(model.predict(img[np.newaxis, ...])[0],
                                    index=categories).sort_values(ascending=False)
