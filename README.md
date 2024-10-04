[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13889714.svg)](https://doi.org/10.5281/zenodo.13889714)

LAGT: Lemmatized Ancient Greek Texts (v4.1)
------------------------------------

## Citation

Vojtěch Kaše, Söderholm, H., Vesala, J., & Nikki, N. (2024). LAGT (v4.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.13889714

## Description

This repository contains scripts and additional data used for production of the LAGT dataset.

LAGT is s a dataset of lemmatized ancient Greek texts, combining works from the Perseus Digital Library, the First 1000 Years of Greek, the GLAUx corpus, and a subset of additional early Christian texts added gradually.

In version v4.1,  LAGT includes 1,958 works from more than 475 authors, covering 35,809,325 tokens of raw text. It includes only works from the period from the 8th c. BCE to the 6th c. CE. Since version 4.0, LAGT dataset consists of two main components:

Main tabular dataset, containing all metadata and also lemmatized filtered sentences, offered here as a parquet file, to be loaded into python directly as a pandas dataframe object.
Morphological data for each document within the corpus with one JSON file per document. Each file is represented as a list of sentences, and each sentence is accompanied by a simplified morphological annotation, containing token, lemma, simplified postag and a positional index of the token. The directory with these files has to be downloaded and unzipped, e.g. in "data/large_files/ subdirectory of a repository or so.
The tabular dataset might be loaded directly into a Python environment as a dataframe using the Pandas library. You can load the dataset directly into your Python environment using the following piece of code:

import pandas as pd
LAGT = pd.read_parquet("https://zenodo.org/records/13761722/files/LAGT_v4-0.parquet?download=1")
Individual works are represented by rows and columns represent attributes, such as the author ID (“doc_id”, e.g. “tlg0086”) and document ID (“doc_id”, e.g. “tlg010”) inherited from the source corpora, the date of creation expressed by means of an interval (“not_before” and “not_after”), manually annotated religious provenience as either pagan, Jewish or Christian (“provenience” attribute) etc., which allow various forms of sorting and filtering. The dating information is coded by means of the “not_before” and “not_after” attributes on the level of authors and with the precision of centuries.

Concerning lemmatization, the dataset contains lemmatized sentences in the "lemmatized_sentences" attribute in form of a list-of-lists, with sublist elements representing individual lemmata. It contains only nouns, proper names, verbs and adjectives.
Wherever available, the lemmata are based on avaialable Treebank data, such as the GLAUx corpus (see below).
Where not, the GreCy model for spaCy is employed for automatic annotation.

The source of the lemmata for individual documents is documented in the "lemmata_source" attribute. Since version 4.0, the lemmata come exclusively either from GLAUx or from grecy.

"glaux": lemmata from a large portion of *automatically* annotated ancient Greek texts, extracted from https://github.com/perseids-publications/glaux-trees/tree/master/public/xml
"grecy": lemmata obtain from *automatically* annotated ancient Greek texts by means of the *grecy* model for *spaCy*.

### Software

1. Python 3
2. Jupyter Lab/Hub/Notebooks (Jupyter notebooks files)


## License

CC-BY-SA 4.0, see attached License.md
