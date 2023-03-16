## Synerparser

# Description

This script is aimed at tagging text in a utf-8 encoded .txt file with pos_ner_deprel_head notation. I.e., each token of the text 
gets assigned underscored tags in the following order: <TOKEN> <PART OF SPEECH> <NER> <TYPE OF SYNTACTIC DEPENDENCY> <TREEBANK_TAG> <DEPENDENCY_HEAD>
The tags are assigned as per [stanza](https://stanfordnlp.github.io/stanza/performance.html) library.

#Tagsets

[NER tags](https://github.com/stanfordnlp/stanza/issues/904)

[The POS tags are assigned as per UD](https://universaldependencies.org/u/pos/)

[Treebank specific POS tags (XPOS)](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

[Dependency relation tags](https://universaldependencies.org/docs/u/dep/index.html)

#Installation

'Synerparser' runs on Python 3.8 or later.

Install the 'stanza' library:
```
pip install stanza  
```

#Usage

To run the script, execute the command:
```

python synerparser.py <filename> <language_code>
```
The language codes are available [here](https://stanfordnlp.github.io/stanza/available_models.html).

The parsed file will be created in the same directory as the script.