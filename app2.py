import streamlit as st
import joblib
from transformers import AutoTokenizer, AutoModelForSequenceClassification

def load_model():
    model = joblib.load('logit_model.pkl')
    vectorizer = joblib.load('PlengP/vectorizer')
    return model, vectorizer

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')  # make tokens after splitting by slash
    total_Tokens = []

    for i in tkns_BySlash:
        tokens = str(i).split('-')  # make tokens after splitting by dash
        tkns_ByDot = []

        for j in range(0, len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')  # make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens

        total_Tokens = total_Tokens + tokens + tkns_ByDot
        total_Tokens = list(set(total_Tokens))  # remove redundant tokens

    if 'com' in total_Tokens:
        total_Tokens.remove('com')
    if 'https:' in total_Tokens:
        total_Tokens.remove('https:')
    if 'http:' in total_Tokens:
        total_Tokens.remove('http:')
    if 'www' in total_Tokens:
        total_Tokens.remove('www')


    return total_Tokens

def main():
    # Set the title and description of the app
    st.title('Welcome to Phish-Off 2.0!')
    st.write('paste your URL here . . .')

    # Load the model
    model, vectorizer = load_model()
  
    # Display an input field for the user to enter data
    input_data = st.text_input( '...')

    if st.button('Predict'):
        # Perform predictions using the loaded model
        input_data = vectorizer.transform([input_data])
        result = model.predict(input_data)

        # Display the result
        st.write('Prediction:', result)


if __name__ == "__main__":
    main()
