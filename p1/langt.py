import sys
from langdetect import detect
from googletrans import Translator

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        print("Error detecting language:", e)
        return None

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        print("Error translating text:", e)
        return None

def main(input_file, output_file, dest_language):
    # Read the input file
    original_text = read_file(input_file)
    
    if not original_text:
        print("Input file is empty or cannot be read.")
        return
    
    # Detect the original language
    original_language = detect_language(original_text)
    if not original_language:
        print("Could not detect language. Translation aborted.")
        return
    print(f"Detected language: {original_language}")
    
    # Translate the text
    translated_text = translate_text(original_text, dest_language)
    if not translated_text:
        print("Translation failed.")
        return
    print(f"Translated to: {dest_language}")
    
    # Write the translated text to the output file
    write_file(output_file, translated_text)
    print(f"Translation saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python translate_document.py <input_file> <output_file> <dest_language>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        dest_language = sys.argv[3]
        main(input_file, output_file, dest_language)
