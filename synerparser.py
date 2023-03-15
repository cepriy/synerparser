# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import stanza
import sys

def text_to_pos_ner(file_path, language_code):
    nlp = stanza.Pipeline(language_code)
    resulting_text = ""
    text_fr_file = open(file_path, "r", encoding="utf-8")
    text = text_fr_file.read().replace("\n", "")
    doc = nlp(text)
    print(doc)
    for sentence in doc.to_dict():
        for word in sentence:
            resulting_text += word["text"] + "_" + word["upos"] + "_" + word["ner"] + "_" + word["deprel"] + "_" + sentence[word["head"]-1]["text"] +  " "
        resulting_text += "\n"
    return resulting_text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sys.argv[0])
    text_fr_file = open("un_ukr_art2.txt", "r", encoding="utf-8")
    text = text_fr_file.read().replace("\n", "")
    print(text)
    #stanza.download('uk')

    # doc = nlp(text)
    # print(doc.to_dict())
    # print(type(doc.to_dict()))
    #
    #
    # print(type(doc))
    # print(doc.sentences[1])
    # print("dependencies")
    # doc.sentences[1].print_tokens()
    # doc.sentences[1].print_words()

    input_file = open(sys.argv[1]+"_parsed", "w", encoding="utf-8")
    input_file.write(text_to_pos_ner(sys.argv[1], sys.argv[2]))
    # doc.sentences[1].print_dependencies()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/