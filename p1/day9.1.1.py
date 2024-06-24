import langid

# Path to your input and output files
input_file = 'output.txt'
output_file = 'output1.txt'

# Predefined short words for some common languages
short_words = {
    # Single-letter words
    'a': 'en', 'I': 'en', 'u': 'es', 'y': 'fr', 'e': 'it', 'o': 'it','à':'fr', 'ç':'fr','é':'fr','è':'fr', 
    # Two-letter words
    'to': 'en', 'in': 'en', 'an': 'en', 'is': 'en', 'on': 'en', 'by': 'en', 'at': 'en', 
    'de': 'de', 'es': 'es', 'en': 'es', 'la': 'es', 'el': 'es', 'le': 'fr', 'du': 'fr', 
    'il': 'it', 'un': 'it', 'di': 'it', 'al': 'it','ah':"fr",'ai':'fr','as':'fr','au':'fr','ça':'fr','ci':'fr','du':'fr','en':'fr','es':'fr','es':'fr','et':'fr','eu':'fr','il':'fr','la':'fr','le':'fr','le':'fr','le':'fr','he':'fr','li':'fr','ma':'fr','me':'fr','mi':'fr','ne':'fr','ni':'fr','nu':'fr','on':'fr','ou':'fr','où':'fr','sa':'fr','se':'fr','si':'fr','ta':'fr','te':'fr','tu':'fr','un':'fr',
#spanish
    'al':'es','él':'es','es':'es','he':'es','la':'es','le':'es','lo':'es','me':'es','mi':'es','no':'es','oy':'es','se':'es','si':'es','ti':'es','tu':'es','ya':'es',
    # Three-letter words
    'the': 'en', 'and': 'en', 'for': 'en', 'you': 'en', 'not': 'en', 'but': 'en', 
    'und': 'de', 'der': 'de', 'die': 'de', 'das': 'de', 'ein': 'de', 'ich': 'de',
    'que': 'es', 'los': 'es', 'con': 'es', 'por': 'es', 'del': 'es', 'las': 'es',
    'qui': 'fr', 'que': 'fr', 'les': 'fr', 'des': 'fr', 'une': 'fr', 'est': 'fr',
    'per': 'it', 'con': 'it', 'del': 'it', 'che': 'it', 'una': 'it', 'gli': 'it',
    # Add more words as needed
}

# Open input and output files
with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    # Read input file line by line
    for line in f_in:
        # Split line into words
        words = line.split()
        for word in words:
            if len(word) <= 3:
                # Assign the predefined language tag for short words if available
                lang = short_words.get(word.lower(), 'unknown')  # Use lower() for case-insensitivity
            else:
                # Detect language of each word
                lang, _ = langid.classify(word)
            # Write word and its language to output file
            f_out.write(f"[{lang}]{word}\n")
