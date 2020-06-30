import pathlib
from distutils.core import setup
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
  name = 'quickplotter',         # How you named your package folder (MyLib)
  packages = ['quickplotter'],   # Chose the same as "name"
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Instantly generate common EDA plots without cleaning your DataFrame',  
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Julian Lehrer',                   # Type in your name
  author_email = 'julianmlehrer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jlehrer1/InstantEDA',   # Provide either the link to your github or to your website
  download_url="https://github.com/jlehrer1/InstantEDA/archive/0.3.tar.gz",
  keywords = ['VISUALIZATION', 'PYTHON', 'DATA SCIENCE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
    	'numpy',
		'pandas',
		'plotly',
		'scikit-learn',  
	],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  include_package_data=True,
)
