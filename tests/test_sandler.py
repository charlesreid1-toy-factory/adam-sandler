import os
import sys
import unittest

from adam_sandler.movies import AdamSandlerMovie, GoodAdamSandlerMovie, BadAdamSandlerMovie

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa


class TestMovies(unittest.TestCase):
    def test_movies(self):

        title = "Happy Gilmore"

        # base
        with self.assertRaises(Exception):
            _ = AdamSandlerMovie()

        hg = AdamSandlerMovie(title)
        self.assertIn(title, hg.title)

        # good
        with self.assertRaises(NotImplementedError):
            _ = GoodAdamSandlerMovie()
            _ = GoodAdamSandlerMovie(title)

        # bad
        with self.assertRaises(Exception):
            _ = BadAdamSandlerMovie()

        hg = BadAdamSandlerMovie(title)
        self.assertIn(title, hg.title)


if __name__ == "__main__":
    unittest.main()
