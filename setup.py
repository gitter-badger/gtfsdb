from setuptools import setup, find_packages
import sys


extras_require = dict(
    dev=[],
    oracle=['cx_oracle>=5.1'],
)

install_requires = ['sqlalchemy == 0.8.6', 'geoalchemy>=0.7.2', 'psycopg2>=2.4.2']
if sys.version_info[:2] <= (2, 6):
    install_requires.append('argparse>=1.2.1')
    extras_require['dev'].append('unittest2')

setup(
    name='gtfsdb',
    version='0.1.6dev',
    description='GTFS Database',
    long_description=open('README').read(),
    keywords='GTFS',
    author='Mike Gilligan',
    author_email='gilligam@trimet.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'gtfsdb-load = gtfsdb.scripts:gtfsdb_load',
            'rs-test = gtfsdb.scripts:route_stop_load'
        ]
    },
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
