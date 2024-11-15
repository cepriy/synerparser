import stanza
import sys
import pandas
import csv


def sent_to_pos_ner(fragment, nlp):

    resulting_text = ""
    doc = nlp(fragment)
    print(doc)
    for sentence in doc.to_dict():
        for sentence in doc.to_dict():
            for word in sentence:
                if "upos" in word.keys():
                    resulting_text += word["text"] + "_" + word["upos"]
                    if "ner" in word.keys():
                        resulting_text += "_" + word["ner"]
                    if "xpos" in word.keys():
                        resulting_text += "_" + word["xpos"]
                    if "deprel" in word.keys():
                        resulting_text += "_" + word["deprel"] + "_" + sentence[word["head"] - 1]["text"] + "_"
                    if "lemma" in word.keys():
                        resulting_text += "(" + word["lemma"] + ") "
            else:
                resulting_text += word["text"]

        resulting_text += "\n"
    return resulting_text

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nlp_orig = stanza.Pipeline(sys.argv[2])
    # nlp_transl = stanza.Pipeline(sys.argv[3])
    df = pandas.read_csv("en_viet_un_chart_I_art_1_2.csv")
    df = df.reset_index()  # make sure indexes pair with number of rows
    resulting_df = pandas.DataFrame(columns=('original', 'translation'))
    resulting_dict = {"original": [], "translation": []}
    for index, row in df.iterrows():
        # print(row['original'], row['translation'])
        # print(sent_to_pos_ner(row['original'], nlp_orig))
        # resulting_dict["original"].append(sent_to_pos_ner(row['original'], nlp_orig))
        # resulting_dict["translation"].append(sent_to_pos_ner(row['translation'], nlp_transl))
        df2 = pandas.DataFrame.from_dict({"original": [sent_to_pos_ner(row['original'], nlp_orig)], "translation": [sent_to_pos_ner(row['translation'], nlp_orig)]})
        resulting_df = pandas.concat([resulting_df, df2])

        #resulting_df.concat({"original": sent_to_pos_ner(row['original'], nlp_orig), "translation": sent_to_pos_ner(row['translation'], nlp_transl)}, ignore_index=True)
        pandas.concat([resulting_df, pandas.Series({"original": "s", "translation": "f"}).to_frame().T], ignore_index=True)
    print("resulting_df")
    print(resulting_df)
    resulting_df.to_csv("resulting_df.csv")
    # with open('output.csv', 'w', encoding="utf-8") as csv_file:
    #     writer = csv.writer(csv_file)
    #     for key, value in resulting_dict.items():
    #         writer.writerow([key, value])


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


