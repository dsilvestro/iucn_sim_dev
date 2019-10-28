import sys
from setuptools import setup
import versioneer

if sys.version_info < (3, 6):
	sys.stdout.write("At least Python 3.6 is required.\n")
	sys.exit(1)

with open('README.md') as f:
	long_description = f.read()


setup(
	name = 'iucn_sim',
	version = versioneer.get_version(),
	cmdclass = versioneer.get_cmdclass(),
	author = 'Tobias Andermann',
	author_email = 'tobias.andermann@bioenv.gu.se',
	url = 'https://github.com/tobiashofmann88/iucn_extinction_simulator',
	description = 'Estimate extinction probabilities and dates for a given set of species, based on IUCN threat assessments',
	long_description = long_description,
	license = 'MIT',
	entry_points = {'console_scripts': ['iucn_sim = iucn_sim.__main__:main']},
	packages = ['iucn_sim'],
    install_requires = [
	    # No dependencies listed here since we need to rely on conda anyway
    ],
	classifiers = [
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3.6",
		"Topic :: Scientific/Engineering :: Bio-Informatics"
	]
)
