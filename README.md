[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10035517.svg)](https://doi.org/10.5281/zenodo.10035517)

LAGT: Lemmatized Ancient Greek Texts
---
## Citation
Vojtěch Kaše. (2023). LAGT (v2.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10035517
## Purpose


This repository serves for extraction, merging, cleaning and morphological analysis of publicly available ancient Greek texts accessible via two GitHub repositories:
* [Perseus Digital Library](https://github.com/PerseusDL/canonical-greekLit)
* [First 1000 Years of Greek](https://github.com/OpenGreekAndLatin/First1KGreek)

Concerning lemmatization, the dataset contains lemmatized sentences in a form of list-of-lists, 
with sublist elements representing individual lemmata. 
It contains only nouns, proper names, verbs and adjectives. 
Wherever available, the lemmata are based on avaialable Treebank data, such as the GLAUx corpus: https://github.com/perseids-publications/glaux-trees. 
Where not, the GreCy model for spaCy is employed for automatic annotation.

---
## Authors
* Vojtěch Kaše [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)]([0000-0002-6601-1605](https://www.google.com/url?q=http://orcid.org/0000-0002-6601-1605&sa=D&ust=1588773325679000)), vojtech.kase@gmail.com 

With contributions from many collaborators and colleagues: Tomáš Glomb, Vojtěch Linka, Viktor Zavřel, Nina Nikki, Zdeňka Špiclová etc.

## License
CC-BY-SA 4.0, see attached License.md



---
## Description v2.0

The lemmata for individual documents come from several sources. See the column `"lemmata_source":`
* "morphgnt": Manually annotated lemmata for the Greek New Testament (tlg0031) according to SBLGNT, as available from here: https://github.com/morphgnt/sblgnt
* "lxxmorph" : Manually annotated lemmata for the Septuaging (tlg0527) according to the CCAT Gopher version, as available from here: https://github.com/nathans/lxxmorph-unicode/tree/master
* "agdt": lemmata extracted from a manually annotated selection of ancient Greek texts, extracted from http://perseusdl.github.io/treebank_data/ (also available [here](https://github.com/PerseusDL/treebank_data/tree/master/v2.1/Greek/texts))
* "gorman": lemmata from a manually annotated selection of ancient Grek texts, extracted from https://github.com/perseids-publications/gorman-trees/tree/master/public/xml (see [^1])
* "pedalion": lemmata from a manually annotated selection of ancient Grek texts, extracted from https://github.com/perseids-publications/pedalion-trees/tree/master/public/xml
* "glaux": lemmata from a large portion of *automatically* annotated ancient Greek texts, extracted from https://github.com/perseids-publications/glaux-trees/tree/master/public/xml (see [^2])




[^1]: Gorman, V. B. (2020). Dependency Treebanks of Ancient Greek Prose. Journal of Open Humanities Data, 6(1), 1. https://doi.org/10.5334/johd.13
[^2]: Keersmaekers, A. (2021). The GLAUx corpus: Methodological issues in designing a long-term, diverse, multi-layered corpus of Ancient Greek. Proceedings of the 2nd International Workshop on Computational Approaches to Historical Language Change 2021, 39–50. https://doi.org/10.18653/v1/2021.lchange-1.6




## Description v2.0

The textual data consist of 1,457 ancient Greek works, 2,891,346 sentences and 31,248,866
words (1,255 documents, 1,783,275 sentences, 21,086074 words from the period from 8th c. BCE to 4 c. CE). Using [TLG metadata for dating](https://raw.githubusercontent.com/cltk/cltk/master/cltk/corpus/greek/tlg/author_date.py), we were able to get some sort of dating for 1,374 documents. Next to it, we were able to classify 876 as either "christian" or "pagan" provenience. 

The scripts are located in `scripts` folder and usually have a form of Jupyter notebooks.

* `1_DATA-EXTRACTION.ipynb` 
	* **description**: It extracts the data from public GitHub repositories (hundreds of tei-xml files), merges them into one Pandas dataframe and export this dataframe into a json file at sciencedata.dk. It also checks for duplicates in tlg codes in filesnames.  (e.g. `tlg0086.tlg010` is a tlg code for Aristotle's *Ethica Nicomachea*).
	* **input**:  xml files located on GitHub, scrapped directly from there
	* **output**: `AGT_raw_[yyyymmdd].json`
    
* `2_DATING&PROVENIENCE.ipynb` 
	* **description**:  This scripts enriches the raw data in various ways, especially by dating and cultural provenience. It also removes duplicates. It splits collective works (e.g. New Testament and Homeric Hymns) as produced by individual authors.
	* **input**: `AGT_raw_[yyyymmdd].json`
	* **output**:  `AGT_dated_[yyyymmdd].json`
  
* `3_PREPROCESSING&RAW-VECTORS.ipynb` 
	* **description**: It cleans the textual data, removes all odd characters etc., splits the text into sentences, generates word-vectors to help the POStagger.
    	* **input**: `AGT_dated_[yyyymmdd].json
    	* **output**: `AGT_preprocessed_[yyyymmdd].json`
    	* **output**: `data/word2vec_win2.txt`
  
* `4_LEMMATIZATION_with-spacy.ipynb` 
	* **description**: It produces lemmatized text as a list of words and a list of lemmatized sentences as a list of lists of words.
    	* **input**: `AGT_preprocessed_[yyyymmdd].json` 
    	* **output**: `AGT_lemmatized_[yyyymmdd].json` # full dataset with lemmatized sentences filtered by POStags (only NOUN, PROPN, ADJ, VERB)
    	* **output** `AGT_tagged_[yyyymmdd]` # full POStagged & lemmatized data, without metadata (> 3GB)
    
* `5_OVERVIEW.ipynb` 
	* **description**: It produces various overview figures and tables
    	* **input**: `AGT_lemmatized_[yyyymmdd].json`
    	* **output**: various figures and tables

The morphological analysis applied in `4_LEMMATIZATION_with-spacy.ipynb`has been implemented using spaCy and consists of (1) a **coarse-grained POS-tagging** and (2) a dictionary-based **lemmatization**.

(1) The POS-tagger has been trained using two universal dependency treebanks:
* [Perseus](https://github.com/UniversalDependencies/UD_Ancient_Greek-Perseus/tree/master) (11,476 train sentences, 1,137 test sentences)
* [PROIEL](https://github.com/UniversalDependencies/UD_Ancient_Greek-PROIEL/tree/master) (15,014 train sentences; 1,019 test sentences) 
(For details, see `scripts/TAGGER&LEMMATIZER_development.py`).

(2) The lemmatizer relies on a stable version of the Greek part of Morpheus dictionary [link]
(https://github.com/gcelano/LemmatizedAncientGreekXML/tree/master/Morpheus) containing  706,506 unique wordform-lemma pairs (we further extended it by  13,157 wordform-lemma pairs found in the training data. The dictionary was reorganized by items arranged by the postags:
```python
{"POSTAG1" : 
	{"wordform1" : "lemma1",
	 "wordform2" : "lemma1",
	 ...},	 
{"POSTAG2": : 
	{...}}
```
(For details see `scripts/MORPHEUS_PARSING+EXTENSION.ipynb`.

(2) The lemmatizor assigns lemmata from Morpheus on the basis of the POSTags. When it does not find any coinciding wordform-lemma pair, it tries to do a series of transformations with the wordform, namely automatic rebreathing, checking all possible accentuations. When still not successful, it tries to look for other POStags (For details, see `scripts/lemmatization.py`). In this way the lemmatizer might correct the POStagger.

**Model performance on two test data:**
```python
{'proiel_tags_correct%': 96.60123058892471,
'proiel_lemmata_correct%': 95.51714034573689,
'perseus_tags_correct%': 88.9405918229049,
'perseus_lemmata_correct%': 87.15608764400271}
```
(The results of this systematically underestimate the performance of the model because of some differences in tokenization between universal dependencies data and spaCy - we have to mode modify the tokenizer.)

---
### Data
The raw data are from two GitHub repositories:
* **Perseus Digital Library**:  https://github.com/PerseusDL/canonical-greekLit - XML Canonical resources for Greek Literature
* **Open Greek and Latin**: https://github.com/OpenGreekAndLatin/First1KGreek - XML files for the works in the First Thousand Years of Greek Project
* [Perseus Greek dependency treebank](https://github.com/UniversalDependencies/UD_Ancient_Greek-Perseus/tree/master) (11,476 train sentences, 1,137 test sentences)
* [PROIEL Greek dependency treebank](https://github.com/UniversalDependencies/UD_Ancient_Greek-PROIEL/tree/master) (15,014 train sentences; 1,019 test sentences) 

### Software
1. Python 3
2. Jupyter Lab/Hub/Notebooks (Jupyter notebooks files)
3. Sciencedata.dk web interface

### Registered account
1. Google account (to work with metadata, not necessary)
2. Github account (to extract the raw data straightforward from Github)
3. Sciencedata.dk account (to work with preprocessed data to which point the script, not necessary).
 
