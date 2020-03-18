from unittest import TestCase
from skimmer.prediction.model import get_animal, get_level


class TestGetModel(TestCase):
    def test_get_animal(self):
        bird = get_animal({"bird": True, "insect": False, "reptile": False})
        assert bird == "bird"
        insect = get_animal({"bird": False, "insect": True, "reptile": False})
        assert insect == "insect"
        reptile = get_animal({"bird": False, "insect": False, "reptile": True})
        assert reptile == "reptile"

    def test_wrong_animal(self):
        with self.assertRaises(Exception):
            get_animal({"lemur": True})

    def test_two_animal(self):
        with self.assertRaises(Exception):
            get_animal({"bird": True, "insect": True, "reptile": False})