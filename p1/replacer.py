def load_mappings(file_path):
    mappings = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                lang_code, word = line.split(']')
                lang_code = lang_code[1:]  # Remove '['
                mappings[word.strip()] = lang_code
    return mappings

def replace_words(input_text, mappings):
    words = input_text.split()
    replaced_words = []
    for word in words:
        if word.lower() in mappings:
            replaced_words.append(f"[{mappings[word.lower()]}]{word}")
        else:
            replaced_words.append(word)
    return ' '.join(replaced_words)

def main():
    # Input file paths
    input_text_file = 'input.html'
    input_mapping_file = 'output2.txt'
    output_file = 'recreate.txt'

    # Load mappings
    mappings = load_mappings(input_mapping_file)

    # Read input text
    with open(input_text_file, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Replace words based on mappings
    output_text = replace_words(input_text, mappings)

    # Write output to file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_text)

    print(f"Output has been written to {output_file}")

if __name__ == "__main__":
    main()
