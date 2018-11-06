from setuptools import setup

setup(name='Nave-Powers Python Package',
      version='0.1',
      description='Read matrix and run BLAST searches',
      url='TBD',
      author='Laurel Nave-Powers',
      author_email='laurel.nave-powers@selu.edu',
      license='MIT',
      packages=['nave-powerspythonpackage'],
      install_requires=[
          'dendropy',
          'pandas',
          'biopython'
      ],
      long_description=open('README.txt').read(),
zip_safe=True)