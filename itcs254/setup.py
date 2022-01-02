import setuptools

URL = "https://github.com/lasthunter657/DIscrete-254"


setuptools.setup(
    name='itcs254',
    version='0.1.0',

    author=['hussain', 'ali'],
    author_email='',

    description="Set of python program that can solve discrete math problem",

    url=URL,
    project_urls={
        'Bug Tracker': f"{URL}/issues",
    },

    python_requires='>=3.10',

    install_requires=[
        'pytest'
    ],

    package_dir={'': 'src'},

    packages=setuptools.find_packages(where='src'),
)
