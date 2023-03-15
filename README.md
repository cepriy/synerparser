This script is aimed at tagging text in a utf-8 encoded .txt file with pos_ner_deprel_head notation. I.e., each token of the text 
gets assigned underscored tags in the following order: _<PART OF SPEECH>_<NER>_<TYPE OF SYNTACTIC DEPENDENCY>_<DEPENDENCY_HEAD>
The tags are assigned as per stanza library: https://stanfordnlp.github.io/stanza/performance.html

The POS tags are assigned as per UD:
https://universaldependencies.org/u/pos/
Dependency relation tags:
https://universaldependencies.org/docs/u/dep/index.html
NER tags:
https://github.com/stanfordnlp/stanza/issues/904

To run the script, use the command

python synerparser.py <filename> <language>

The available language codes are here:
https://stanfordnlp.github.io/stanza/available_models.html

The parsed file will be created in the same directory as the script.