from setuptools import setup

setup(
    name='snow_connector',
    version='0.1',
    description='utilities for connecting to ServiceNow',
    url='https://github.com/MikeRodziewicz/snow_connector_pck',
    author='MikeRodziewicz',
    author_email='mike.python.testing@gmail.com',
    license='unlicense',
    packages=['snow_connector'],
    install_requires=[
                    'python-dotenv',
                    'requests',
                    'aiohttp',
                    'Faker'
                    ],
    zip_safe=False
)

