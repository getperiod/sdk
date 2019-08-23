import setuptools
from pathlib import Path

setuptools.setup(
    name='period',
    version='0.0.2',
    author='Breitburg Elias',
    author_email='contact@breitburg.me',
    long_description=open(str(Path(__file__).resolve().parent.joinpath('readme.md')), 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url='https://github.com/breitburg/period',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open(str(Path(__file__).resolve().parent.joinpath('requirements.txt')), 'r').read().split('\n')
)
