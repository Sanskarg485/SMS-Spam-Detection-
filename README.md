# 📩 SMS Spam Classifier (Streamlit App)

A simple and interactive Streamlit web app that detects whether an SMS message is **spam** or **not spam** using a machine learning model trained on SMS data.

---

## 🚀 Features

- Classifies SMS messages as **Spam** or **Not Spam**
- Uses a pre-trained `KNeighborsClassifier` and `TfidfVectorizer`
- Built with **Streamlit** for an easy-to-use UI
- Real-time prediction with clear visual feedback
- Lightweight and runs locally

---

💬 NLP Technique Used
This project uses TF-IDF (Term Frequency–Inverse Document Frequency), a classic NLP technique, to convert raw SMS messages into numerical features that can be processed by a machine learning algorithm.

🔍 How it works:
TfidfVectorizer from scikit-learn is used.

It tokenizes the input text into words.

Calculates:

Term Frequency (TF): how often a word appears in a message.

Inverse Document Frequency (IDF): how rare the word is across all messages.

Multiplies TF and IDF to get a weighted score for each word.

The output is a sparse matrix representing each SMS numerically.

This matrix is then used as input to a KNeighborsClassifier model to predict whether the message is spam.

✅ TF-IDF is fast, interpretable, and performs well on small to medium-sized text classification tasks like spam filtering.



## 📁 Files

- `app.py`: Streamlit frontend app
- `SMS_Spam_Model.pkl`: Trained ML model (KNeighborsClassifier)
- `SMS_Vectorizer.pkl`: Pre-fitted TfidfVectorizer

---

## 🛠 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SMS-Spam-Detection.git
   cd SMS-Spam-Detection

▶️ Run the App
streamlit run app.py

