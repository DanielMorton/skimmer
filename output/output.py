import numpy as np

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


def output(pred, animal, level):
    for n in range(PREDICTIONS[animal][level]):
        print(f"#{n + 1} {pred.index[n]} with score {100 * np.round(pred[n], 3)}")


def save_output(preds, output_file):
    preds.to_csv(output_file)
