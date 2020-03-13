ANIMAL_MAP = {"bird": ["Aves"],
              "insect": ["Insecta"],
              "reptile": ["Amphibia", "Reptilia"]}
IMG_SIZE = 448
LEVELS = ["class", "order", "family", "genus", "species"]
CATEGORY_FILE = "./models/category_levels.csv"
MODEL_FILE = "./models/{animal}/enetB{size}_{level}.h5"
ORDINALS = ["First", "Second", "Third", "Fourth", "Fifth"]
PREDICTIONS = {"bird": {"order": 1,
                        "genus": 2,
                        "species": 5},
               "insect": {"order": 1,
                          "family": 2,
                          "genus": 2,
                          "species": 5},
               "reptile": {"class": 1,
                           "family": 1,
                           "species": 5}}

