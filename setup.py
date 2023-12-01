from setuptools import setup, find_packages

setup(
    name='oasdowngrade',
    version='0.1.0',
    packages=find_packages(include=['src']),
    entry_points={
        'console_scripts': ['oasdowngrade=src.oasdowngrade:main']
    }
)