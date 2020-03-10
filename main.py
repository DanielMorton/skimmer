import argparse
import os

from output import output
from prediction import predict

STORE_TRUE = "store_true"


def main():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--name", required=True, type=str,
                    help="Name of image file")
    ap.add_argument("-e", "--enet", required=True, type=int,
                    help="Size of EfficientNet")
    animal_group = ap.add_mutually_exclusive_group(required=True)
    animal_group.add_argument("-i", "--insect", action=STORE_TRUE,
                              help="Identify Insect")
    animal_group.add_argument("-b", "--bird", action=STORE_TRUE,
                              help="Identify Bird")
    animal_group.add_argument("-r", "--reptile", action=STORE_TRUE,
                              help="Identify Reptile or Amphibian")
    animal_level = ap.add_mutually_exclusive_group(required=True)
    animal_level.add_argument("-c", "--class", action=STORE_TRUE,
                              help="Make a class level ID")
    animal_level.add_argument("-o", "--order", action=STORE_TRUE,
                              help="Make an order level ID")
    animal_level.add_argument("-f", "--family", action=STORE_TRUE,
                              help="Make a family level ID")
    animal_level.add_argument("-g", "--genus", action=STORE_TRUE,
                              help="Make a genus level ID")
    animal_level.add_argument("-s", "--species", action=STORE_TRUE,
                              help="Make a species level ID")
    args = vars(ap.parse_args())
    animal, level, pred = predict(args)
    output(pred, animal, level)


if __name__ == '__main__':
    main()
