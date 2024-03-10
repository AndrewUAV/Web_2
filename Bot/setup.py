from setuptools import setup,find_packages


setup(
    name='Bot',
    version='1.1',
    entry_points={
        'console_scripts':['Bot=app.__main__:main']
    },
    packages=find_packages()
)