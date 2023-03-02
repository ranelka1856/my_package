import setuptools


with open('readme.md') as file:
    read_me_desc = file.read()

setuptools.setup(
    name='hamster_calc',
    version='0.1',
    author='Ranelka',
    author_email='hamster@gmail.com',
    description='Calculator for hamsters',
    long_description=read_me_desc,
    long_description_content_type='text/markdown',
    url='http://github.com/example',
    packages=['hamster_calc'],
    #install_requires=['logging'],
    python_requires='>=3.6',
)