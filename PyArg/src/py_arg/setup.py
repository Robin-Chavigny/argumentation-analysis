from setuptools import setup, find_packages

setup(
    name='py_arg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'dash',
        'dash-bootstrap-components==1.0.0',
        'dash_daq',
        'pandas',
        'parse',
    ],
    include_package_data=True,
)
