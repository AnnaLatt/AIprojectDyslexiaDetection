<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# AI-Powered Model for Detecting Dyslexia in English as a EFL

Final project for the Building AI course.

## Summary

Developing an AI-powered system to assist teachers in identifying signs of dyslexia in English language learners by analyzing students' written work and flagging common error patterns. This model aims to guide students towards formal assessment by providing teachers with early identification tools, enabling timely support and interventions for improved educational outcomes.


## Background

Detecting dyslexia is a challenging process in comprehensive and upper secondary schools, where I have worked as an English teacher for years. The lack of resources and the increasing number of students per group have compounded this issue. In Finland, where dyslexia and learning difficulties are identified using Finnish materials, there is a lack of available resources on common dyslexia-related mistakes in English. This lack of information can make it difficult for English teachers to get these observations further studied and addressed. 

Introducing a system that can automatically flag potential learning difficulties among learners would greatly facilitate the identification process and guide students towards formal testing. For instance, common errors include misspelling words like 'witch' instead of 'which', 'teh' instead of 'the', and 'almoust' instead of 'almost'. These mistakes can be indicative of dyslexia, but they are not always easy to spot. A system that can automatically identify these errors and flag them for further investigation would be a valuable tool in the detection and support of individuals with dyslexia.

A system that can automatically identify these errors and flag them for further investigation would be a valuable tool in the detection and support of individuals with dyslexia who encounter obstacles in academic and daily life settings due to undiagnosed conditions. Users who may benefit from this include students, educators, and healthcare professionals concerned with dyslexia detection and support.


## How is it used?

Teachers or other users can input a written text from a student for analysis to detect potential dyslexia indicators. The target users for this system include English teachers who are concerned with the early detection and support of individuals with dyslexia. For example, a teacher might input the following text from a student: "Teh books in my class are allways really booring staff and I almoust never read execpt when something is intresting." In this text, the system would flag words like 'teh', 'allways', 'booring', 'staff', 'almoust', 'execpt', 'intresting' as potential indicators of dyslexia.  When three mistakes are detected, the system presents the warning: "Dyslexia may be a possibility based on the identified words."


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Faber-Castell_pencil_and_eraser.jpg/640px-Faber-Castell_pencil_and_eraser.jpg" width="300">


Here's an example of the code, the full code is saved as codeforAiproject.py :

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



## Data sources and AI methods

The data that was used is from a master's degree by Heidi Valasjoki on Dyslexia and English as a Foreign Language in addition to my 15 years experience as an English teacher. It's worth noting that the data I've used to develop this system is limited, mainly coming from one master's thesis and my own observations of learning difficulties during my teaching career. I'm prioritizing the accuracy of the data over the amount of data, so that the patterns we identify are trustworthy indicators of dyslexia. The AI methods involve the use of pattern matching and comparison algorithms to identify errors.


## Challenges

The model developed may have limitations in capturing all the variations of dyslexia or accounting for individual differences. The dyslexia detection model could potentially produce false positives if it incorrectly identifies individuals without dyslexia as having the condition. As such, the system would need to be continuously refined and improved. Additionally, there are important ethical considerations to address, such as ensuring privacy and sensitivity in handling any data related to dyslexia. Maintaining the confidentiality and appropriate use of such sensitive information would be crucial.

## What next?

The model has the potential to improve by adding more error patterns and broadening its use to different language settings. Skills required include advancing AI technology, working together with dyslexia specialists, and having knowledge in safeguarding data privacy.


## Acknowledgments

[Heidi Valasjoki and her thesis on Dyslexia and English as a Foreign Language](https://trepo.tuni.fi/bitstream/handle/10024/79113/gradu02527.pdf?sequence=1)

picture: [Fabr Castell by Hawyih](https://commons.wikimedia.org/wiki/File:Faber-Castell_pencil_and_eraser.jpg#filelinks) / [CC BY 1.0](https://creativecommons.org/licenses/by/1.0)

I used [Perplexity](https://perplexity.ai) to help create the Python code for the dyslexia detection AI model.

I utilized [Replit](https://replit.com/~) to verify the functionality of the code. Additionally, I uploaded the code to GitHub.

