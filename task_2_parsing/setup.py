import setuptools
from os.path import join, dirname


setuptools.setup(
    name='text_view_of_date',
    version='1.0',
    packages=setuptools.find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
)
