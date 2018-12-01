from setuptools import setup, find_packages

setup(
    name = "Alchemist",
    version = "0.1.0",
    packages = find_packages(exclude=['*test']),
    install_requires = ['argparse'],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:process'
        ]
    }
)
