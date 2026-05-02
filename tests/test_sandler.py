import unittest

from adam_sandler.movies import (
    AdamSandlerMovie,
    GoodAdamSandlerMovie,
    BadAdamSandlerMovie,
    MOVIES,
    get_movies,
    get_good_movies,
    get_bad_movies,
)


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

    def test_get_movies_returns_all(self):
        movies = get_movies()
        self.assertEqual(len(movies), len(MOVIES))
        self.assertGreater(len(movies), 0)

    def test_get_good_movies(self):
        good = get_good_movies()
        self.assertGreater(len(good), 0)
        for m in good:
            self.assertEqual(m["category"], "good")

    def test_get_bad_movies(self):
        bad = get_bad_movies()
        self.assertGreater(len(bad), 0)
        for m in bad:
            self.assertEqual(m["category"], "bad")

    def test_movie_structure(self):
        for m in get_movies():
            self.assertIn("title", m)
            self.assertIn("year", m)
            self.assertIn("category", m)
            self.assertIsInstance(m["title"], str)
            self.assertIsInstance(m["year"], int)
            self.assertIn(m["category"], ("good", "bad"))


if __name__ == "__main__":
    unittest.main()
