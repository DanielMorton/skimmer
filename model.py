from tensorflow.keras.models import load_model

ANIMALS = ['birds', 'insects', 'reptiles']
LEVELS = ["class", "order", "family", "genus", "species"]
MODEL_FILE = "./models{animal}/enetB{size}_{level}.h5"


def get_animal(args):
    return [a for a in ANIMALS if a in args][0]


def get_level(args):
    return [l for l in LEVELS if l in args][0]


def get_model(args):
    animal = get_animal(args)
    level = get_level(args)
    size = args["enet"]
    return animal, level, load_model(MODEL_FILE.format(animal=animal,
                                                       level=level,
                                                       size=size))
