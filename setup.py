from setuptools import setup  # type:ignore
import os

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='nonogram_solver',
    version='0.1',
    description='A nonogram puzzle solver.',
    url='https://github.com/SpiritD/nonograms',
    author='Denis',
    keywords='python nonogram solver',
    packages=['nonogram_solver'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'coverage']
    }
)
