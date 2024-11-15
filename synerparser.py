import os
import sys
import stanza

def text_to_pos_ner(file_path, language_code):
    nlp = stanza.Pipeline(language_code)
    resulting_text = ""
    with open(file_path, "r", encoding="utf-8") as text_file:
        text = text_file.read().replace("\n", "")
    doc = nlp(text)

    for sentence in doc.to_dict():
        for word in sentence:
            if "upos" in word.keys():
                resulting_text += word["text"] + "_" + word["upos"]
                # Uncomment these lines to include additional annotations
                # if "ner" in word.keys():
                #     resulting_text += "_" + word["ner"]
                # if "xpos" in word.keys():
                #     resulting_text += "_" + word["xpos"]
                # if "deprel" in word.keys():
                #     resulting_text += "_" + word["deprel"] + "_" + sentence[word["head"] - 1]["text"]
                # if "lemma" in word.keys():
                #     resulting_text += "(" + word["lemma"] + ")"
                resulting_text += " "
            else:
                resulting_text += word["text"]

        resulting_text += "\n"
    return resulting_text

def process_file(file_path, language_code):
    """Process a single file."""
    print(f"Processing file: {file_path}")
    output_file_path = file_path + "_parsed"
    parsed_text = text_to_pos_ner(file_path, language_code)
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(parsed_text)
    print(f"Output written to: {output_file_path}")

def process_folder(folder_path, language_code):
    """Process all files in a folder."""
    print(f"Processing folder: {folder_path}")
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            process_file(file_path, language_code)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:\npython synerparser.py <file_or_folder> <language_code>")
        sys.exit(1)

    path = sys.argv[1]
    language_code = sys.argv[2]

    if os.path.isfile(path):
        process_file(path, language_code)
    elif os.path.isdir(path):
        process_folder(path, language_code)
    else:
        print(f"Error: {path} is neither a file nor a folder.")
        sys.exit(1)
