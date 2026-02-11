from setuptools import setup, find_packages

setup(
    name="active_cookie",             
    version="1.0.0",                 
    packages=find_packages(),          
    python_requires=">=3.0",

    entry_points={
        'console_scripts': [
            'active-cookie=active_cookie.cli:main',
        ],
    },
)