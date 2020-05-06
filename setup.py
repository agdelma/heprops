from setuptools import setup, find_packages

setup(
    name='heprops',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='Properties of the chemical element helium.',
    long_description=open('README.md').read(),
    install_requires=['numpy','scipy'],
    url='https://github.com/agdelma/heprops',
    author='Adrian Del Maestro',
    author_email='adrian@delmaestro.org'
)
