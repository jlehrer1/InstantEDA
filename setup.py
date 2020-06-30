from distutils.core import setup
setup(
  name = 'quickplotter',         # How you named your package folder (MyLib)
  packages = ['quickplotter'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Instantly generate common EDA plots without cleaning your DataFrame',   # Give a short description about your library
  long_description="""# Instant EDA (Work in progress!)
	Instantly generate common exploratory data plots without having to worry about cleaning your data.

	To setup the proper development environment, run `conda env create -f environment.yml`

	Usage:
	```python3
	plotter = quickplotter.QuickPlotter(df: pd.DataFrame) #creates a QuickPlotter object with the given DataFrame
	
	plotter.common(subset=['correlation', 'percent_nan']) #plots correlation between features, and percent nan in each column
	
	plotter.distribution(column_subset=df.columns[0:4]) #plots distributions for the first four columns in the DataFrame

	```

	The quickplot module works mainly with two specifications, `subset` and `diff`. 

	For any `subset`-like list, the items in the list will be used. For any `diff`-like list, all items *except* those in the list will be used. 

	To specifiy column `subset`'s or `diff`'s, call each plot individually or call `.common` with the `column_subset` or `column_diff` attributes (need to be added as of 6/18/20).
	""",
  author = 'Julian Lehrer',                   # Type in your name
  author_email = 'julianmlehrer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/jlehrer1/InstantEDA',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jlehrer1/InstantEDA/archive/0.1.tar.gz',    # I explain this later on
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
)
