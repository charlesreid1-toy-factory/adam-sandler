from setuptools import setup, find_packages
from src import __version__

with open("requirements.txt") as f:
    all_deps = [x for x in f.read().splitlines() if not x.startswith("#")]
with open("requirements-dev.txt") as f:
    dev_deps = [x for x in f.read().splitlines() if not x.startswith("#")]

setup(
    name="adam-sandler",
    version=__version__,
    description="a dumb package",
    author="Chaz Reid",
    author_email="charlesreid1@gmail.com",
    url="https://github.com/charlesreid1-toy-factory/adam-sandler",
    packages=["adam_sandler"],
    package_dir={"adam_sandler": "src"},
    package_data={
        "adam_sandler": [
            "data/*.json",
            "data/*.txt",
        ]
    },
    entry_points={
        "console_scripts": [
            "adam-sandler=adam_sandler.cli:main",
        ],
    },
    license="MIT",
    install_requires=all_deps,
    extras_require={
        "test": dev_deps,
    #    "docs": dev_deps,
    #    "develop": dev_deps,
    },
)
