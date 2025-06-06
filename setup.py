from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
    name='moexapiparser',
    version='0.1.0',
    long_description=readme(),
    long_description_content_type='text/markdown',
    description='A module for parsing MOEX financial data',
    author='Sukhanov_Maxim',
    author_email='mssukhanov@gmail.com',
    packages=find_packages(),
    keywords='moex api parser ',
    install_requires=[
        'pandas',
        'numpy',
        'requests',
        'certifi',
    ],
    url='https://github.com/MaximSukh/moexapiparser',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
