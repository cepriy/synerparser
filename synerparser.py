import stanza
import sys

def text_to_pos_ner(file_path, language_code):
    nlp = stanza.Pipeline(language_code)
    resulting_text = ""
    text_fr_file = open(file_path, "r", encoding="utf-8")
    text = text_fr_file.read().replace("\n", "")
    doc = nlp(text)

    for sentence in doc.to_dict():
        for word in sentence:
            if "upos" in word.keys():
                resulting_text += word["text"] + "_" + word["upos"]
                if "ner" in word.keys():
                    resulting_text += "_" + word["ner"]
                if "xpos" in word.keys():
                    resulting_text += "_" + word["xpos"]
                if "deprel" in word.keys():
                    resulting_text += "_" + word["deprel"] + "_" + sentence[word["head"] - 1]["text"] + " "
            else:
                resulting_text += word["text"]

        resulting_text += "\n"
    return resulting_text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:\npython synerparser.py <filename> <language_code>")

    input_file = open(sys.argv[1]+"_parsed", "w", encoding="utf-8")
    input_file.write(text_to_pos_ner(sys.argv[1], sys.argv[2]))
    # doc.sentences[1].print_dependencies()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/