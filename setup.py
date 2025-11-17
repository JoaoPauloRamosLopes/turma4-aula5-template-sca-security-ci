from setuptools import setup, find_packages

setup(
    name="app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests==2.19.1',
    ],
    python_requires='>=3.6',
)
