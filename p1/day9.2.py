import re

def remove_english_words_from_file(input_filename, output_filename=None):
    # If no output filename is specified, use a default one
    if output_filename is None:
        output_filename = "output2.txt"
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file, \
             open(output_filename, 'w', encoding='utf-8') as output_file:
            
            for line in input_file:
                # Use regex to find and remove [en] and the following English word
                processed_line = re.sub(r'\[en\]\w+\s*', '', line)
                output_file.write(processed_line)
                
        print(f"Processing complete. Output written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")

# Example usage:
input_filename = "output1.txt"  # Replace with your input file name
output_filename = "output2.txt"  # Replace with desired output file name, if different

remove_english_words_from_file(input_filename, output_filename)