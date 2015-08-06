import sys

from setuptools import setup, find_packages

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_mako',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'wtforms',
    'nose',
    'mako',
    'python-dateutil'
]

if sys.version_info[:3] < (2, 5, 0):
    requires.append('pysqlite')

setup(
    name='PyCK',
    version='0.9.8.6',
    description='Python Code Karigar - Web Framework',
    long_description="""PyCK is an "opinionated" web framework based on Pyramid that makes choices of
    ORM (SQLAlchemy), Templates(Mako) etc and aims at building more reusable componenets on top of these choices.""",
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Kashif Iftikhar',
    author_email='kashif@compulife.com.pk',
    url='http://pyck.compulife.com.pk',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='combined_apps',
    install_requires=requires,
    entry_points="""\
    [pyramid.scaffold]
    pyck=pyck.scaffolds:PyCKTemplate
    """,
)

