from gettext import install
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    package=find_packages(exclude=['test*']),
    license='MIT',
    description='A basic calculator',
    long_description=open('REAME.md').read(),
    install_reqires=[''],
    url='https://github.com/thembani47/mypackage',
    author='Thembani Maswanganyi',
    author_email='t.maswanganyi101@gmail.com'
)