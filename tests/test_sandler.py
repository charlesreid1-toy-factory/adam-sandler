import unittest

from click.testing import CliRunner

from adam_sandler.movies import (
    AdamSandlerMovie,
    GoodAdamSandlerMovie,
    BadAdamSandlerMovie,
    MOVIES,
    get_movies,
    get_good_movies,
    get_bad_movies,
)
from adam_sandler.quotes import QUOTES, random_quote
from adam_sandler.cli import main


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


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_version_command(self):
        result = self.runner.invoke(main, ["version"], catch_exceptions=False)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("adam-sandler", result.output)
        self.assertIn("python", result.output)

    def test_list_command(self):
        result = self.runner.invoke(main, ["list"], catch_exceptions=False)
        self.assertEqual(result.exit_code, 0)
        for m in get_movies():
            self.assertIn(m["title"], result.output)

    def test_random_command(self):
        result = self.runner.invoke(main, ["random"], catch_exceptions=False)
        self.assertEqual(result.exit_code, 0)
        titles = [m["title"] for m in get_movies()]
        self.assertTrue(any(t in result.output for t in titles))

    def test_quote_command(self):
        result = self.runner.invoke(main, ["quote"], catch_exceptions=False)
        self.assertEqual(result.exit_code, 0)
        # Should contain at least one quote text or movie title
        texts = [q["text"][:20] for q in QUOTES]
        movies = set(q["movie"] for q in QUOTES)
        self.assertTrue(
            any(t in result.output for t in texts)
            or any(m in result.output for m in movies)
        )


class TestQuotes(unittest.TestCase):
    def test_random_quote_returns_dict(self):
        q = random_quote()
        self.assertIn("text", q)
        self.assertIn("movie", q)
        self.assertIn("character", q)

    def test_quotes_have_required_fields(self):
        for q in QUOTES:
            self.assertIsInstance(q["text"], str)
            self.assertIsInstance(q["movie"], str)
            self.assertIsInstance(q["character"], str)
            self.assertGreater(len(q["text"]), 0)
            self.assertGreater(len(q["movie"]), 0)
            self.assertGreater(len(q["character"]), 0)

    def test_quotes_not_empty(self):
        self.assertGreater(len(QUOTES), 0)


if __name__ == "__main__":
    unittest.main()
