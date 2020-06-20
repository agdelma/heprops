import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='heprops',
    version='1.0.0',
    packages=setuptools.find_packages(),
    license='MIT',
    description='Properties of the chemical element helium.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy','scipy'],
    python_requires='>=3.6',
    url='https://github.com/agdelma/heprops',
    author='Adrian Del Maestro',
    author_email='adrian@delmaestro.org',
    classifiers=[
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3.6',
   'Programming Language :: Python :: 3.7',
   'Topic :: Scientific/Engineering :: Physics']
)
