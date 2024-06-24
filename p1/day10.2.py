from bs4 import BeautifulSoup
import langdetect
from nltk import word_tokenize, ne_chunk

# Pre-load language identification model for efficient detection
langid.set_languages(['en'])  # Replace with a list of languages you want to identify

def read_html_file(file_path):
    """Read the content of an HTML file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_from_html(html_content):
    """Extract text from HTML content using BeautifulSoup."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def is_english(word):
    """Check if a word is likely English using language detection."""
    try:
        return langdetect.detect(word) == 'en'
    except langdetect.lang_detectException:
        # Handle potential errors during language detection
        return False

def find_non_english_words(text):
    """Find all non-English words in the text (excluding potential proper nouns)."""
    words_list = word_tokenize(text)
    non_english_words = []
    for word in words_list:
        if not is_english(word) and not is_named_entity(word):
            non_english_words.append(word)
    return non_english_words

def is_named_entity(word):
    """Simple check for named entities using NLTK's chunking (can be improved)."""
    # Replace with a more comprehensive NER approach if needed
    tags = ne_chunk(word_tokenize([word]))
    return any(tag[1] != 'O' for tag in tags)  # Check for non-Other tags

def write_to_output_file(words, output_file_path):
    """Write the non-English words to an output text file."""
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

def main(input_html_path, output_txt_path):
    """Main function to coordinate the process."""
    html_content = read_html_file(input_html_path)
    text_content = extract_text_from_html(html_content)
    non_english_words = find_non_english_words(text_content)
    write_to_output_file(non_english_words, output_txt_path)
    print(f"Non-English words have been written to {output_txt_path}")

if __name__ == "__main__":
    input_html_path = 'input.html'  # Path to your HTML file
    output_txt_path = 'output.txt'  # Path to your output text file
    main(input_html_path, output_txt_path)
