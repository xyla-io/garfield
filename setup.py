from setuptools import setup, find_packages

setup(name='garfield',
      version='0.0.1',
      description='Xyla\'s Python Adjust KPI Service client.',
      url='https://github.com/xyla-io/garfield',
      author='Gregory Klein',
      author_email='gklei89@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'pandas',
      ],
      zip_safe=False)
