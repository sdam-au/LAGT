# !pip install greek-accentuation
from greek_accentuation.characters import strip_accents
from greek_accentuation.syllabify import *
from greek_accentuation.accentuation import *
import spacy
import re

nlp = spacy.load("../models/spacy_grc_model_6")
ag_lemma_lookup = nlp.vocab.lookups.get_table("lemma_lookup")

def grave_to_acute(string):
    GRAVE = "\u0300"
    ACUTE = "\u0301"
    return unicodedata.normalize("NFC", "".join(unicodedata.normalize("NFD", string).replace(GRAVE, ACUTE)))


def list_of_possible_accentuations(morph):
    try:
        if isinstance(morph, str):
            morph = strip_accents(morph)
            morph = rebreath(morph.lower())
            s = syllabify(morph)
            morph_vars = []
            for accentuation in possible_accentuations(s, default_short=True):
                pos, accent = accentuation #add_accentuation(s, accentuation))
                final = s[1 - pos:] if pos > 1 else [""]
                morph_acc_var = "".join(s[:-pos] + [syllable_add_accent(s[-pos], accent)] + final)
                morph_vars.append(morph_acc_var)
                morph_vars.append(morph_acc_var.capitalize())
            return morph_vars
        else:
            return []
    except:
        return []


def grc_doc_lemmatizer(doc):
    for token in doc:
        token.lemma_, token.pos_ = lemmatizer(token.text, token.pos_, token.lemma_)
    return doc   

def apply_nlp(sentences_list):
    spacy_docs = []
    for sentence in sentences_list:
        doc = nlp(sentence)
        spacy_docs.append(doc)
    return spacy_docs

def check_char_validity(token_text, tag):
    if re.search("\W", token_text):
        if re.match("\W+$", token_text):
            tag = "PUNCT"
        else:
            if "’" not in token_text:
                token_text = re.sub("\W", "", token_text)
    return token_text, tag

# for new tags in specific order...

keys = ['PRON', 'ADP', 'PUNCT', 'DET', 'CCONJ', 'INTJ', 'PART', 'ADJ', 'AUX', 'SCONJ', 'ADV', 'NOUN','PROPN', 'VERB','X', 'NUM']
 
def check_other_tags(token_text, tag):
    lemma = token_text
    match = False
    # for new tags in specific order...
    for new_tag in keys:
        try:
            lemma = ag_lemma_lookup[new_tag][token_text]
            tag = new_tag
            match = True
            break
        except:
            pass
    return lemma, tag, match


def lemmatizer_v1(token_text, tag, old_lemma=None):
    if (old_lemma==None) or (token_text == old_lemma):
        lemma = token_text.lower() # start with assigning the word as it stands
        try:
            lemma = ag_lemma_lookup[tag][token_text]
        except:
            try:
                lemma = ag_lemma_lookup_merged[token_text]
            except:
                try:
                    lemma = ag_lemma_lookup[tag][grave_to_acute(token_text)]
                except:
                    try:
                        lemma = ag_lemma_lookup_merged[grave_to_acute(token_text)]
                    except:
                        morph_vars = list_of_possible_accentuations(token_text)
                        for var in morph_vars:
                            try:
                                lemma = ag_lemma_lookup[tag][var] 
                                break
                            except:
                                try:
                                    lemma = ag_lemma_lookup_merged[var]
                                    break
                                except:
                                    pass
        return lemma, tag
    else:
        return old_lemma, tag
    
def lemmatizer(token_text, tag, old_lemma=None):
    if (old_lemma==None) or (token_text == old_lemma):
        token_text, tag = check_char_validity(token_text, tag)
        lemma = token_text.lower() # start with assigning the word as it stands
        try:
            lemma = ag_lemma_lookup[tag][token_text]
        except:
            try:
                lemma = ag_lemma_lookup[tag][grave_to_acute(token_text)]
            except:
                if check_other_tags(token_text, tag)[2] == True:
                    lemma, tag, match = check_other_tags(token_text, tag)
                else:
                        morph_vars = list_of_possible_accentuations(token_text)
                        for var in morph_vars:
                            try:
                                try:
                                    lemma = ag_lemma_lookup[tag][var] 
                                    break
                                except:
                                    a, b, match = check_other_tags(var, tag)
                                    if match ==True:
                                        lemma, tag, match = check_other_tags(var, tag)
                                        break
                            except:
                                pass

        return lemma, tag
    else:
        return old_lemma, tag