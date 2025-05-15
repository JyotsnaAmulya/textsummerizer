from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

def text_summarizer(text, threshold):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    freq_table = dict()

    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    sentences = sent_tokenize(text)
    sentence_value = dict()

    for sentence in sentences:
        word_count_in_sentence = len(word_tokenize(sentence))
        for word in freq_table:
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq_table[word]
                else:
                    sentence_value[sentence] = freq_table[word]

        sentence_value[sentence] = sentence_value.get(sentence, 0) // word_count_in_sentence

    summary = ''
    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] >= threshold:
            summary += " " + sentence

    return summary

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        threshold = int(request.form["threshold"])
        summary = text_summarizer(text, threshold)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
