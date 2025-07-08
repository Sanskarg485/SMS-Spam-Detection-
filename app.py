import streamlit as st
import joblib
import os

model_path = "SMS_Spam_Model.pkl"
vectorizer_path = "SMS_Vectorizer.pkl"

# Check file existence
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    st.error("❌ Model or vectorizer file not found. Please make sure both `.pkl` files exist.")
else:
    # Load model and vectorizer
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    # Streamlit UI
    st.set_page_config(page_title="SMS Spam Classifier", layout="centered")
    st.title("📩 SMS Spam Classifier")
    st.write("Enter a message to check if it's **spam** or **not spam**.")

    message = st.text_area("Enter SMS Message:")

    if st.button("Classify"):
        if message.strip() == "":
            st.warning("Please enter a message.")
        else:
            input_vector = vectorizer.transform([message])
            prediction = model.predict(input_vector)[0]
            label = "🔴 Spam" if prediction == 1 else "🟢 Not Spam"
            st.markdown(f"### Prediction: {label}")
            st.success("✅ Classification completed successfully!")
            st.balloons()   
            st.write("Thank you for using the SMS Spam Classifier!")
            st.write("Feel free to enter another message or close the app.")
            st.write("Made with ❤️ [by Sanskar Gupta] (https://www.linkedin.com/in/sanskar-gupta-6253a0294)")
            st.write("If you have any feedback or suggestions, please let me know!")
            st.write("You can also check the source code on [GitHub](https://github.com/yourusername/SMS-Spam-Detection)")
            st.write("Have a great day! 😊"
            )
            st.write("For more information, visit the [project documentation](https://yourprojectdocumentationlink.com)")
            st.write("If you encounter any issues, please check the [troubleshooting guide](https://yourtroubleshootingguidelink.com)")
            st.write("Thank you for using the SMS Spam Classifier! 😊")
            st.write("If you have any questions or need assistance, feel free to reach out!")
            st.write("You can also check the [GitHub repository](https://github.com/yourusername/SMS-Spam-Detection)")