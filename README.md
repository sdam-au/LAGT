# AGT: Ancient Greek Texts
---

## Purpose
The purpose of this repository is to extract, merge and clean all digitally available ancient Greek texts available in GitHub repositories associted with two projecty:
* Perseus Digital Library 
* First 1000 Years of Greek 

---
## Authors
* Vojtěch Kaše [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)]([0000-0002-6601-1605](https://www.google.com/url?q=http://orcid.org/0000-0002-6601-1605&sa=D&ust=1588773325679000)), SDAM project, vojtech.kase@gmail.com


## License
CC-BY-SA 4.0, see attached License.md

## DOI
[Here will be DOI or some other identifier once we have it]

### References
[Here will go related articles or other sources we will publish/create]

---
# How to use this repository

## Sources and prerequisites
This repository contains scripts in Python 3. These scripts are mainly in  Jupyter Notebook file format and were developed primarily for usage in Google Colaboratory. However, it should be also possible to run them with your local Python and Jupyter Notebook/Lab environment. 

### Data
The raw data are from two GitHub repositories:
* **Perseus Digital Library**:  https://github.com/PerseusDL/canonical-greekLit - XML Canonical resources for Greek Literature
* **Open Greek and Latin**: https://github.com/OpenGreekAndLatin/First1KGreek - XML files for the works in the First Thousand Years of Greek Project

### Software
1. Google Colaboratory
1. Sciencedata.dk web interface

### Registered account
1. Google account
2. Github account (to get raw data)
3. Sciencedata.dk account (to work with preprocessed data to which point the script.
4. S

## Instructions 

You can either (1) clone the repo into your Google Drive and then open the scripts directly in Google Colab (2) clone the repo into your local hard drive and run the scripts with your local Jupyter, (3) open Google Colab and choose an option to open a file from Github.

* `1_DATA-EXTRACTION.ipynb` 
	* **description**: It extracts the data from public GitHub repositories (hundreds of tei-xml files), merges them into one Pandas dataframe and export this dataframe into a json file at sciencedata.dk. It also checks for duplicates in tlg codes in filesnames.  (e.g. `tlg0086.tlg010` is a tlg code  code for Aristotle's *Ethica Nicomachea*).
	* **input**:  xml files located on GitHub, scrapped directly from there
	* **output**: `SDAM_root/SDAM_data/AGT/data_merged_raw.json` -
* `
* `2_METADATA&LEMMATIZATION&OVERVIEW.ipynb` 
	* **description**:  This scripts enriches the raw data in various ways, especially by dating and cultural provenience. Subsequently, it also applies functions from **anda.gr** package for lemmatization.
	* **input**: `SDAM_root/SDAM_data/AGT/data_merged_raw.json`
	* **output**:  `AGT.json` or `AGT_[timestamp].json`
* `VARIOUS.ipynb` 
	* **description**: ` various scripts, mainly for testing


Using [TLG metadata for dating](https://raw.githubusercontent.com/cltk/cltk/master/cltk/corpus/greek/tlg/author_date.py), we were able to get some sort of dating for 1,374 documents.

Next to it, we were able to classify 876 as either "christian" or "pagan" provenience. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU1OTI4MzcwMiwtMTc4NjI3NzA0Nyw0NT
IzNzcwMTYsLTYxMDAzNzc1MSwxNjkyNTY4ODkwLC0xNTE5NjIy
ODExXX0=
-->                                                                                                                                                                                                                                             