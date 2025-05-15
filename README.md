  **Text Summarization Web Application using NLTK and Flask**

Description:
This project is a basic **extractive text summarization tool**  built using **Python**, **NLTK (Natural Language Toolkit)**, and **Flask**.  
It allows users to input any text through a clean web interface, specify a threshold value, and instantly receive a summarized version by extracting key sentences based on word frequency.

Objectives:
- Apply **Natural Language Processing (NLP)** techniques like tokenization, stopword removal, and sentence scoring.
- Build a lightweight **web interface** for the summarizer using Flask.
- Provide control over **summary length** through a user-defined threshold.

  Tech Stack:
- **NLTK**
  - Word Tokenization
  - Sentence Tokenization
  - Stopwords Removal
- **Flask**
- **HTML/CSS**

 Features:
- **Text Input:** Enter or paste custom text.
- **Threshold Control:** Adjust a numeric threshold to modify the summary length.
- **Real-Time Summarization:** Get summarized content instantly.
- **Clean, Responsive UI:** Simple design with intuitive interface.


How It Works:
1. Text is tokenized into words.
2. Stopwords are removed.
3. A frequency table is built for remaining words.
4. Sentences are tokenized and scored based on the frequency table.
5. Sentences with a score above the user-defined threshold are included in the summary.
6. Summary is displayed on the same web page.

