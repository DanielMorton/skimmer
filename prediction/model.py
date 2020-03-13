from tensorflow.keras.models import load_model
from efficientnet.tfkeras import *
from . import ANIMAL_MAP, LEVELS, MODEL_FILE


def get_animal(args):
    return [a for a in ANIMAL_MAP.keys() if args[a]][0]


def get_level(args):
    return [l for l in LEVELS if args[l]][0]


def get_model(args):
    animal = get_animal(args)
    level = get_level(args)
    size = args["enet"]
    return animal, level, load_model(MODEL_FILE.format(animal=animal,
                                                       level=level,
                                                       size=size),
                                     compile=False)
