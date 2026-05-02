"""Main adam-sandler CLI."""
import random
import sys
import click
from . import __version__
from .movies import get_movies
from .quotes import random_quote


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """adam-sandler: a totally serious Adam Sandler movie CLI."""
    if ctx.invoked_subcommand is None:
        version()


@main.command()
def version():
    """Print version information."""
    python_version = sys.version[:3]
    try:
        click.echo("adam-sandler {}".format(__version__))
        click.echo("python {}".format(python_version))
    except Exception as error:
        click.echo(error)
        sys.exit(1)


@main.command()
def list():
    """List all Adam Sandler movies."""
    movies = get_movies()
    for m in movies:
        icon = "+" if m["category"] == "good" else "-"
        click.echo(" {} {} ({})".format(icon, m["title"], m["year"]))


@main.command(name="random")
def random_cmd():
    """Pick a random Adam Sandler movie."""
    m = random.choice(get_movies())
    icon = "+" if m["category"] == "good" else "-"
    click.echo(" {} {} ({})".format(icon, m["title"], m["year"]))


@main.command()
def quote():
    """Print a random Adam Sandler movie quote."""
    q = random_quote()
    click.echo(' "{}"'.format(q["text"]))
    click.echo("   -- {} ({})".format(q["character"], q["movie"]))


if __name__ == "__main__":  # pragma: no cover
    main()
