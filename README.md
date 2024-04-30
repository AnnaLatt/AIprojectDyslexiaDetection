<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# Project Title

Dyslexia Detection Ai Model

## Summary

Creating an AI model that detects dyslexia in students based on common error patterns in written text, aiming to provide early identification and support for individuals with dyslexia.


## Background

* Problem: Many individuals with dyslexia face challenges in academic and everyday settings due to undiagnosed conditions.
Solution: Developing an AI model to identify common error patterns indicative of dyslexia, aiding in early detection and intervention.
Motivation: Personal interest in leveraging AI for social good and improving accessibility in education.


## How is it used?

Usage: Users input written text for analysis to detect potential dyslexia indicators.
Situations: Valuable in educational settings, assessments, and for individuals seeking early dyslexia screening.
Users: Students, educators, and healthcare professionals concerned with dyslexia detection and support.

![Study](sarah-noltner-4U3d6u_p-fE-unsplash.jpg "Optional title)

Here's a code example, the full code is saved as codeforAiproject.py:

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

# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)

# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)

# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)
 
# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)

# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)
  

# Example usage
text = "She is playing wiht her friens at the place and they are supportive to every student and almoust all the teahers."
errors = identify_errors(text)
flag_dyslexia(errors, threshold=3)


## Data sources and AI methods
Data: A master's degree on the typical erros made by dyslexics in addition to my 15 years experience as an English teacher.
AI Methods: Utilizing pattern matching and comparison algorithms for error identification.


If you need to use links, here's an example:
[Master's Thesisby Heidi Valasjoki on Dyslexia and English as a Foreign Language](https://trepo.tuni.fi/bitstream/handle/10024/79113/gradu02527.pdf?sequence=1)


## Challenges

Limitations: The model may not capture all dyslexia variations or account for individual differences.
Ethical Considerations: Ensuring privacy and sensitivity in handling dyslexia-related data.

## What next?

Growth: Enhance the model with more error patterns and expand its application to diverse language contexts.
Skills Needed: Further AI development, collaboration with dyslexia experts, and data privacy expertise.


## Acknowledgments

Heidi Valasjoki and her thesis on Dyslexia and English as a Foreign Language


* list here the sources of inspiration 
* do not use code, images, data etc. from others without permission
* when you have permission to use other people's materials, always mention the original creator and the open source / Creative Commons licence they've used
  <br>For example: [Sleeping Cat on Her Back by Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
* etc
