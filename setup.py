from setuptools import setup, find_packages

setup(
    name = "alchemist",
    version = "0.1.0",
    summary = "Library for simulating 2-shelf wizardry reactions.",
    author = "Isak Falk",
    author_email = "ucabitf@ucl.ac.uk",
    licence = "MIT",
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse', 'pyyaml', 'pytest'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]
    }
)
