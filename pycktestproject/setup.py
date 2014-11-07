import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'PyCK',
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_mako',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'webtest',
    'waitress',
    'wtforms',
    'wtdojo'
]

if sys.version_info[:3] < (2, 5, 0):
    requires.append('pysqlite')

setup(
    name='pycktestproject',
    version='0.0',
    description='pycktestproject',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: PyCK",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web PyCK framework pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='pycktestproject',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = pycktestproject:main
    [console_scripts]
    pycktestproject_populate = pycktestproject.scripts.populate:main
    pycktestproject_newapp = pycktestproject.scripts.newapp:main
    """,
)
