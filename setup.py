"""
more.colander
------------
Colander for Morepath.
"""

import io
from setuptools import (
    setup,
    find_packages
)

try:
    import pypandoc
except ImportError:
    print('pypandoc not found, could not convert Markdown to RST')
    pypandoc = None


def read_md(f):
    if pypandoc:
        return pypandoc.convert(f, 'rst')
    return io.open(f, encoding='utf-8').read()


version = '0.1.0-dev0'

long_description = '\n'.join((
    read_md('README.md'),
    read_md('CHANGES.md')
))

install_requires = [
    'morepath >= 0.18',
    'colander'
]

tests_require = [
    'pytest',
    'coverage',
    'pytest-cov',
    'webtest'
]

docs_require = [
    'sphinx',
    'docutils'
]

pypi_require = [
    'pypandoc',
    'twine'
]


setup(
    name='more.colander',
    version=version,
    url='https://github.com/morepath/more.colander',
    license='BSD',
    author='Blaise Laflamme',
    author_email='blaise@laflamme.org',
    description='Colander for Morepath',
    long_description=long_description,
    keywords='morepath validation schemas colander',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    namespace_packages=['more'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'docs': docs_require,
        'pypi': pypi_require
    },
    test_suite='more.colander'
)
