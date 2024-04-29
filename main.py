# Dictionary of common error patterns and corrections
error_patterns = {
    'witch': 'which',
    'teh': 'the',
    'wnat': 'want',
    'thier': 'their',
    'waht': 'what',
    'wher': 'where',
    'tehre': 'there',
    'teh ': 'the ',
    ' teh': ' the',
    'lot of': 'a lot of',
    'intresting': 'interesting',
    'execpt': 'except',
    'wich': 'which',
    'were': 'where',
    'parens': 'parents',
    'telvision': 'television',
    'almoust': 'almost',
    'booring': 'boring',
    'wiht': 'with',
    'ther': 'their',
    'friens': 'friends',
    'enof': 'enough',
    'sed': 'said',
    'now': 'know',
    'mohter': 'mother',
    'staff': 'stuff',
    'destroyed': 'destroyed',
    'studend': 'student',
    'halv': 'half',
    'plaze': 'place',
    'teknical': 'technical',
    'musik': 'music',
    'qreat': 'great',
    'teathers': 'teachers',
    'allways': 'always',
    'usuall': 'usual',
    'traditionall': 'traditional',
    'tree': 'three',
    'sheself': 'herself',
    'morrong': 'morning',
    'restaurang': 'restaurant'
}

def identify_errors(text):
    words = text.split()
    errors = []

    for word in words:
        if word.lower() in error_patterns:
            errors.append((word, error_patterns[word.lower()]))

    return errors

def flag_dyslexia(errors, threshold=3):
    if len(errors) >= threshold:
        print("Warning: Dyslexia may be a possibility based on the identified words.")
        print("Incorrect words:")
        for word, correction in errors:
            print(f"'{word}' should be '{correction}'")
    else:
        print("No dyslexia flagged. Incorrect words:")
        for word, correction in errors:
            print(f"'{word}' should be '{correction}'")

# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)