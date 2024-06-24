import langid

# Path to your input and output files
input_file = 'output.txt'
output_file = 'output1.txt'

# Open input and output files
with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    # Read input file line by line
    for line in f_in:
        # Split line into words
        words = line.split()
        for word in words:
            # Detect language of each word
            lang, _ = langid.classify(word)
            # Write word and its language to output file
            f_out.write(f"[{lang}]{word}\t\n")
