import numpy as np
import pandas as pd

import os

from datetime import datetime
from .model import get_model
from .preprocess import read_image
from . import PREDICTIONS
from . import ANIMAL_MAP, CATEGORY_FILE, ORDINALS


def pred_dict(animal, level):
    pd = {}
    for n in range(PREDICTIONS[animal][level]):
        pd["File"] = []
        pd[f"{ORDINALS[n]} Species"] = []
        pd[f"{ORDINALS[n]} Score"] = []

    return pd


def print_prediction_time(pred_time):
    time_string = ""
    hours = pred_time.seconds // 3600
    minutes = (pred_time.seconds % 3600) // 60
    seconds = pred_time.seconds % 60
    if hours > 1:
        time_string += f"{hours} hours,"
    elif hours == 1:
        time_string += "1 hour,"

    if minutes > 1:
        time_string += f"{minutes} minutes,"
    elif minutes == 1:
        time_string += f"1 minutes,"
    elif hours > 0:
        time_string += f"0 minutes,"

    if seconds > 1:
        time_string += f"{seconds} seconds."
    elif seconds == 1:
        time_string += f"1 second."
    elif hours > 0 or minutes > 0:
        time_string += f"0 seconds."

    print(pred_time)


def predict_directory(args):
    directory = args["directory"]
    images = [f for f in os.listdir(directory) if '.jpg' in f]
    animal, level, model = get_model(args)
    categories = pd.read_csv(CATEGORY_FILE)
    categories = categories[categories["class"].isin(ANIMAL_MAP[animal])][level].unique()
    num_preds = PREDICTIONS[animal][level]
    predictions = pred_dict(animal, level)
    start = datetime.now()
    for f in images:
        img = read_image(f"{directory}/{f}")
        pred = pd.Series(model.predict(img[np.newaxis, ...])[0],
                         index=categories).sort_values(ascending=False)[:num_preds]
        predictions["File"].append(f)
        for n in range(num_preds):
            predictions[f"{ORDINALS[n]} Species"].append(pred.index[n])
            predictions[f"{ORDINALS[n]} Score"].append(pred[n])

    end = datetime.now()
    print_prediction_time(end - start)
    return pd.DataFrame(predictions)


def predict_image(args):
    img = read_image(args["name"])
    animal, level, model = get_model(args)
    categories = pd.read_csv(CATEGORY_FILE)
    categories = categories[categories["class"].isin(ANIMAL_MAP[animal])][level].unique()
    return animal, level, pd.Series(model.predict(img[np.newaxis, ...])[0],
                                    index=categories).sort_values(ascending=False)
