from tensorflow.keras.models import load_model
from efficientnet.tfkeras import *
from .config import ANIMAL_MAP, LEVELS, MODEL_FILE


def get_animal(args):
    try:
        animals = [a for a in ANIMAL_MAP.keys() if args[a]]
        if len(animals) != 1:
            raise
        else:
            return animals[0]
    except Exception as e:
        print(e)
        raise


def get_level(args):
    try:
        levels = [l for l in LEVELS if args[l]]
        if len(levels) != 1:
            raise
        else:
            return levels[0]
    except Exception as e:
        print(e)
        raise


def get_model(args):
    animal = get_animal(args)
    level = get_level(args)
    size = args["enet"]
    return animal, level, load_model(MODEL_FILE.format(animal=animal,
                                                       level=level,
                                                       size=size),
                                     compile=False)
