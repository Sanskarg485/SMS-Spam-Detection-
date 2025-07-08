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

