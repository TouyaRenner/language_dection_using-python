from bs4 import BeautifulSoup
from langdetect import detect
import re

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def is_english(word):
    try:
        return detect(word) == 'en'
    except:
        return False

def find_non_english_words(text):
    words = re.findall(r'\b\w+\b', text)
    non_english_words = [word for word in words if not is_english(word)]
    return non_english_words

def write_to_output_file(words, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

def main(input_html_path, output_txt_path):
    html_content = read_html_file(input_html_path)
    text_content = extract_text_from_html(html_content)
    non_english_words = find_non_english_words(text_content)
    write_to_output_file(non_english_words, output_txt_path)
    print(f"Non-English words have been written to {output_txt_path}")

if __name__ == "__main__":
    input_html_path = 'input.html'  # Path to your HTML file
    output_txt_path = 'output.txt'  # Path to your output text file
    main(input_html_path, output_txt_path)
