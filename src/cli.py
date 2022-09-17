"""Main adam-sandler CLI."""
import os
import sys
import click
from . import __version__


here = os.path.dirname(os.path.abspath(__file__))


@click.command()
def main():
    """
    Simple command line tool that just prints some version information
    """
    python_version = sys.version[:3]
    try:
        asvr = "adam-sandler {}".format(__version__)
        pyvr = "python {}".format(python_version)
        click.echo(asvr)
        click.echo(pyvr)

    except Exception as error:
        click.echo(error)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
