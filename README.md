[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10684841.svg)](https://doi.org/10.5281/zenodo.10684841)

LAGT: Lemmatized Ancient Greek Texts
------------------------------------

## Citation

Vojtěch Kaše. (2024). LAGT (v3.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10684841

## Authors

* Vojtěch Kaše [![](https://orcid.org/sites/default/files/images/orcid_16x16.png)]([0000-0002-6601-1605](https://www.google.com/url?q=http://orcid.org/0000-0002-6601-1605&sa=D&ust=1588773325679000)), kase@ff.zcu.cz

(With contributions from many collaborators and colleagues: Tomáš Glomb, Vojtěch Linka, Viktor Zavřel, Nina Nikki, Zdeňka Špiclová etc.)

## Description

This repository serves for extraction, merging, cleaning morphological analysis and aggregation of publicly available ancient Greek texts accessible via two GitHub repositories:

* [Perseus Digital Library](https://github.com/PerseusDL/canonical-greekLit)
* [First 1000 Years of Greek](https://github.com/OpenGreekAndLatin/First1KGreek)

Concerning lemmatization, the dataset contains lemmatized sentences in a form of list-of-lists,
with sublist elements representing individual lemmata.
It contains only nouns, proper names, verbs and adjectives.
Wherever available, the lemmata are based on avaialable Treebank data, such as the GLAUx corpus (see below).
Where not, the GreCy model for spaCy is employed for automatic annotation.

In version v3.0 it includes 1,710 works from more than 325 authors, covering 32,323,612 tokens of raw text. It covers only works from the period from the 8th c. BCE to the 6th c. CE.

LAGT delivers all the data and metadata as one large tabular object, available for download either as a `json` or `parquet` file, which might be loaded directly into a Python environment as a dataframe using the Pandas library.

Individual works are represented by rows and columns represent attributes, such as the author ID (“doc\_id”, e.g. “tlg0086”) and document ID (“doc\_id”, e.g. “tlg010”) inherited from the source corpora, the date of creation expressed by means of an interval (“not\_before” and “not\_after”), manually annotated religious provenience as either pagan, Jewish or Christian (“provenience” attribute) etc., which allow various forms of sorting and filtering. The dating information is coded by means of the “not\_before” and “not\_after” attributes on the level of authors and with the precision of centuries.

---

### Lemmatization v3.0

The lemmata for individual documents come from several sources. See the column `"lemmata_source":`

* "morphgnt": Manually annotated lemmata for the Greek New Testament (tlg0031) according to SBLGNT, as available from here: https://github.com/morphgnt/sblgnt
* "lxxmorph" : Manually annotated lemmata for the Septuaging (tlg0527) according to the CCAT Gopher version, as available from here: https://github.com/nathans/lxxmorph-unicode/tree/master
* "agdt": lemmata extracted from a manually annotated selection of ancient Greek texts, extracted from http://perseusdl.github.io/treebank_data/ (also available [here](https://github.com/PerseusDL/treebank_data/tree/master/v2.1/Greek/texts))
* "gorman": lemmata from a manually annotated selection of ancient Grek texts, extracted from https://github.com/perseids-publications/gorman-trees/tree/master/public/xml (see [^1])
* "pedalion": lemmata from a manually annotated selection of ancient Grek texts, extracted from https://github.com/perseids-publications/pedalion-trees/tree/master/public/xml
* "glaux": lemmata from a large portion of *automatically* annotated ancient Greek texts, extracted from https://github.com/perseids-publications/glaux-trees/tree/master/public/xml (see [^2])
* "grecy": lemmata obtain from *automatically* annotated ancient Greek texts by means of the `grecy` model for `spaCy`.


### Software

1. Python 3
2. Jupyter Lab/Hub/Notebooks (Jupyter notebooks files)


## License

CC-BY-SA 4.0, see attached License.md

[^1]: Gorman, V. B. (2020). Dependency Treebanks of Ancient Greek Prose. Journal of Open Humanities Data, 6(1), 1. https://doi.org/10.5334/johd.13
    
[^2]: Keersmaekers, A. (2021). The GLAUx corpus: Methodological issues in designing a long-term, diverse, multi-layered corpus of Ancient Greek. Proceedings of the 2nd International Workshop on Computational Approaches to Historical Language Change 2021, 39–50. https://doi.org/10.18653/v1/2021.lchange-1.6
