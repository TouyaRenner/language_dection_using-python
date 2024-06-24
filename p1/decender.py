# Function to read words from the input file
def read_words(input_file):
    with open(input_file, 'r') as file:
        words = file.read().split()
    return words

# Function to write words to the output file
def write_words(words, output_file):
    with open(output_file, 'w') as file:
        for word in words:
            file.write(word + '\n')

# Main function to read, sort, and write words
def sort_words_ascending(input_file, output_file):
    words = read_words(input_file)
    sorted_words = sorted(words)
    write_words(sorted_words, output_file)

# Example usage
input_file = 'output.txt'
output_file = 'outpu1.txt'
sort_words_ascending(input_file, output_file)
